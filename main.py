from algorithm import *
from file_configuration import *
from freq_analysis import *

option_ans = "COMMAND LIST \n" \
                "Input '1' To Frequency Analysis \n" \
                "Input '2' To Kasiski \n" \
                "Input '3' To Encrypting \n" \
                "Input '4' To Decrypting \n\n" \
                "Your input ... "

option = input(option_ans)

if option.lower() == '3' or option.lower() == '4':
    source_type_ans = "CHOOSE THE SOURCE TYPE \n" \
                  "Input '1' To Input Manually \n" \
                  "Input '2' If Source From .txt \n\n" \
                  "Your input ... "
    source_type = input(source_type_ans)

    if option.lower() == '3':
        if source_type.lower() == '1':
            plaintext = input("Input Plaintext : ")
        elif source_type.lower() == '2':
            filename = input("Input File Name (.txt) Without Extension : ")
            plaintext = readTxtFile(filename)
        else:
            print("On Development Process")

        katakunci = input("Input Kata Kunci : ")
        ciphertext, exec_time = enkripsi(plaintext, katakunci)

        output_file_type_ans = "CHOOSE THE OUTPUT TYPE \n" \
                  "Input '1' To Output in Terminal \n" \
                  "Input '2' to Generate .txt File\n\n" \
                  "Your input ... "

        output_file_type = input(output_file_type_ans)

        if output_file_type.lower() == '1':
            print("Ciphertext : {}".format(ciphertext))
        elif output_file_type.lower() == '2':
            output_filename = input("Input Filename (.txt) Without Extension : ")
            writeTxtFile(ciphertext, output_filename)
        else:
            print("In Development Process")
        plaintext, exec_time = dekripsi(ciphertext, katakunci)
        res = char_bigram_trigram_and_freq(ciphertext)
        print(res)

    elif option.lower() == '4':
        if source_type.lower() == '1':
            ciphertext = input("Input Ciphertext : ")
        elif source_type.lower() == '2':
            filename = input("Input File Name (.txt) Without Extension : ")
            ciphertext = readTxtFile(filename)

        katakunci = input("Input Kata Kunci : ")
        plaintext, exec_time = dekripsi(ciphertext, katakunci)

        output_file_type_ans = "CHOOSE THE OUTPUT TYPE \n" \
                  "Input '1' To Output in Terminal \n" \
                  "Input '2' to Generate .txt File\n" \
                  "Your input ... "

        output_file_type = input(output_file_type_ans)

        if output_file_type.lower() == '1':
            print("Plaintext : {}".format(plaintext))
        elif output_file_type.lower() == '2':
            output_filename = input("Input Filename (.txt) Without Extension : ")
            writeTxtFile(plaintext, output_filename)
        else:
            print("In Development Process")