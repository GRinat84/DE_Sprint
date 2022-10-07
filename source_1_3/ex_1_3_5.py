def run(first, second):
    print(dec_10_to_2(dec_2_to_10(first) * dec_2_to_10(second)))
    

def dec_2_to_10(dec_2):
    dec_10 = 0

    for i in range (1, len(dec_2) + 1):
        dec_10 += int(dec_2[i - 1]) * (2**(i - 1))

    return dec_10


def dec_10_to_2(dec_10):
    dec_2 = ''

    while dec_10 > 0:

        div_int = dec_10 // 2;
        div_float = dec_10 % 2;

        dec_2 = str(div_float) + dec_2

        dec_10 = div_int


    return dec_2