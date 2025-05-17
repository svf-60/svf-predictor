import random
from discord import Embed

percentages = ('.69','.79','.89','.99', '.95', '.97', '.93', '.88',)
alg_models = ['AlphaZero', 'MuZero', 'Deep Q-Network', 'Bayesian Optimization']

round_ids = [
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

class Prediction:
  def __init__(self, percentage, mines):
    random.seed()

    mmap = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
    for _ in range(mines):
      random.choice(mmap)[random.randint(0, 4)] = 0

    self.mines = mmap
    self.guessRate = str(percentage) + random.choice(percentages)

  def embed(self):
      return Embed.from_dict({
      "title": "\U0001F4AF **SVP60's PREDICTOR** \U0001F4AF",
      "description": "We appreciate you choosing our tool. \n Your trust means a lot to us, and we're glad we could support your decision-making. \nIf you have any feedback or suggestions, we’d love to hear from you!",
      "fields": [
        {
          "name": "\U0001F4B8 Algorithm Prediction",
          "value": f'{repr(self)}',
        },
        {
          "name": '\U0001F4A3 Bomb Probability Index',
          "value": f'{str(self.guessRate) + '9'*8}%',
          'inline':True
        },
        {
          "name": "\U0001F916 Algorithm Model",
          "value": f'{random.choice(alg_models)}',
          'inline':True
        },
        {
          "name": "\U0001FAAA Round ID",
          "value": f'{random.choice(round_ids)}',
        }
      ]
      })

  def __repr__(self):
    emoji_list = [['\U0001F7E9' if i == 1 else '\u274C' for i in x] for x in self.mines]

    return ''.join(f'{i}' + '\n' for i in emoji_list).replace("'", '')
