import discord
from prediction import Prediction
from asyncio import sleep

intents = discord.Intents().default()
intents.message_content = True

roles = {'1373073557805863003': 89, '1373073595504529601': 95, '1373073617809702943': 99}

class Bot(discord.Client):
  async def predictor(self, channel, role):
      pred = Prediction(role, 3)
      msg = await channel.send('```\nLoading\n``` ')

      for i  in range (5):
        await sleep(0.5)
        await msg.edit(content=f'```\n{'Loading' + '.'*i}\n``` ')

      await msg.edit(content='', embed=pred.embed())

  async def on_message(self, msg : discord.Message):
      if msg.author.bot: return
      if not msg.content == 'svp60' and not msg.channel.name == 'tickets': return

      role = next(roles[str(r.id)] for r in msg.author.roles if str(r.id) in roles)

      await self.predictor(msg.channel, role)

if __name__ == '__main__':
  bot = Bot(intents=intents)
  bot.run('MTM3MzAzOTY4Nzg5MTE1NzEzMw.G363hU.eHogvntKObBJ0eDc8usl9G4YlQvBtdG7U6uG90')
