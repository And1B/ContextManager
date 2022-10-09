from contextlib import contextmanager

@contextmanager
def generic(card_type, sender_name):
  generic_card = open(card_type, 'r')
  sender_card = open(f'{sender_name}_generic.txt', 'w')
  try:
    yield sender_card.write(f"Dear {sender_name}\n{generic_card.read()}\nSincerely, {sender_name}")
  finally:
    generic_card.close()
    sender_card.close()

with generic('thankyou_card.txt', 'Mwenda') as mwenda:
  print('Card Generated!')
with open('Mwenda_generic.txt', 'r') as mwenda_card:
  print(mwenda_card.read())

class personalized:
  def __init__(self, senders_name, receivers_name):
    self._senders_name = senders_name
    self._receivers_name = receivers_name
    self.file = open(f'{self._senders_name}_personalized.txt', 'w')

  def __enter__(self):
    self.file.write(f'Dear {self._receivers_name}\n')
    return self.file

  def __exit__(self, *exc):
    self.file.write(f'Sincerely {self._senders_name}')
    self.file.close()

with personalized('John', 'Michael') as greeting_card:
  greeting_card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don't say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.\n")

with generic("happy_bday.txt", "Remy") as generic_card, personalized("Josiah", "Esther") as personalized_card:
  personalized_card.write("Happy Birthday!! I love you to the moon and back. Even though you're a pain sometimes, you're a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You're getting old!\n")

with open('Josiah_personalized.txt', 'r') as esther_card:
  print(esther_card.read())


