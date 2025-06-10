alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


list_of_text = list(text)
def encrypt():
    display = ""
    indexn = []
    for n in range(len(text)):
        print(text[n])
        indexn.append((alphabet.index(text[n])))
        print(indexn)
        if indexn[n] + shift > 25:
            value = indexn[n] + shift
            indexn[n] = value - (25+shift+1)

        display += alphabet[int(indexn[n]) + shift]
    print(alphabet.index(text[n]))
    print(display)
    print(list(display))

if direction == 'encode':
    encrypt()

