sharp =[[ 1,  2,  3,  4,  5,  6],
        [ 7,  8,  9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36]]
def Decryption(m,key):
    decr0 = ''
    decr1 = ''
    decr2 = ''
    decr3 = ''
    i = 0
    j = 0
    k = 0
    while i < 6:
        while j < 6:
            if k < 9 and sharp[i][j] == key[k]:
                decr0 += encr[sharp[i][j] - 1]
                decr1 += encr[sharp[i + (j - i)][-i - 1] - 1]
                decr2 += encr[sharp[-1 - i][-1 - j] - 1]
                decr3 += encr[sharp[-1 - i - (j - i)][i] - 1]
                i = i - i - 1
                j = j - j - 1
                k += 1
                m += 1
                break
            j += 1
        else:
            j = 0
        i += 1
    else:
        i = 0
    decr = decr0 + decr1 + decr2 + decr3
    return decr
encr = input("Введите зашифрованное слово,имеющую длину - 36 символов")
print("зашифрованное сообщение:\n", encr)
key0 = [6, 25, 18, 32, 29, 9, 13, 23, 21]
decr = Decryption(0, key0)
print("расшифрованное сообщение:\n", decr)
