text = input()
def double(str):
  alphabet = ('abcdefghijklmnopqrstuvwxyzабвгдеєжзиїйклмнопрстуфхцчшщьюя')
  new_str = ''
  for c in str:
    if c.lower() in alphabet:
      new_str += c
    new_str += c
  return new_str
print(double(text))