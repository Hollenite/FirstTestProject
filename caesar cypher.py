logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift NUMBER:\n"))


list_of_text = list(text)
def encrypt(shift_text):
    display = ""
    indexn = []
    for n in range(len(text)):
        # print(text[n])
        if text[n] not in alphabet:
            indexn.append(-1)
        else:
            indexn.append((alphabet.index(text[n])))
        # print(indexn)
        value = indexn[n] + shift_text
        if indexn[n] == -1:
            display += text[n]
        else:
            if value >= 26:
                if shift_text >= 26:
                    shift_text %= 26
                    # print(indexn[n] + shift_text)
                    if indexn[n] + shift_text >= 26:
                        indexn[n] -= 26
                else:
                    indexn[n] -= 26
        if indexn[n] != -1:
            display += alphabet[int(indexn[n]) + shift_text]
    print(display)
    # print(list(display))

def decrypt(cipher_shift):
    display = ""
    indexn = []
    for n in range(len(text)):
        # print(text[n])
        if text[n] not in alphabet:
            indexn.append(-1)
        else:
            indexn.append((alphabet.index(text[n])))
        # print(indexn)
        value = indexn[n] - cipher_shift
        if indexn[n] == -1:
            display += text[n]
        else:
            if value < 0:
                if cipher_shift >= 26:
                    cipher_shift %= 26
                    print(indexn[n] - cipher_shift)
                    if indexn[n] - cipher_shift < 0:
                        indexn[n] += 26
                else:
                    indexn[n] += 26
        if indexn[n] != -1:
            display += alphabet[int(indexn[n]) - cipher_shift]
    print(display)
    # print(list(display))

if direction == 'encode':
    encrypt(shift_text=shift)
elif direction == 'decode':
    decrypt(cipher_shift=shift)
else:
    print("Invalid direction")

continue1 = input("Press yes to continue and no to stop\n")
while continue1 == "yes":
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    list_of_text = list(text)
    if direction == 'encode':
        encrypt(shift_text=shift)
    elif direction == 'decode':
        decrypt(cipher_shift=shift)
    else:
        print("Invalid direction")
    continue1 = "no"
    continue1 = input("Press yes to continue and no to stop\n")
