import time
from file_configuration import *

def convert_to_ascii(text):
    ascii_list = []

    for char in text:
        ascii_list.append(ord(char))

    return ascii_list


def get_block_size(katakunci_ascii):
    if len(str(katakunci_ascii[0])) > 1:
        block_size = len(str(katakunci_ascii[0]))
    else:
        block_size = len(str(katakunci_ascii[0])) + len(str(katakunci_ascii[1]))

    return block_size


def get_increment_num(katakunci_ascii):
    if len(str(katakunci_ascii[1])) > 1:
        increment_num = len(str(katakunci_ascii[1]))
    else:
        increment_num = len(str(katakunci_ascii[1])) + str(len(katakunci_ascii[2]))

    return increment_num


def get_key_ekspansion_len(plaintext, block_size):
    if len(plaintext) % block_size == 0:
        return len(plaintext)
    else:
        num_padded = block_size - (len(plaintext) % block_size)
        return len(plaintext) + num_padded


def text_and_katakunci_processing(text, katakunci):
    katakunci_ascii = convert_to_ascii(katakunci)
    block_size = get_block_size(katakunci_ascii)
    increment_num = get_increment_num(katakunci_ascii)
    key_ekpansion_len = get_key_ekspansion_len(text, block_size)
    text_ascii = convert_to_ascii(text)

    return text_ascii, katakunci_ascii, block_size, increment_num, key_ekpansion_len


def get_sub_key(katakunci_ascii, increment_num, block_size, key_ekspansion_len):
    k1 = []
    k2 = []
    katakunci_ascii_len = len(katakunci_ascii)
    k3 = katakunci_ascii_len

    block = []
    for index in range(key_ekspansion_len):
        k1.append(katakunci_ascii[index % katakunci_ascii_len] + (increment_num * index))
        block.append(katakunci_ascii[index % katakunci_ascii_len])
        if len(block) == block_size:
            for index in range(block_size):
                k2.insert(index, block[index])
            block = []

    return k1, k2, k3


def get_super_key(k1, k2, k3):
    super_key = []

    for index in range(len(k1)):
        super_key.append(k1[index] * k2[index] * k3)

    return super_key


def subtitute(text, super_key, mode):
    result = ""
    p = []
    if mode == 'encrypting':
        for index in range(len(text)):
            result_ascii = (text[index] + super_key[index]) % 128
            result_char = chr(result_ascii)
            result += result_char
    elif mode == 'decrypting':
        for index in range(len(text)):
            result_ascii = (text[index] - super_key[index]) % 128
            p.append(result_ascii)
            result_char = chr(result_ascii)
            result += result_char

    return result


def dekripsi(ciphertext, katakunci):

    ciphertext_ascii, katakunci_ascii, block_size, increment_num, key_ekspansion_len = text_and_katakunci_processing(ciphertext, katakunci)

    k1, k2, k3 = get_sub_key(katakunci_ascii, increment_num, block_size, key_ekspansion_len)
    super_key = get_super_key(k1, k2, k3)

    plaintext = subtitute(ciphertext_ascii, super_key, 'decrypting')

    return plaintext


def enkripsi(plaintext, katakunci):

    plaintext_ascii, katakunci_ascii, block_size, increment_num, key_ekspansion_len = text_and_katakunci_processing(plaintext, katakunci)

    k1, k2, k3 = get_sub_key(katakunci_ascii, increment_num, block_size, key_ekspansion_len)
    super_key = get_super_key(k1, k2, k3)

    ciphertext = subtitute(plaintext_ascii, super_key, 'encrypting')

    return ciphertext
