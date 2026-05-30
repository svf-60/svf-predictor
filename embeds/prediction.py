from discord import Embed

class PredictionEmbeds:
    LOADING = {
        'description': '*Loading...*',
        'fields': [],
        'title': '**Please wait....**'
    }
    
    HELP = {
        'description': '**Get started in seconds:**\n\nUse `/predict_mines` or `/predict_dice` to generate a prediction for your next round.\n\n**Command Formats**\n`/predict_mines:<1-24> client_phrase:<3-64 characters>`\n`/predict_dice condition:<over/under> limit:<0.01-99.99> client_phrase:<3-64 characters>`\n\n**Arguments**\n**For `/predict_mines`**\n• `mines` → Enter how many mines the game has, from **1 to 24**.\n• `client_phrase` → Enter your client phrase, between **3 and 64 characters**.\n\n**For `/predict_dice`**\n• `condition` → Choose whether the roll must land **over** or **under** the target.\n• `limit` → Enter the target number for the roll, from **0.01 to 100.00**.\n• `client_phrase` → Enter your client phrase, between **3 and 64 characters**.\n\n**Examples**\n`/predict_mines:5 client_phrase:myluck123`\n`/predict_dice condition:under limit:49.50 client_phrase:myluck123`\n\n**Tips**\n• Make sure your settings match your game exactly.\n• Double-check your mine count, roll condition, and target before predicting.\n• Your seed or phrase must meet the required character length.\n• Accurate inputs give the best prediction experience.',
        'fields': [],
        'title': '**HOW TO USE THE PREDICTOR?**'
    }
    
    CLIENT_PHRASE_HELP = {
        'description': '**Find your client phrase in seconds:**\n\nFirst, go to the site and open the game you want to play.\n\nThen click **Fairness**.\nIf there is a **Seed** tab, open it.\nLook for **Active Client Seed** and copy it exactly as shown.\n\n**Where to use it**\n• Use that value as your `client_phrase` when running `/predict_mines` or `/predict_dice`.\n\n**Tips**\n• Make sure you copy the **active** client seed, not an old one.\n• Double-check for extra spaces before submitting.\n• If the Fairness menu has multiple tabs, always check **Seed** first.\n• Your client phrase must be between **3 and 64 characters**.',
        'fields': [],
        'title': '**HOW TO GET CLIENT PHRASE?**'
    }

def get_embed(name : str):
    return Embed.from_dict(getattr(PredictionEmbeds, name.upper()))
