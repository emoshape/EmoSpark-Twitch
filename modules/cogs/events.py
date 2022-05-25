import twitchio
from twitchio.ext import commands


class EventsCog(commands.Cog):
    def __init__(self, bot: commands.Cog) -> None:
        self.bot = bot

    @commands.Cog.event()
    async def event_ready(self) -> None:
        """
        Ptints who the bot is logged in as when ready.
        """
        print(f"Logged in as | {self.bot.nick}")

    @commands.Cog.event()
    async def event_message(self, message: twitchio.Message) -> None:
        """
        Ignore messages sent by the bot and handle the commands, and send messages to API.
        """
        if message.echo:
            return
        accounts = self.bot.conf_options["APP"]["ACCOUNTS"]
        account = accounts[0]

        ## Send message to API

        send_data = {
            "secret": f"{account['metasoul_api_key']}",
            "epuid": f"{account['metasoul_epuid']}",
            "message": f"{message.content}",
        }
        async with self.bot.session.post(self.bot.SEND_API, json=send_data) as r:
            json_data = await r.json(content_type="application/json")
            print(json_data)

        ## Print message to console

        print(message.content)


def prepare(bot: commands.Bot) -> None:
    bot.add_cog(EventsCog(bot))
