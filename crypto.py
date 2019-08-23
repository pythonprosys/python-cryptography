from random import randint
print("Encrypt/Decrypt")
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;_-@!$%&/()=?#{}[]0123456789<>#'

def generate_otp(sheets, length):
        for sheet in range(sheets):
                with open("otp" + str(sheet) + ".txt","w") as f:
                        for i in range(length):
                                f.write(str(randint(0,86))+"\n")

def load_sheet(filename):
        with open(filename, "r") as f:
                contents = f.read().splitlines()
        return contents
def get_plaintext1():
        plaintext = input('Message ')
        p1 = plaintext
        return p1
def get_plaintext():
        plaintext = input('Filename ')
        file123 = open(plaintext)
        p1 = file123.read()
        return p1

def load_file(filename):
        with open(filename, "r") as f:
                contents = f.read()
        return contents

def save_file(filename, data):
        with open(filename, 'w') as f:
                f.write(data)

def encrypt(p1, sheet):
        ciphertext = ''
        for position, character in enumerate(p1):
                if character not in ALPHABET:
                        ciphertext += character
                else:
                        encrypted = (ALPHABET.index(character) + int(sheet[position])) % 86
                        ciphertext += ALPHABET[encrypted]
        return ciphertext
def encrypt1(p1, sheet):
        ciphertext = ''
        for position, character in enumerate(p1):
                if character not in ALPHABET:
                        ciphertext += character
                else:
                        encrypted = (ALPHABET.index(character) + int(sheet[position])) % 86
                        ciphertext += ALPHABET[encrypted]
        return ciphertext

def decrypt(ciphertext, sheet):
        plaintext = ''
        for position, character in enumerate(ciphertext):
                if character not in ALPHABET:
                        plaintext += character
                else:
                        decrypted = (ALPHABET.index(character) - int(sheet[position])) % 86
                        plaintext += ALPHABET[decrypted]
        return plaintext
def save_python(filename, decrypted_otp):
        python_file = open("saves/" + filename, "a")
        python_file.write(decrypted_otp)
        python_file.close()
def save_html(filename, decrypted_otp):
        html_file = open("saves/" + filename, "a")
        html_file.write(decrypted_otp)
        html_file.close()
def save_php(filename, decrypted_otp):
        html_file = open("saves/" + filename, "a")
        html_file.write(decrypted_otp)
        html_file.close()
def menu():
        choices = ['1', '2', '3', '4']
        choice = '0'
        while True:
                while choice not in choices:
                        print('What would you like to do?')
                        print('1. Generate one-time pads')
                        print('2. Encrypt a File')
                        print('3. Decrypt a File')
                        print('4. Encrypt a Message')
                        choice = input('Please type 1, 2, 3 or 4 and press Enter ')
                        if choice == '1':
                                sheets = int(input('How many one-time pads would you like to generate? '))
                                length = int(input('What will be your maximum message length? '))
                                generate_otp(sheets, length)
                        elif choice == '2':
                                filename = input('Type in the filename of the OTP you want to use ')
                                sheet = load_sheet(filename)
                                plaintext = get_plaintext()
                                ciphertext = encrypt(plaintext, sheet)
                                filename = input('What will be the name of the encrypted file? ')
                                save_file(filename, ciphertext)
                        elif choice == '3':
                                filename = input('Type in the filename of the OTP you want to use ')
                                sheet = load_sheet(filename)
                                filename = input('Type in the name of the file to be decrypted ')
                                ciphertext = load_file(filename)
                                plaintext = decrypt(ciphertext, sheet)
                                print('The message reads:')
                                print('')
                                print(plaintext)
                                save = input("Would you like to save the file? Y/N").lower()
                                if save == "y":
                                    file = open("./saves/" + filename, "w")
                                    file.write(plaintext)
                                    file.close()
                        elif choice == '4':
                                filename = input('Type in the filename of the OTP you want to use ')
                                sheet = load_sheet(filename)
                                plaintext = get_plaintext1()
                                ciphertext = encrypt1(plaintext, sheet)
                                filename = input('What will be the name of the encrypted file? ')
                                save_file(filename, ciphertext)
                        choice = '0'


menu()
