import json
import logging
from datetime import datetime, timedelta
from os import environ, path
from typing import Optional

from disnake import Client, Guild
from dotenv import load_dotenv
from ics import Calendar, ContentLine, Event
from ics.alarm import DisplayAlarm
from quart import Quart, redirect, render_template, request, url_for
import sentry_sdk
from sentry_sdk.integrations.quart import QuartIntegration
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware  # type: ignore

load_dotenv()

QUART_DEBUG = environ.get("QUART_DEBUG", False)
DISCORD_TOKEN = environ.get("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise Exception("Missing DISCORD_TOKEN")

if QUART_DEBUG:
    logging.basicConfig(level=logging.DEBUG)

SENTRY_DSN = environ.get("SENTRY_DSN")
if SENTRY_DSN:
    sentry_sdk.init(SENTRY_DSN, integrations=[QuartIntegration()])


class Discord(Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!", flush=True)


client = Discord()
app = Quart(__name__)
app.asgi_app = ProxyHeadersMiddleware(app.asgi_app, "*")  # type: ignore


def get_guild_by_id(guild_id: str) -> Optional[Guild]:
    if guild_id:
        for guild in client.guilds:
            if str(guild.id) == guild_id or guild.vanity_url_code == guild_id:
                return guild
    return None


CATALOG_CACHE = {}


@app.errorhandler(500)
async def errorhandler(error: Exception):
    print(f"\33[31m{error}\33[m", flush=True)
    return await render_template("error.html.j2", error=str(error)), 500


@app.errorhandler(404)
async def not_found(error: Exception):
    return await render_template("error.html.j2", error=str(error)), 404


def i18n(str: str) -> str:
    lang = request.accept_languages.best_match(["en", "fr"])

    if lang not in CATALOG_CACHE:
        catalog_file = f"{path.dirname(__file__)}/translations/{lang}.json"
        if path.exists(catalog_file):
            with open(catalog_file) as catalog_json:
                catalog = json.load(catalog_json)
                CATALOG_CACHE[lang] = catalog

    if lang in CATALOG_CACHE and str in CATALOG_CACHE[lang]:
        return CATALOG_CACHE[lang][str]

    return str


def days_before_failure() -> int:
    nextYear = datetime.today().year + 5 - ((datetime.today().year + 5) % 5)
    nextDate = datetime(year=nextYear, month=6, day=3)
    nextDelta = nextDate - datetime.now()

    return nextDelta.days


@app.context_processor
def context_processor():
    return dict(_=i18n, client=client, days_before_failure=days_before_failure())


@app.route("/")
async def index():
    guild_id = request.args.get("guild")
    guild = get_guild_by_id(guild_id)

    if guild:
        return redirect(url_for(".subscribe", guild_id=guild_id))

    return await render_template("index.html.j2")


@app.route("/subscribe/<guild_id>")
async def subscribe(guild_id: str):
    guild = get_guild_by_id(guild_id)
    if guild is None:
        return redirect(url_for(".index"))

    return await render_template("subscribe.html.j2", guild=guild)


@app.route("/<guild_id>.ics")
async def ical(guild_id: str):
    guild = get_guild_by_id(guild_id)
    if guild is None:
        return redirect(url_for(".index"))

    calendar = Calendar()

    calendar.extra.append(ContentLine(name="REFRESH-INTERVAL", value="PT1H"))
    calendar.extra.append(ContentLine(name="X-PUBLISHED-TTL", value="PT1H"))

    calendar.extra.append(ContentLine(name="NAME", value=guild.name))
    calendar.extra.append(ContentLine(name="X-WR-CALNAME", value=guild.name))

    if guild.description:
        calendar.extra.append(ContentLine(name="DESCRIPTION", value=guild.description))
        calendar.extra.append(ContentLine(name="X-WR-CALDESC", value=guild.description))

    for scheduled_event in guild.scheduled_events:
        event = Event()
        event.summary = scheduled_event.name
        event.begin = scheduled_event.scheduled_start_time
        event.end = scheduled_event.scheduled_end_time
        event.duration = timedelta(hours=2)
        event.uid = str(scheduled_event.id)
        event.description = scheduled_event.description
        event.url = f"https://discord.com/events/{guild_id}/{scheduled_event.id}"
        event.location = (
            scheduled_event.entity_metadata.location
            if scheduled_event.entity_metadata
            else None
        )

        alarm = DisplayAlarm()
        alarm.trigger = timedelta(hours=-1)
        event.alarms.append(alarm)

        calendar.events.append(event)

    return calendar.serialize()


quart_task = client.loop.create_task(app.run_task("0.0.0.0"))
quart_task.add_done_callback(lambda f: client.loop.stop())
client.run(DISCORD_TOKEN)
