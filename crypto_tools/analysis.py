# analysis tools for crypto root me challenge, write function here

def frequency(string, maximum=False):
  """Count the number of occurrences contained in the string \n Returns a tuple (key, value) if maximum's true else returns the dict
  """
  if len(string):
    # Formatting string
    string = string.lower()
    # Generating alphabet
    alphabet = dict([(chr(x), string.count(chr(x))) for x in range(97, 123)])



    if maximum == True:
      values = list(alphabet.values())
      maximum_value = max(values)

      for key in alphabet.keys():
        if alphabet.get(key) == maximum_value:
          return (key, maximum_value)
    else:
      return alphabet


def firstLetters(message):
    return [letter[0] for letter in message.split()]

def lastLetters(message):
    return [letter[-1:] for letter in message.split()]
