txt_file = open("plik.txt", "r+")
txt_file.writelines([str(number)+'\n' for number in (1, 200)])
print(txt_file.read())
