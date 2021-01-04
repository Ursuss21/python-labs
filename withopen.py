txt_file1 = None
txt_file2 = None
try:
    with open('plik2.txt', 'r') as txt_file1:
        with open('plik2.txt', 'w') as txt_file2:
            for line in txt_file1.readlines():
                txt_file2.writelines(line)
except (IOError, FileNotFoundError) as e:
    print("Zły plik lub ścieżka do pliku do odczytu")
finally:
    if txt_file1:
        txt_file1.close()
        txt_file2.close()