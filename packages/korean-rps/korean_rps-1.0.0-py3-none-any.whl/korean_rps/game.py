import random

class Rps:
  list = ['가위', '바위', '보']
  data = {0 : True, 1 : False, 2 : 0}

  def play(self, user : str):
    if not user in self.list:
      return None

    bot = random.choice(self.list)
    if user == bot:
      stat = 2
    elif user == '가위' and bot == '바위':
      stat = 1
    elif user == '바위' and bot == '보':
      stat = 1
    elif user == '보' and bot == '가위':
      stat = 1
    else:
      stat = 0
    result = {}
    result['result'] = self.data[stat]
    result['user'] = user
    result['bot'] = bot
    return result

  def emoji(self, text):
    if text == '가위':
      return '✌️'
    elif text == '보':
      return '🖐️'
    elif text == '바위':
      return '✊'
    else:
      return None