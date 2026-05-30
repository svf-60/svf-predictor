from discord import Embed

class ErrorEmbeds:
    MISSINGANYROLE= {
        "description": "You are not a member yet! Pay and sign up to get the best predictors and make bank \U0001F4B8...",
        "fields": [],
        "title": "\U0001F6AB Not a member yet... \U0001F6AB"
    }

    MISSINGREQUIREDARGUEMENT= {
        "description": "\U000026A0 Enter the valid arguments, so our predictor can work best for you and make you some money! \U000026A0",
        "fields": [],
        "title": "\U00002753 Bad arguments.... \U000026A0"
    }      

def get_embed(name : str):
    return Embed.from_dict(getattr(ErrorEmbeds, name.upper()))