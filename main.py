alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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
wanna_play = True
while wanna_play:
    direction = int(input("Type '1' to encrypt, type '2' to decrypt:\n"))
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift >= 27:
        shift = shift % 26
    def encrypt(plain_text, shift_amount):
        chipher_text = ""
        for char in plain_text:
            if char in alphabet:
                possition = alphabet.index(char)
                new_possition = possition + shift_amount
                if new_possition >= 25:
                    new_possition -= 26
                
                new_letter = alphabet[new_possition]
                chipher_text += new_letter
            else:
                chipher_text += char    
        print(f"The encoded text is {chipher_text}")


    def decrypt(plain_text2, shift_amount2):
        decrypt_text = ""
        for char in plain_text2:
            if char in alphabet:
                possition = alphabet.index(char)
                new_possition = possition - shift_amount2
                if new_possition <= -1:
                    new_possition += 26
                new_letter = alphabet[new_possition]
                decrypt_text += new_letter
            else:
                decrypt_text += char     
        print(f"The decoded text is {decrypt_text}")           
            


    if direction == 1:
        encrypt(text, shift)
    elif direction == 2:
        decrypt(text, shift)
    else:
        print(f"Your input {direction} was not one of the options. Enter a valid that is either '1' or '2'")

    wanna = int(input("If you want to continue type '1' and if you don't want to continue type '2'\n"))
    if wanna == 2:
            wanna_play = False