import random

from embeds.error import get_embed as get_error_embed
from embeds.prediction import get_embed as get_prediction_embed

from string import ascii_letters, digits

from discord import Embed, app_commands
from discord.ext import commands

from asyncio import sleep

VALID_ROLE_IDS = [ 1381802014492590082, 1381802014492590081, 1381802014492590083 ]

PERCENTAGES = ['.69','.79','.89','.99', '.95', '.97', '.93', '.88']

ROUND_IDS = [
    "Z81QK-9T7MG-KDN4U28MW3",
    "F4X2P-B91RV-03A7ZL8KCN",
    "M7NWD-CR6T1-Q9VK2HZ0AE",
    "L3BXP-VRA29-GTXKM408DU",
    "92KMQ-XEZ75-NCD8M32LQW",
    "Y7HRA-PTQ5Z-94UVM23KLE",
    "KN304-WVZQR-M81GTX2LDU",
    "BRX29-7FA2E-MCWKZ1N830",
    "H05MC-L7ZQP-T94XNWA38D",
    "X9G3R-M5PLD-KWNCV7Q108",
    "WDNX5-QBRL0-ZPTU7C34VM",
    "PZ72L-K9Q8R-T4XWCG31DN",
    "MJQ5A-XTN04-LWZB8C93VE",
    "V0KCN-RL79T-82XMQAZPWD",
    "C93QP-H2XLM-KBVW8740NZ",
    "74ZTN-K9BWP-RQEMVXA813",
    "NXP3C-LBRZ8-1AVTQMKW29",
    "TLM90-ZX3PW-C2VBQ7RDAE",
    "K2R8Z-PMX0W-LT9V3JCAQN",
    "XA41M-VRQ9B-KNZT2LG38W"
]

GAME_TYPES = { 1: "Mines", 2: "Dice"}

ROLE_IDS = { 1381802014492590081: '89', 1381802014492590082: '95', 1381802014492590083: '99' }

class Prediction:
    def __init__(self, role_id, phrase_id, type):
        random.seed()

        self.role_id = role_id
        self.phrase_id = phrase_id
        
        self.uid = ''.join(random.choices(ascii_letters + digits, k=12))
        
        self.game_type = type
        self.display = ""
        
    def generate_dice_roll(self, condition, limit):
        min = 0.01 if not condition else limit
        max = 100.00 if condition else limit
        
        roll = random.uniform(min, max)
        
        self.display = f"{roll:.2f}"

    def generate_mine_map(self, amount):
        mine_map = [[1]*5 for _ in range(5)]
        
        for r, c in random.sample([(i, j) for i in range(5) for j in range(5)], amount):
            mine_map[r][c] = 0        
        
        emoji_list = [['\U0001F7E9' if i == 1 else '\u274C' for i in x] for x in mine_map]

        self.display = ''.join(f'{i}' + '\n' for i in emoji_list).replace("'", '')

    def embed(self):
        guess_rate = ROLE_IDS[self.role_id] + random.choice(PERCENTAGES)
        game_type = GAME_TYPES[self.game_type]
        
        return Embed.from_dict({
            "title": f"**{game_type.upper()}_PREDICTION @ ID *{self.uid}***",
            "description": f"Your prediction for the upcoming {game_type.lower()} game has been generated with precision. *Thank you for choosing our tool—built to give you confidence before every move.* ||**\nClient Seed Phrase: { self.phrase_id }**||",
            "fields": [
                {
                    "name": "\U0001F4B8 Algorithm Prediction",
                    "value": f'{self.display}',
                },
                {
                    "name": f'\U0001F4A3 {game_type} Probability Index',
                    "value": f'{str(guess_rate) + '9' * 8}%',
                    'inline':True
                },
                {
                    "name": "\U0001FAAA Algorithm ID",
                    "value": f'{random.choice(ROUND_IDS)}',
                }
                ]
            })

class Predictor(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="predict_mines", description="Get your next big win! Using the best tool in the game.")
    @app_commands.guilds(1381802014492590080)
    @app_commands.describe(
        mines="The amount of mines in the round.",
    )
    @app_commands.checks.has_any_role(*VALID_ROLE_IDS)
    async def predict_mines(
            self, interaction,
            mines : app_commands.Range[int, 1, 24], client_phrase : app_commands.Range[str, 13, 15]):
        role_id = next((role.id for role in interaction.user.roles if role.id in VALID_ROLE_IDS), None)
        
        prediction = Prediction(role_id, client_phrase, 1)
        prediction.generate_mine_map(mines)
        
        await interaction.response.send_message(embed=get_prediction_embed('loading'), ephemeral=True)
        await sleep(2)
        
        msg = await interaction.original_response()
        
        await msg.edit(embed=prediction.embed())
        
    @app_commands.command(name="predict_dice", description="Dice dice dice! Predict the next required roll!")
    @app_commands.guilds(1381802014492590080)
    @app_commands.describe(
        condition="Choose whether the roll must land over or under the target.",
        limit="Enter the target number for the roll."
    )
    @app_commands.checks.has_any_role(*VALID_ROLE_IDS)
    async def predict_dice(
            self, interaction,
            condition: bool, limit: app_commands.Range[float, 0.01, 99.99], client_phrase : app_commands.Range[str, 13, 15]):
        role_id = next((role.id for role in interaction.user.roles if role.id in VALID_ROLE_IDS), None)
        
        prediction = Prediction(role_id, client_phrase, 2)
        prediction.generate_dice_roll(condition, limit)
        
        await interaction.response.send_message(embed=get_prediction_embed('loading'), ephemeral=True)
        await sleep(2)
        
        msg = await interaction.original_response()
        
        await msg.edit(embed=prediction.embed())  
        
    @app_commands.command(name="how-to-get-client-phrase", description="Don't know how to get the client phrase? Use this command!")
    @app_commands.guilds(1381802014492590080)
    async def get_client_phrase(self, interaction):
        await interaction.response.send_message(embed=get_prediction_embed('client_phrase_help'), ephemeral=True)

    @app_commands.command(name="help", description="Need help? Use this command!")
    @app_commands.guilds(1381802014492590080)
    async def help(self, interaction):
        await interaction.response.send_message(embed=get_prediction_embed('help'), ephemeral=True)

    @predict_dice.error
    @predict_mines.error
    async def on_predict_error(self, interaction, error):
        await interaction.response.send_message(embed=get_error_embed(error.__class__.__name__), ephemeral=True)

async def setup(bot):
    await bot.add_cog(Predictor(bot))
