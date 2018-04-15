# Résolution du challenge ENCODE - ASCII
# Lien : https://www.root-me.org/fr/Challenges/Cryptanalyse/Encodage-ASCII

message = "4C6520666C6167206465206365206368616C6C656E6765206573743A203261633337363438316165353436636436383964356239313237356433323465"
clear_message = []

for i in range(len(message) - 1):
    if i % 2 == 0:
        temp = int(f"0x{message[i]}{message[i+1]}", 16)
        clear_message.append(chr(temp))


clear_message = "".join(clear_message)
print(clear_message)
