import re

var_name = input ("Podaj nazwę: ")
pattern_var = re.compile(r"^[a-z_A-Z][a-z_A-Z0-9]*$")
result_var = pattern_var.search(var_name)
if result_var:
    result_word = result_var.group()
    if re.match(r"[A-Z][a-z0-9]+$", result_word):
        print("Wpisane przez Ciebie {} może być nazwą klasy".format(result_word))
    if re.match(r"^[A-Z]+(?:_[A-Z]+)*$", result_word):
        print("Wpisane przez Ciebie {} może być nazwą stałej".format(result_word))
    if re.match(r"_+$", result_word):
        print("Niby może, ale nawet nie próbuj!")
    else:
        print("Wpisane przez Ciebie {} może być nazwą zmiennej lub funkcji.".format(result_word))
else:
    print("Podana prezz Ciebie {} nie może być nazwą zmiennej".format(var_name))