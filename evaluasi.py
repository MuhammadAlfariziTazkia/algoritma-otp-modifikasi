import xlsxwriter
from file_configuration import readTxtFile, writeTxtFile
import os
from algorithm import enkripsi, dekripsi
from kasiski import kasiski
from evaluasi_analisis_frekuensi import get_subtitution_freq_analysis

def similiarity_checker(text_a, text_b):
    length_a_and_b = [len(text_a), len(text_b)]
    length = min(length_a_and_b)

    num_diff_char = 0

    for index in range (length):
        if text_a[index] != text_b[index]:
            num_diff_char += 1

    num_same_char = length - num_diff_char
    similiarity = (num_same_char/length) * 100

    return num_diff_char, num_same_char, "{} %".format(round(similiarity, 2))


resource_evaluasi_dir = "resource_evaluasi"
plaintext_case_dir = os.path.join(resource_evaluasi_dir, "plaintext")
katakunci_case_dir = os.path.join(resource_evaluasi_dir, "katakunci")

filename_list = ["alphabetical.txt", "numerical.txt", "symbol.txt", "combination.txt"]

plaintext_list = []
katakunci_list = []

for filename in filename_list:
    plaintext_list.append(readTxtFile(os.path.join(plaintext_case_dir, filename)))
    katakunci_list.append(readTxtFile(os.path.join(katakunci_case_dir, filename)))

report_string = ""
case_no = 1

plaintext_input_record = []
plaintext_decrypt_res_record = []

ciphertext_record = []
katakunci_record = []

sync_evaluation_result_record = []
sync_evaluation_similiarity_record = []

kasiski_evaluation_record = []
katakunci_len_kasiski_record = []
katakunci_len_actual_record = []

freq_analysis_evaluation_record = []
subtitution_result_record = []

workbook = xlsxwriter.Workbook("report.xlsx")
general_worksheet = workbook.add_worksheet("general")
evaluasi_sync_worksheet = workbook.add_worksheet("evaluasi_sync")
evaluasi_analisis_frekuensi_worksheet = workbook.add_worksheet('evaluasi_freq_analysis')
evaluasi_kasiski_worksheet = workbook.add_worksheet("evaluasi_kasiski")

general_worksheet.write("A1", "Plaintext")
general_worksheet.write("B1", "Kata Kunci")
general_worksheet.write("C1", "Ciphertext")
general_worksheet.write("D1", "Pengujian Kesesuaian Algoritma")
general_worksheet.write("E1", "Pengujian Kasiski")
general_worksheet.write("F1", "Pengujian Analisis Frekuensi")

evaluasi_sync_worksheet.write("A1", "Plaintext (Input)")
evaluasi_sync_worksheet.write("B1", "Plaintext (Hasil Dekripsi)")
evaluasi_sync_worksheet.write("C1", "Plaintext (Input)")
evaluasi_sync_worksheet.write("D1", "Banyak Perbedaan Karakter")
evaluasi_sync_worksheet.write("E1", "Tingkat Kesesuaian")
evaluasi_sync_worksheet.write("F1", "Hasil")

evaluasi_analisis_frekuensi_worksheet.write("A1", "Plaintext")
evaluasi_analisis_frekuensi_worksheet.write("B1", "Ciphertext")
evaluasi_analisis_frekuensi_worksheet.write("C1", "Urutan Karakter Plaintext Berdasarkan Frekuensi")
evaluasi_analisis_frekuensi_worksheet.write("D1", "Urutan Karakter Ciphertext Berdasarkan Frekuensi")
evaluasi_analisis_frekuensi_worksheet.write("E1", "Percobaan Substitusi")
evaluasi_analisis_frekuensi_worksheet.write("F1", "Banyak Persamaan karakter")
evaluasi_analisis_frekuensi_worksheet.write("G1", "Banyak karakter Plaintext")
evaluasi_analisis_frekuensi_worksheet.write("H1", "Tingkat Kesesuaian")
evaluasi_analisis_frekuensi_worksheet.write("I1", "Hasil")

