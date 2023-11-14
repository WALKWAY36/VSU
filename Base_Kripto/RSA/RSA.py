import string

key = "".join(dict.fromkeys(string.ascii_lowercase + string.digits + string.punctuation))
"""Check then number is simple"""


def check_simple(number):
    s = 0
    for i in range(2, 10):
        if number % i == 0 and number != i:
            s += 1
    if s != 0:
        print(f"{number} not simple number!!!")
    return number, s


"""Method sieve of Eratosthenes"""


def simple_number(n):
    a = [i for i in range(2, n + 1)]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] != 0 and a[j] % a[i] == 0:
                a[j] = 0
    a = [i for i in a if i != 0]
    return a


def division_to_simple(number, dividers):
    for i in range(2, 10):
        if number % i == 0 and number != i:
            if number % i == 0:
                number = number / i
                dividers += str(i)
            return division_to_simple(number, dividers)
    return int(number), dividers


def Generate_Symbol(key):
    matrix = [[0] * 8 for i in range(8)]
    for i in range(8):
        for j in range(8):
            matrix[i][j] = key[i * 8 + j]
        print(matrix[i])
    return matrix


def numb_word(number, key):
    word = ''
    for i in number:
        word += key[i]
    return word


def word_numb(word, key):
    number = list()
    for i in word:
        for j in range(len(key)):
            if i == key[j]:
                number.append(j)

    return number


def help_d(e, phi_n):
    d_help = []
    for i in range(10000):
        d = (i * e) % phi_n
        if d == 1:
            d_help.append(i)
    return d_help


if __name__ == '__main__':
    print("""RSA-algoripthm""")
