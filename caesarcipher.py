symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main_menu():
    encrypt_decrypt = input("Do you want to (e)ncrypt or (d)ecrypt? > ").lower()
    if encrypt_decrypt.startswith('e'):
        get_key('e')
    elif encrypt_decrypt.startswith('d'):
        get_key('d')
    else:
        print("Invalid selection")
        main_menu()


def get_key(operation):
    key = input("Please enter the key (0-25) to use. > ")
    if int(key) > 25 or int(key) < 0 or key.isnumeric() == False or key == '':
        print("Invalid key selection")
        get_key(operation)
    if operation == 'e':
        encrypt(key)
    elif operation == 'd':
        decrypt(key)


def encrypt(key):
    message = input("Please enter the message to encrypt. > ")
    if message == "":
        print("Invalid input. Please enter a valid string of characters.")
        encrypt(key)
    else:
        message_upper = message.upper()
        result_buffer = []
        for char in message_upper:
            if ord(char) == 32 or ord(char) in range(0, 64) or ord(char) in range(91, 96) or ord(char) in range(123,
                                                                                                                127):
                result_buffer.append(char)
            else:
                char_before = ord(char)
                char_after = char_before + key
                result_buffer.append(chr(char_after))


def decrypt(key):
    message = input("Please enter the message to decrypt. > ")
    if message == "":
        print("Invalid input. Please enter a valid string of characters.")
        decrypt(key)
    else:
        pass