from algorithm import enkripsi
from file_configuration import writeTxtFile

def kasiski(ciphertext):
  repeated_substr = get_repeated_substr(ciphertext.lower())
  substr_and_range, factors_list = get_range_between_repeated_substr(repeated_substr, ciphertext.lower())
  slice_list = get_slice_every_list(factors_list)
  return slice_list, substr_and_range


def get_repeated_substr(ciphertext):
  substring_and_frequency = {}
  block_size = 2
  stop_condition = False
  repeated_substr_list = []

  while stop_condition == False or block_size <= len(ciphertext)/2:
    stop_condition = True
    for index in range(len(ciphertext)-(block_size-1)):
      substring = ciphertext[index : index + block_size]
      if substring not in substring_and_frequency:
        substring_and_frequency[substring] =  1
      else:
        substring_and_frequency[substring] +=1
        if substring_and_frequency[substring] > 1 and substring not in repeated_substr_list:
          repeated_substr_list.append(substring)
          substring_of_substring = ""
          for char_index in range(len(substring) - 1):
            substring_of_substring += substring[char_index]
            if substring_of_substring in repeated_substr_list:
              repeated_substr_list.remove(substring_of_substring)
          substring_of_substring = ""
          for char_index in range(len(substring) - 1, 0, -1):
            substring_of_substring = substring[char_index] + substring_of_substring
            if substring_of_substring in repeated_substr_list:
              repeated_substr_list.remove(substring_of_substring)
        stop_condition = False
    block_size += 1
  return repeated_substr_list


def get_range_between_repeated_substr(repeated_substr, ciphertext):
  substr_and_range = {}
  factors_list = []
  for word in repeated_substr:
    substr_and_range[word] = {}
    found = False
    for index in range(len(ciphertext) - len(word) + 1):
      word_pointer = ciphertext[index: index + len(word)]
      if word_pointer == word and found == False:
        found = True
        counter = 0
      elif word_pointer != word and found == True:
        counter += 1
      elif word_pointer == word and found == True:
        counter += 1
        factors = get_factor_of_num(counter)
        substr_and_range[word][counter] = factors
        factors_list.append(factors)
        counter = 0

  return substr_and_range, factors_list

def get_factor_of_num(num):
  factor = []
  for index in range(1, num + 1):
    if num % index == 0:
      factor.append(index)

  return factor


def get_slice_of_all_factors(list_of_factors):
  slice_list = []
  for factor_index in range(len(list_of_factors)):
    factor = list_of_factors[factor_index]
    for num in factor:
      is_have_slice = True
      for index in range(0, len(list_of_factors)):
        if num not in list_of_factors[index]:
          is_have_slice = False
          break
      if is_have_slice and num not in slice_list:
        slice_list.append(num)

  return slice_list


def get_slice_every_list(list_of_factors):
  slice_list = []
  for factor in list_of_factors:
    factor_index = list_of_factors.index(factor)
    for num in factor:
      for index in range(factor_index + 1, len(list_of_factors)):
        if num in list_of_factors[index] and num not in slice_list:
          slice_list.append(num)
          break

  return slice_list

# TEST SCENARIO
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

case = 1
report_string = ""
for data in data_all:
    plaintext = data["plaintext"]
    katakunci = data["katakunci"]

    ciphertext = enkripsi(plaintext, katakunci)
    kasiski_result, substr_and_range = kasiski(ciphertext.lower())
    report_string += "\nCASE #{}".format(case)
    report_string += "\nPlaintext : {}".format(plaintext)
    report_string += "\nCiphertext : {}".format(ciphertext)
    report_string += "\nKata Kunci : {}".format(katakunci)
    report_string += "\nSubstring Berulang : {}".format(substr_and_range.keys())
    for substr in substr_and_range:
        report_string += "\nSubstring <{}>, Jarak --> {}".format(substr, list(substr_and_range[substr].keys()))
        for range_value in substr_and_range[substr].keys():
            report_string+= "\nJarak <{}>, Faktor Pembagi ---> {}".format(range_value, substr_and_range[substr][range_value])
        print()

    report_string += "\nPanjang Kata Kunci (Actual)         : {}".format(len(katakunci))
    report_string += "\nIrisan dari Faktor Pembagi : {}".format(kasiski_result)

    if len(katakunci) in kasiski_result:
        report_string += "\nHASIL TEST ---> FAILED ( Probability : {}% )".format(100/len(kasiski_result))
    else:
        report_string += "\nHASIL TEST ---> TEST SUCCESS"

    case += 1
    report_string += "\n"

writeTxtFile(report_string, "kasiski_result")