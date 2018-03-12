# Found at GitHub repository alikellaway/String-Encryption

# Assign the alphabet numbers
# Transfer the message into the numbers
# Create a random sequence of numbers of the same length as the message (aka a key)
# Add the values of the key's numbers to the messages' numbers and then transfer each new number into
# its original letter on the scale

import random

def number_to_letter_retranslation(output_list, input_list_of_numbers, data_1, data_2, data_3, data_4):
    for list_values in input_list_of_numbers:
        if 1 <= int(list_values) <= 26:
            for keys in data_1:
                if data_1[keys] == list_values:
                    output_list.append(keys)
        if 27 <= int(list_values) <= 52:
            for keys in data_2:
                if alphabet_upper[keys] == list_values:
                    output_list.append(keys)
        if 53 <= int(list_values) <= 62:
            for keys in data_3:
                if data_3[keys] == list_values:
                    output_list.append(keys)
        if 63 <= int(list_values) <= 94:
            for keys in data_4:
                if data_4[keys] == list_values:
                    output_list.append(keys)


def letter_to_number_translation(string, data1, data2, data3, data4):
    string_number_storage = []
    for i in string:
        for keys in data1:
            if i == keys:
                string_number_storage.append(data1[keys])
        for keys in data2:
            if i == keys:
                string_number_storage.append(data2[keys])
        for keys in data3:
            if i == keys:
                string_number_storage.append(data3[keys])
        for keys in data4:
            if i == keys:
                string_number_storage.append(data4[keys])
    return string_number_storage


def encrypt(data_1, data_2, data_3, data_4, write_file_yn):
    message = input('Type your message:\n\t')
    storage_list_for_addition_values = []
    storage_list_for_chars_value = []
    # reading message and generating accompanying letter sequence
    for i in message:
                try:
                        storage_list_for_chars_value.append(data_1[i])
                        number_value = int(data_1[i])
                        max_number = 94 - number_value
                        storage_list_for_addition_values.append(random.randint(1, max_number))
                except Exception:
                        try:
                                storage_list_for_chars_value.append(data_2[i])
                                number_value = int(data_2[i])
                                max_number = 94 - number_value
                                storage_list_for_addition_values.append(random.randint(1, max_number))
                        except Exception:
                                try:
                                        storage_list_for_chars_value.append(data_3[i])
                                        number_value = int(data_3[i])
                                        max_number = 94 - number_value
                                        storage_list_for_addition_values.append(random.randint(1, max_number))
                                except Exception:
                                        try:
                                                storage_list_for_chars_value.append(data_4[i])
                                                number_value = int(data_4[i])
                                                max_number = 94 - number_value
                                                storage_list_for_addition_values.append(random.randint(1, max_number))
                                        except Exception:
                                                print('Error! Character value in password was not found'
                                                      ' in any libraries:\n\t' + str(i))
                                                if str(i) == '\\':
                                                    print('(Backslashes are unavailable)')
                                                    quit()
    # adding the two values of message and generated sequence
    ciphered_value_storage = []
    index = -1
    for i in storage_list_for_chars_value:
        index += 1
        ciphered_value = storage_list_for_chars_value[index] + storage_list_for_addition_values[index]
        ciphered_value_storage.append(ciphered_value)
    # finding the corresponding added number
    message_storage = []
    number_to_letter_retranslation(message_storage, ciphered_value_storage, alphabet, alphabet_upper, numbers, symbols)
    # translating the generated sequence into chars
    sequence_storage = []
    number_to_letter_retranslation(sequence_storage, storage_list_for_addition_values, alphabet,
                                   alphabet_upper, numbers, symbols)
    final_message = "".join(map(str, message_storage))
    final_sequence = "".join(map(str, sequence_storage))
    print(final_sequence)
    if write_file_yn =="y" or write_file_yn =='Y':
        f = open("message.txt","w+")
        f.write(final_message)
    return final_sequence, final_message


