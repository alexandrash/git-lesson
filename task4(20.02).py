
def dec_to_bin(dec):
    bin = " "
    while dec != 0:
        bin += str(dec % 2)
        dec //= 2

    return bin[::-1]

dec = int(input('Введите число в десятичной системе. Оно будет переведено в двоичную систему: '))
print(dec_to_bin(dec))


def bin_to_dec(bin):
    dec = 0
    for i in range(len(bin)):
        dec += int((bin[len(bin)-1- i]) * (2 ** i))
    return dec

bin = str(input('Введите число в двоичной системе. Оно будет переведено в десятичную систему:'))
print(bin_to_dec(bin))





