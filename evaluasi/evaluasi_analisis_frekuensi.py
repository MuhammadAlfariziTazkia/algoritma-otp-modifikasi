from algorithm import enkripsi
from file_configuration import writeTxtFile

def get_character_and_frequency(text):
    character_and_frequency = {}

    for char in text:
        if char not in character_and_frequency:
            character_and_frequency[char] = 1
        else:
            character_and_frequency[char] += 1
    character_and_frequency = dict(sorted(character_and_frequency.items(), key=lambda x: x[1], reverse=True))
    return character_and_frequency

data_all = [
    {
        "plaintext" : "Topik penelitian ini adalah Modifikasi Algoritma Kriptografi Klasik One Time Pad Dengan Kombinasi Metode Substitusi, Transposisi, dan Ekspansi.",
        "katakunci" : "modifikasi kriptografi otp"
    },
    {
        "plaintext" : "Nama saya Muhammad Alfarizi Tazkia, saya merupakan mahasiswa teknik informatika di Institut Teknologi Sumatera. Saat ini saya sedang berada di semester 8. Untuk semester ini, saya hanya mengambil mata kuliah Tugas Akhir 1 dan Tugas Akhir 2. Semoga saya lulus tepat waktu.",
        "katakunci" : "mahasiswa itera"
    },
    {
        "plaintext" : "Saat ini kita sedang memasuki keadaan perang dingin dengan kerajaan tetangga, harap kirim mata - mata terbaik kita untuk melihat kekuatan militer dan teknologi yang ada pada kerajaan tersebut, dan kumpulkan prajurit terkuat kita. Kita akan menyerang kerajaan tersebut besok malam",
        "katakunci" : "invansi militer"
    }
]

for data in data_all:
    data["ciphertext"] = enkripsi(data["plaintext"], data["katakunci"])
    top_ciphertext_char = list((get_character_and_frequency(data["ciphertext"].lower())).keys())
    top_plaintext_char = list((get_character_and_frequency(data["plaintext"].lower())).keys())
    data["percobaan"] = data["ciphertext"]

    for index in range(10):
        data["percobaan"] = data["percobaan"].replace(top_ciphertext_char[index], top_plaintext_char[index])

report_string = ""
for data in data_all:
    for attr in data:
        report_string += "\n{} : {}".format(attr.upper(), data[attr])
    report_string += "\n"

writeTxtFile(report_string, "analisis_frekuensi_result")

