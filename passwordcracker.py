password = 'cokolwiek'
for i in range(3):
    x = input('Enter your guess: ')
    if x==password:
        print('Nice work! You have guessed the password!')
        break
else:
    print('You have run out of attempts.')
