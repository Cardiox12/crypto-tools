# substitute tools for crypto root me challenge, write function here
import string 

def decode(message, shift):
  ascii_codes = [ord(x) for x in message.lower()]
  final_message = []

  for ascii in ascii_codes:
    if (chr(ascii)).isalpha():
      if ascii - shift < 97:
        final_message.append((122 - 97 % (ascii - shift)) + 1)
      else:
        final_message.append(ascii - shift)
    else:
        final_message.append(ascii)

  return "".join([chr(x) for x in final_message])


def encode(message, shift):
  ascii_codes = [ord(x) for x in message.lower()]
  final_message = []

  for ascii in ascii_codes:
    if (chr(ascii)).isalpha():
      if ascii + shift > 122:
        final_message.append(96 + (ascii + shift) % 122)
      else:
        final_message.append(ascii + shift)
    else:
        final_message.append(ascii)

  return "".join([chr(x) for x in final_message])


def brute_force(message):
  messages = []

  for i in range(26):
    messages.append(decode(message, i))

  return messages


def decode_simple(message, shift):
  ascii_codes = [ord(x) for x in message]
  final_message = []

  for ascii in ascii_codes:
    if (chr(ascii)).isalpha():
      if ascii - shift < 0:
        final_message.append(256 - (ascii - shift))
      else:
        final_message.append(ascii - shift)
    else:
        final_message.append(ascii)


  return "".join([chr(x) for x in final_message])


def brute_force_simple(message):
  messages = []

  for i in range(256):
    messages.append(decode_simple(message, i))

  return messages
