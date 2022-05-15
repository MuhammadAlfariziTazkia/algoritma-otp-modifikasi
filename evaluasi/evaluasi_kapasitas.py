import os
from file_configuration import *
from algorithm import *
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str

def enkripsi_original_otp(plaintext, kunci):
    ciphertext = ""
    for index in range(len(plaintext)):
        ciphertext += chr((ord(plaintext[index]) + ord(kunci[index])) % 128)

    return ciphertext

def get_directory_size(path):
    total_size = 0
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        total_size += os.path.getsize(fp)

    return total_size


otp_asli_base_directory = 'evaluasi_kapasitas/otp_asli'
otp_asli_dictionary = {
    "10000" : {
        "plaintext": os.path.join(otp_asli_base_directory, "10000", "plaintext.txt"),
        "ciphertext": os.path.join(otp_asli_base_directory, "10000", "ciphertext.txt"),
        "kunci": os.path.join(otp_asli_base_directory, "10000", "kunci.txt")
    },
    "100000" : {
        "plaintext": os.path.join(otp_asli_base_directory, "100000", "plaintext.txt"),
        "ciphertext": os.path.join(otp_asli_base_directory, "100000", "ciphertext.txt"),
        "kunci": os.path.join(otp_asli_base_directory, "100000", "kunci.txt")
    },
    "1000000" : {
        "plaintext": os.path.join(otp_asli_base_directory, "1000000", "plaintext.txt"),
        "ciphertext": os.path.join(otp_asli_base_directory, "1000000", "ciphertext.txt"),
        "kunci": os.path.join(otp_asli_base_directory, "1000000", "kunci.txt")
    }
}

otp_modifikasi_base_directory = 'evaluasi_kapasitas/otp_modifikasi'
otp_modifikasi_dictionary = {
    "10000" : {
        "plaintext": os.path.join(otp_modifikasi_base_directory, "10000", "plaintext.txt"),
        "ciphertext": os.path.join(otp_modifikasi_base_directory, "10000", "ciphertext.txt"),
        "kunci": os.path.join(otp_modifikasi_base_directory, "10000", "kunci.txt")
    },
    "100000" : {
        "plaintext": os.path.join(otp_modifikasi_base_directory, "100000", "plaintext.txt"),
        "ciphertext": os.path.join(otp_modifikasi_base_directory, "100000", "ciphertext.txt"),
        "kunci": os.path.join(otp_modifikasi_base_directory, "100000", "kunci.txt")
    },
    "1000000" : {
        "plaintext": os.path.join(otp_modifikasi_base_directory, "1000000", "plaintext.txt"),
        "ciphertext": os.path.join(otp_modifikasi_base_directory, "1000000", "ciphertext.txt"),
        "kunci": os.path.join(otp_modifikasi_base_directory, "1000000", "kunci.txt")
    }
}

case_list = ['10000', '100000', '1000000']

for case in case_list:
    plaintext_asli_content = readTxtFile(otp_asli_dictionary[case]["plaintext"])
    plaintext_modifikasi_content  = readTxtFile(otp_modifikasi_dictionary[case]["plaintext"])

    kunci_asli = get_random_string(len(plaintext_asli_content))
    katakunci = "modifikasi otp"

    ciphertext_asli_content = enkripsi_original_otp(plaintext_asli_content, kunci_asli)
    ciphertext_modifikasi_content = enkripsi(plaintext_modifikasi_content, katakunci)

    writeTxtFile(kunci_asli, otp_asli_dictionary[case]["kunci"])
    writeTxtFile(ciphertext_asli_content, otp_asli_dictionary[case]["ciphertext"])

    writeTxtFile(katakunci, otp_modifikasi_dictionary[case]["kunci"])
    writeTxtFile(ciphertext_modifikasi_content, otp_asli_dictionary[case]["ciphertext"])

report_string = ""
for case in case_list:
    otp_asli_case = os.path.join(otp_asli_base_directory, case)
    otp_modifikasi_case = os.path.join(otp_modifikasi_base_directory, case)

    otp_asli_case_size = get_directory_size(otp_asli_case)
    otp_modifikasi_case_size = get_directory_size(otp_modifikasi_case)

    eficiency_in_byte = otp_asli_case_size - otp_modifikasi_case_size
    eficiency_in_percent = round((eficiency_in_byte / otp_asli_case_size) * 100, 2)

    report_string += "\n*** CASE {} KARAKTER ***".format(case)
    report_string += "\nOTP ORIGINAL : {} B".format(otp_asli_case_size)
    report_string += "\nOTP MODIFIKASI : {} B".format(otp_modifikasi_case_size)
    report_string += "\n"
    report_string += "\n--- EFICIENCY RESULT ---"
    report_string += "\nEficiency (Bytes) : {} B".format(eficiency_in_byte)
    report_string += "\nEficiency (Kilo Bytes) : {} KB".format(round(eficiency_in_byte / 1000, 2))
    report_string += "\nEficiency (Mega Bytes) : {} MB".format(round(eficiency_in_byte / 1000000, 2))
    report_string += "\nEficiency (Percent) : {} %".format(eficiency_in_percent)
    report_string += "\n"
    report_string += "\n"

writeTxtFile(report_string, "capacity_result.txt")