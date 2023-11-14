import Main

"""I choose the primitive root g=5 to mod7"""
primitive = {1: 5, 2: 4, 3: 6, 4: 2, 5: 3, 6: 1}
p = 7
g = 5

alphabet = Main.alphabet
x = int(input("Enter private key x: "))
y = g ** x % p
print("Open key is: {}".format(y))
text = input("Enter word>")
a_i = []
b_i = []
for i in range(len(text)):
    k = int(input("Enter session key k{}: ".format(i)))
    numb = Main.word_numb(text[i])
    numb_ = Main.dec_bin(numb[0])

    a = g ** k % p
    a_w = alphabet[a]
    print("a{} is: {}".format(i, a))

    M = y ** k % p

    b_bin = Main.dec_bin(M) ^ numb_
    b_dec = Main.bin_dec(str(b_bin))
    b_w = alphabet[b_dec]
    print("b{} is: {}".format(i, b_bin))

    a_i.append(a_w)
    b_i.append(b_w)

encr = Main.gluing(a_i, b_i)
f = open('encrypt.txt', 'w')
f.write("Open key is y: {} p: {}  \nprivate key is x: {} \nencrypt word is: {} ".format(y, p, x, encr))
f.close()
