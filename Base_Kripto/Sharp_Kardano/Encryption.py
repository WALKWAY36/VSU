sharp = [[ 1,  2,  3,  4,  5,  6],
         [ 7,  8,  9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18],
         [19, 20, 21, 22, 23, 24],
         [25, 26, 27, 28, 29, 30],
         [31, 32, 33, 34, 35, 36]]
encr = ''
def Encryption(m,key):
    i = 0
    j = 0
    k = 0
    while i < 6:
        while j < 6:
            if k < 9 and sharp[i][j] == key[k]:
                sharp[i][j] = inpt[m]
                sharp[i + (j - i)][-i - 1] = inpt[m + 9]
                sharp[-1 - i][-1 - j] = inpt[m + 18]
                sharp[-1 - i - (j - i)][i] = inpt[m + 27]
                i = i - i - 1
                j = j - j - 1
                k += 1
                m += 1
                break
            j += 1
        else: j = 0
        i += 1
    else: i = 0
inpt = input("Введите слово,имеющую длину - 36 символов")
print("Изначальное сообщение:\n", inpt)
key0 = [6, 25, 18, 32, 29, 9, 13, 23, 21]
Encryption(0, key0)
print("Зашифрованное предложение")
for i in range(6):
    for j in range(6):
        encr += sharp[i][j]
        print(sharp[i][j], end=' ')
    print()
print(encr)