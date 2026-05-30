from discord import Intents as DiscordIntents
from discord.ext import commands

INTENTS = DiscordIntents().default()
INTENTS.message_content = True

initial_extensions = [
    'cogs.predictor',
    'cogs.admin'
]

class PredictorBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix='$', intents=INTENTS)

        self.token = ''

    async def setup_hook(self):
        for extension in initial_extensions:
            try:
                await self.load_extension(extension)
                print(f'Loaded {extension}')

            except Exception as e:
                print(f'Exception caught; unable to load extension {e}/{type(e)}')

    def run(self, reconnect=True):
        super().run(self.token, reconnect=reconnect)

if __name__ == '__main__':
    PredictorBot().run()
