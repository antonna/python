# Prime Number Calculation

while True:
    num = input('Number (or "q" to exit): ')

    if num == "q":
        break

    num = int(num)
    prime = True
    for i in range(2, num // 2 + 1):
        if num % i:
            continue
        else:
            prime = False
            break

    if prime:
        print('The number', num, 'is prime.')
    else:
        print('The number', num, 'is NOT prime.')

print('Program terminated.')