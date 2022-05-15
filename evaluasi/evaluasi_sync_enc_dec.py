from algorithm import enkripsi, dekripsi
from file_configuration import writeTxtFile

plaintext_list = [
        "kajsdnkajbdkasdbasjkbdasjdhjvVHJGVHJGVHJGVHGVHJGVHJGVhjgvhgJGVHJVGHJGVHJgvhgvhjgvhjgvhgv",
        "8923749872348972349827349827429817293719617253671236178236",
        "(*&(*&&*^^&*^&^&*^(*&^&*^^&%^$^%$%$%$^%$^%$%^$^%$^%$%$&>:><?<>?<?><?}{}}{}}:<?:<>*&^*(^*&^*&^*&^%$^%$%&$&^$",
        "ajshdkjladhsjkashJKHJKHKJHKJH89798798798(*&(&*(&(JBHJKBJBkjbjkbjkasbdhjg()*&*&(*&9789jshakjhdkjsbgkjbdf2309420394)(*j&^jhjhjvjhgvh"
]

katakunci_list = [
        "bhasjkdhJKHJKHkj",
        "9879889789798786",
        "^&*(^*&^*&^*&^&*",
        "ajsh*(&78yhsdu&_"
]

string_report = ""
case_no = 1
for plaintext_input in plaintext_list:
    for katakunci in katakunci_list:
        ciphertext = enkripsi(plaintext_input, katakunci)
        plaintext_res = dekripsi(ciphertext, katakunci)
        string_report += "CASE {}\n".format(case_no)
        case_no += 1
        string_report += "----------------\n"
        string_report += "Plaintext (User Input)     : {}\n".format(plaintext_input)
        string_report += "Plaintext (Decrypt Result) : {}\n".format(plaintext_res)

        num_miss_char = 0
        total_char = len(plaintext_input)

        for index in range(total_char):
            if plaintext_input[index] != plaintext_res[index]:
                num_miss_char += 1

        string_report += "Banyak perbedaan karakter = {} dari {}\n".format(num_miss_char, total_char)
        string_report += "TINGKAT KESESUAIAN    : {}%\n\n\n".format(((total_char-num_miss_char)/total_char)*100)

writeTxtFile(string_report, "sync_enc_dec_result.txt")