import string

alphabet = key = "".join(dict.fromkeys(string.ascii_lowercase + string.digits + string.punctuation))


def dec_bin(n):
    bin = ''
    while n > 0:
        bin = str(n % 2) + bin
        n //= 2
    return int(bin)


def bin_dec(n):
    d = len(n)
    dec = 0
    for i in range(0, d):
        dec += int(n[i]) * (2 ** (d - i - 1))
    return dec


def word_numb(word):
    key = "".join(dict.fromkeys(string.ascii_lowercase + string.digits + string.punctuation))
    number = list()
    for i in word:
        for j in range(len(key)):
            if i == key[j]:
                number.append(j)
    return number


def gluing(a_i, b_i):
    code = ''
    for i in range(len(a_i)):
        code += a_i[i] + b_i[i]
    return code


def bundle(str):
    a_i = []
    b_i = []
    for i in range(0, len(str), 2):
        a_i.append(str[i])
        b_i.append(str[i + 1])
    return a_i, b_i


if __name__ == '__main__':
    print("""El_Gamal-algoripthm""")