evaluasi_kasiski_worksheet.write("A1", "Ciphertext")
evaluasi_kasiski_worksheet.write("B1", "kata Kunci")
evaluasi_kasiski_worksheet.write("C1", "Panjang Kata Kunci (Kasiski)")
evaluasi_kasiski_worksheet.write("D1", "Panjang Kata Kunci (Actual)")
evaluasi_kasiski_worksheet.write("E1", "Hasil")

report_string_sync = ""
report_string_analisis_frekuensi = ""
report_string_kasiski = ""

row_no = 2
for plaintext_input in plaintext_list:
    for katakunci in katakunci_list:

        ciphertext = enkripsi(plaintext_input, katakunci)
        plaintext_result = dekripsi(ciphertext, katakunci)
        katakunci_len_kasiski, repeated_substr, substr_and_range = kasiski(ciphertext)
        banyak_perbedaan_karakter_aspek_kesesuaian, banyak_persamaan_karakter_aspek_kesesuaian, persentase_kesamaan_aspek_kesesuaian = similiarity_checker(plaintext_input, plaintext_result)

        substitusi_by_frekuensi_analisis, top_plaintext, top_ciphertext = get_subtitution_freq_analysis(plaintext_input, ciphertext)

        banyak_perbedaan_karakter_frekuensi_analisis, banyak_persamaan_karakter_frekuensi_analisis, persentase_kesamaan_frekuensi_analisis = similiarity_checker(plaintext_input, substitusi_by_frekuensi_analisis)

        general_worksheet.write("A{}".format(row_no), plaintext_input)
        general_worksheet.write("B{}".format(row_no), katakunci)
        general_worksheet.write("C{}".format(row_no), ciphertext)

        if banyak_perbedaan_karakter_aspek_kesesuaian == 0:
            general_worksheet.write("D{}".format(row_no), "SUCCESS")
            evaluasi_sync_worksheet.write("F{}".format(row_no), "SUCCESS")
        else:
            general_worksheet.write("D{}".format(row_no), "FAIL")
            evaluasi_sync_worksheet.write("F{}".format(row_no), "FAIL")

        if len(katakunci) in katakunci_len_kasiski:
            general_worksheet.write("E{}".format(row_no), "FAIL")
            evaluasi_kasiski_worksheet.write("E{}".format(row_no), "FAIL")
        else:
            general_worksheet.write("E{}".format(row_no), "SUCCESS")
            evaluasi_kasiski_worksheet.write("E{}".format(row_no), "SUCCESS")

        if banyak_perbedaan_karakter_frekuensi_analisis == len(plaintext_input):
            general_worksheet.write("F{}".format(row_no), "FAIL")
            evaluasi_analisis_frekuensi_worksheet.write("I{}".format(row_no), "FAIL")
        else:
            general_worksheet.write("F{}".format(row_no), "SUCCESS")
            evaluasi_analisis_frekuensi_worksheet.write("I{}".format(row_no), "SUCCESS")

        evaluasi_sync_worksheet.write("A{}".format(row_no), plaintext_input)
        evaluasi_sync_worksheet.write("B{}".format(row_no), plaintext_result)
        evaluasi_sync_worksheet.write("C{}".format(row_no), ciphertext)
        evaluasi_sync_worksheet.write("D{}".format(row_no), banyak_perbedaan_karakter_aspek_kesesuaian)
        evaluasi_sync_worksheet.write("E{}".format(row_no), persentase_kesamaan_aspek_kesesuaian)

        report_string_sync += "CASE {}\n".format(row_no-1)
        report_string_sync += "-------------------------  \n"
        report_string_sync += "PLAINTEXT (AWAL) ==> {}  \n".format(plaintext_input)
        report_string_sync += "PLAINTEXT (HASIL DEKRIPSI) ==> {}  \n".format(plaintext_result)
        report_string_sync += "KATA KUNCI ==> {}  \n".format(katakunci)
        report_string_sync += "CIPHERTEXT ==> {}  \n".format(ciphertext)
        report_string_sync += "BANYAK PERBEDAAN KARAKTER ==> {} dari {} Karakter  \n".format(banyak_perbedaan_karakter_aspek_kesesuaian, len(plaintext_input))
        report_string_sync += "TINGKAT PERSAMAAN ==> {}  \n".format(persentase_kesamaan_aspek_kesesuaian)
        report_string_sync += " \n\n\n"

        evaluasi_analisis_frekuensi_worksheet.write("A{}".format(row_no), plaintext_input)
        evaluasi_analisis_frekuensi_worksheet.write("B{}".format(row_no), ciphertext)
        evaluasi_analisis_frekuensi_worksheet.write("C{}".format(row_no), ",".join(top_plaintext))
        evaluasi_analisis_frekuensi_worksheet.write("D{}".format(row_no), ",".join(top_ciphertext))
        evaluasi_analisis_frekuensi_worksheet.write("E{}".format(row_no), substitusi_by_frekuensi_analisis)
        evaluasi_analisis_frekuensi_worksheet.write("F{}".format(row_no), banyak_persamaan_karakter_frekuensi_analisis)
        evaluasi_analisis_frekuensi_worksheet.write("G{}".format(row_no), len(plaintext_input))
        evaluasi_analisis_frekuensi_worksheet.write("H{}".format(row_no), persentase_kesamaan_frekuensi_analisis)

        report_string_analisis_frekuensi += "CASE {}\n".format(row_no - 1)
        report_string_analisis_frekuensi += "-------------------------  \n"
        report_string_analisis_frekuensi += "PLAINTEXT  ==> {}  \n".format(plaintext_input)
        report_string_analisis_frekuensi += "KATA KUNCI ==> {}  \n".format(katakunci)
        report_string_analisis_frekuensi += "CIPHERTEXT ==> {}  \n".format(ciphertext)
        report_string_analisis_frekuensi += "HASIL SUBSTITUSI ==> {}  \n".format(substitusi_by_frekuensi_analisis)
        report_string_analisis_frekuensi += "BANYAK PERSAMAAN KARAKTER ==> {} dari {} Karakter  \n".format(banyak_persamaan_karakter_frekuensi_analisis, len(plaintext_input))
        report_string_analisis_frekuensi += "TINGKAT PERSAMAAN ==> {}  \n".format(persentase_kesamaan_frekuensi_analisis)
        report_string_analisis_frekuensi += " \n\n\n"

        evaluasi_kasiski_worksheet.write("A{}".format(row_no), ciphertext)
        evaluasi_kasiski_worksheet.write("B{}".format(row_no), katakunci)
        evaluasi_kasiski_worksheet.write("C{}".format(row_no), str(katakunci_len_kasiski))
        evaluasi_kasiski_worksheet.write("D{}".format(row_no), len(katakunci))

        report_string_kasiski += "CASE {}\n".format(row_no - 1)
        report_string_kasiski += "-------------------------  \n"
        report_string_kasiski += "PLAINTEXT ==> {}  \n".format(plaintext_input)
        report_string_kasiski += "KATA KUNCI ==> {}  \n".format(katakunci)
        report_string_kasiski += "CIPHERTEXT ==> {}  \n".format(ciphertext)
        report_string_kasiski += "POTONGAN CIPHERTEXT BERULANG ==> {} \n".format(substr_and_range)
        report_string_kasiski += "IRISAN FAKTOR PEMBAGI ==> {}  \n".format(katakunci_len_kasiski)
        report_string_kasiski += "PANJANG KATA KUNCI ==> {}  \n".format(len(katakunci))
        report_string_kasiski += " \n\n\n"
        row_no += 1

workbook.close()

writeTxtFile(report_string_sync, "[RESULT] Evaluasi Kesesuaian.txt")
writeTxtFile(report_string_analisis_frekuensi, "[RESULT] Evaluasi Analisis Frekuensi.txt")
writeTxtFile(report_string_kasiski, "[RESULT] Evaluasi Kasiski.txt")