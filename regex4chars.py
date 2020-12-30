import re
var_word = input("Podaj zdanie, w którym chcesz znaleźć przynajmniej czteroliterowe słowa: ")
pattern_var = re.compile(r"\b\w{4,}\b")
result_var = pattern_var.findall(var_word)
if result_var:
    print("Znalezione słowa to: ")
    for word in result_var:
        print(word, " ")
else:
    print("Brak pasujących słów.")
