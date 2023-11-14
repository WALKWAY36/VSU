import Main
alphabet = Main.alphabet
p = 7
y = int(input("Enter open key y: "))
x = int(input("Enter private key: "))
encr = input("Enter encrypt word")
a_i, b_i = Main.bundle(encr)
print(a_i, b_i)
decr = ''
for i in range(len(a_i)):
    a_w = a_i[i]
    a_dec = Main.word_numb(a_w)
    m = a_dec[0] ** x % p
    m_bin = Main.dec_bin(m)
    b_w = b_i[i]
    b_dec = Main.word_numb(b_w)
    b_bin = Main.dec_bin(b_dec[0])
    decr_bin = m_bin ^ b_bin
    decr_dec = Main.bin_dec(str(decr_bin))
    decr += alphabet[decr_dec]



print(decr)