def decrypt(data1, data2, data3, data4, read_from_file_yn):
    if read_from_file_yn == 'y' or read_from_file_yn == 'Y':
        f = open('message.txt','r')
        message_for_decryption = f.read()
    if read_from_file_yn == 'n' or read_from_file_yn == 'N':
        message_for_decryption = input('Input the message: ')
    sequence = input('Input the sequence: ')
    if len(sequence) != len(message_for_decryption):
        print("Incorrect sequence length. You will not obtain the full message even if the sequence"
              " is correct up to the end of itself.")
        end_presentation = 'Incompletely deciphered message:'
    else:
        end_presentation= 'Completely deciphered message:'
    try:
        sequence_numbers = letter_to_number_translation(sequence, data1, data2, data3, data4)
        message_numbers = letter_to_number_translation(message_for_decryption, data1, data2, data3, data4)
        original_message_numbers = []
        original_message_list = []
        length = len(sequence_numbers)
        variable_index = 0
        while length > 0:
            number_value_of_original_message = message_numbers[variable_index]-sequence_numbers[variable_index]
            original_message_numbers.append(number_value_of_original_message)
            variable_index += 1
            length -= 1
        number_to_letter_retranslation(original_message_list, original_message_numbers, data1, data2, data3, data4)
        original_message = "".join(map(str, original_message_list))
        print(end_presentation+ '\n\t',original_message)
    except Exception:
        'Something went wrong! Your sequence was not correct or there may have been a value' \
        ' we could not find in our library.'


def lost_sequence():
    original = input('Input original message:\n\t')
    ciphered = input('Input ciphered message:\n\t')
    original_numbers = letter_to_number_translation(original, alphabet, alphabet_upper, numbers, symbols)
    ciphered_numbers = letter_to_number_translation(ciphered, alphabet, alphabet_upper, numbers, symbols)
    sequence_number_storage = []
    for i in original_numbers:
        index = original_numbers.index(i)
        total_number = ciphered_numbers[index]-i
        sequence_number_storage.append(total_number)
    sequence_letter_storage = []
    number_to_letter_retranslation(sequence_letter_storage, sequence_number_storage, alphabet,
                                   alphabet_upper, numbers, symbols)
    print(original_numbers)
    print(ciphered_numbers)
    final_sequence = "".join(map(str, sequence_letter_storage))
    print(final_sequence)
    return final_sequence

alphabet = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
            "i": 9,
            "j": 10,
            "k": 11,
            "l": 12,
            "m": 13,
            "n": 14,
            "o": 15,
            "p": 16,
            "q": 17,
            "r": 18,
            "s": 19,
            "t": 20,
            "u": 21,
            "v": 22,
            "w": 23,
            "x": 24,
            "y": 25,
            "z": 26
        }
alphabet_upper = {
            "A": 27,
            "B": 28,
            "C": 29,
            "D": 30,
            "E": 31,
            "F": 32,
            "G": 33,
            "H": 34,
            "I": 35,
            "J": 36,
            "K": 37,
            "L": 38,
            "M": 39,
            "N": 40,
            "O": 41,
            "P": 42,
            "Q": 43,
            "R": 44,
            "S": 45,
            "T": 46,
            "U": 47,
            "V": 48,
            "W": 49,
            "X": 50,
            "Y": 51,
            "Z": 52,
        }
numbers = {
            "0": 53,
            "1": 54,
            "2": 55,
            "3": 56,
            "4": 57,
            "5": 58,
            "6": 59,
            "7": 60,
            "8": 61,
            "9": 62
         }
symbols = {
            "!": 63,
            "@": 64,
            "£": 65,
            "$": 66,
            "%": 67,
            "^": 68,
            "&": 69,
            "*": 70,
            "(": 71,
            ")": 72,
            "€": 73,
            "#": 74,
            "_": 75,
            "-": 76,
            "=": 77,
            "+": 78,
            "{": 79,
            "}": 80,
            "[": 81,
            "]": 82,
            "/": 83,
            ":": 84,
            ";": 85,
            "'": 86,
            "`": 87,
            "~": 88,
            " ": 89,
            ".": 90,
            "?": 91,
            ",": 92,
            ">": 93,
            "<": 94
         }




encrypt(alphabet, alphabet_upper, numbers, symbols, 'y')

#decrypt(alphabet, alphabet_upper, numbers, symbols, 'N')

#lost_sequence()
