letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

print(' _______    ______    ____     _    _    ______    ____')
print('| ______|  |__  __|  |    \   | |  | |  | _____|  |    \\')
print('| |          |  |    | []  |  | |__| |  | |____   | []  |')
print('| |          |  |    | ___/   |  __  |  | _____|  | ___/')
print('| |_____    _|  |_   | |      | |  | |  | |____   | | \ \\')
print('|_______|  |______|  |_|      |_|  |_|  |______|  |_|  \_\\')
print('')
print('')
print('')



while True:

    option = ''
    message = ''

    decoded_message = ''
    coded_message = ''

    option_input = input('What to do (encode: , decode: , exit): ')
    if option_input == 'exit':
        break

    try:
        option_input_split = option_input.split(': ')
        option = option_input_split[0]
        message = option_input_split[1]
        code = int(input('Code (0 - 27): '))
    except:
        print('INVALID CHARACTER (only lowercase letters and spaces are allowed)')

    if option == 'encode':

        try: 

            for character in message:
                if (letters.index(character) + code) >= len(letters):
                    difference = len(letters) - letters.index(character)
                    coded_message += letters[code - difference]
                else:
                    coded_message += letters[(letters.index(character) + code)]

        except:
            print('INVALID CHARACTER (only lowercase letters and spaces are allowed)')

        print('')
        print(coded_message)
    
    elif option == 'decode':

        try:

            for character in message:
                if (letters.index(character) - code) < 0:
                    difference = letters.index(character)
                    decoded_message += letters[len(letters) - (code - difference)]
                else:
                    decoded_message += letters[(letters.index(character) - code)]

        except:
            print('')
            print('INVALID CHARACTER (only lowercase letters and spaces are allowed)')

        print(decoded_message)

    print('')
    print('')


