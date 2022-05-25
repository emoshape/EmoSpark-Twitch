# Import libraries
import logging
import os
import sys
import traceback
from typing import Any, Dict, List

import yaml
from aiohttp import ClientSession
from aiohttp.web_runner import GracefulExit
from twitchio.ext import commands


# Define function to process yaml config file
def process_config_file() -> Any:
    with open("config.yaml", "r") as stream:
        config_options = yaml.safe_load(stream)

    return config_options


# Define Bot class
class Bot(commands.Bot):
    SEND_API = "https://emohuman.com/send_text"

    def __init__(
        self,
        access_token: str,
        prefix: str,
        initial_channels: List[str],
        conf_options: Dict[str, Any],
    ):
        """
        Tells the Bot class which token it should use, channels to connect to and prefix to use.
        """
        self.conf_options = conf_options
        super().__init__(token=access_token, prefix=prefix, initial_channels=initial_channels)

    async def ainit(self) -> None:
        self.session = ClientSession()


if __name__ == "__main__":
    conf_options = process_config_file()
    if conf_options["APP"]["DEBUG"] == True:
        logging.basicConfig(level=logging.DEBUG)
    channel_names = []
    for channel in conf_options["APP"]["ACCOUNTS"]:
        channel_names.append("#" + channel["name"])
    bot = Bot(
        access_token=conf_options["APP"]["ACCESS_TOKEN"],
        prefix="!",
        initial_channels=channel_names,
        conf_options=conf_options,
    )

    for filename in os.listdir("./modules/cogs/"):
        if filename.endswith(".py"):
            try:
                bot.load_module(f"modules.cogs.{filename.strip('.py')}")
            except Exception:
                print(f"Failed to load extension modules.cogs.{filename}.", file=sys.stderr)
                traceback.print_exc()

    bot.loop.create_task(bot.ainit())
    bot.loop.create_task(bot.connect())
    try:
        bot.loop.run_forever()
    except GracefulExit:
        sys.exit(0)
