try:
    with open('plik1.txt', 'r') as txt_file1:
        with open('plik2.txt', 'w') as txt_file2:
            for line in txt_file1.readlines():
                txt_file2.writelines(line)
except IOError as e:
    print(e)
finally:
    if txt_file2:
        txt_file2.close()
    if txt_file1:
        txt_file1.close()