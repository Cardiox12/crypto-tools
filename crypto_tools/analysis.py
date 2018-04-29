# analysis tools for crypto root me challenge, write function here
from terminaltables import AsciiTable


def frequency(message, maximum=False, display=False):
  """
    Analyse the frequency of a string

    :param message: The message you want to analyse 
    :type message: string
    :param maximum: Optional argument, if True return the character and the maximum
    :maximum type: boolean  
    :param display: Optional argument, if True pretty print the frequency
    :display type: boolean
    :returns: 
      if maximum is set to False, by default it returns a dictionnary with every character and their occurences 
      if maximum is set to True it returns a tuples containing the character and the maximum
    :rtypes: 
      if maximum is set to True : tuples
      if maximum is set to True : dict
  """
  if len(message):
    # Formatting string
    message = message.lower()
    # Generating alphabet
    alphabet = dict([(chr(x), message.count(chr(x))) for x in range(97, 123)])


    if display == True:
        datas = [alphabet.keys(), alphabet.values()]
        table = AsciiTable(datas)
        print(table.table)

    if maximum == True:
        values = list(alphabet.values())
        maximum_value = max(values)

        for key in alphabet.keys():
          if alphabet.get(key) == maximum_value:
              return (key, maximum_value)
    else:
        return alphabet


def firstLetters(message):
  """ 
    Get the first letters of a string
    :param message: The message you want to analyse
    :type message: string
    :returns: Returns the first letters of the string passed in param
    :rtypes: list
  """
  return [letter[0] for letter in message.split()]

def lastLetters(message):
  """ 
    Get the last letters of a string
    :param message: The message you want to analyse
    :type message: string
    :returns: Returns the last letters of the string passed in param
    :rtypes: list
  """
  return [letter[-1:] for letter in message.split()]



