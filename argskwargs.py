def test_fun(number, *multiples):
    print("Liczba: ", number)
    for n in multiples:
        print("Wielokrotność: ", n)


test_fun(2, 4, 6, 8)


def test_fun2(number, **multiples):
    print("Liczba: ", number)
    for key, value in multiples.items():
        print(f"Wielokrotność {key}: {value}")


test_fun2(2, pierwsza=4, druga=6, trzecia=8)


def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


person_print("robert", "skrzypczak", "Kraków", "Uniwersytet Pedagogiczny", age=22)
