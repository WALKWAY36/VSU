import cv2
import numpy as np
import RSA

print(RSA.simple_number(34))
p = int(input("Enter any simple number p \n Input>"))
q = int(input("Enter any simple number q \n Input>"))

RSA.check_simple(p)
RSA.check_simple(q)

"""Calculation comparison module"""
n = p * q
if n > 68:
    assert print("Error!!!\n Please input n <=68")
"""Calculation PHI(n)"""
phi_n = (p - 1) * (q - 1)

phi_n, s = RSA.check_simple(phi_n)

dividers_phi = ""
phi = 0
if s != 0:
    phi, dividers_phi = RSA.division_to_simple(phi_n, dividers_phi)
    print(phi, dividers_phi)

"""Choise e"""
print("Enter number e less than comparison module \n and number can't common factors ")

e = int(input('Input> '))
dividers_e = ""
_e, dividers_e = RSA.division_to_simple(e, dividers_e)
"""Helping for find d"""
d_help = RSA.help_d(e, phi_n)
while True:
    print(f"Enter number d which division to simple\nfor example \n {d_help} ")
    _d = int(input("Input> "))
    compar = (_d * e) % phi_n
    if compar == 1:
        break
print("Open key is {} {}".format(n, e))

encrypt = True
while encrypt:
    inpt = input("Enter i if you want encrypting image "
                 "\n Enter w if you want encrypting text "
                 "\n Enter q if you want exit "
                 "\n Input> ")
    """Encryption image"""
    if inpt == 'i':
        name = '1.png'
        img = cv2.imread(name, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('grayscale' + name, img)
        WIDTH = img.shape[1]
        HEIGHT = img.shape[0]
        C = [[0 for j in range(WIDTH)] for i in range(HEIGHT)]
        for i in range(HEIGHT):
            for j in range(WIDTH):
                C[i][j] = (img[i][j] ** e) % n
        C = np.array(C, dtype=np.uint8)
        print("you encrypt: ", C)
        cv2.imshow('Encrypt_img', C)
        cv2.waitKey(0)
        filename = 'encrypt.jpg'
        cv2.imwrite(filename, C)
        f = open('encrypt.txt', 'w')
        f.write("Open key is n: {}  e: {}\n private key is d: {} \n encrypt image is: encrypt.jpg ".format(n, e, _d))
        f.close()
    """Encryption words"""
    if inpt == 'w':
        alphabet = RSA.key
        """Generation matrix of simbols 8x8"""
        matrix = RSA.Generate_Symbol(alphabet)
        text = input("Please enter text which you want encrypting")
        """Fiiling symbols from text in var m"""
        m = RSA.word_numb(text, alphabet)
        print("You entered: ", m)
        """Filling C by zero
        C = m ^e mod n
        """
        C = [0 for i in range(len(m))]
        for i in range(len(m)):
            C[i] = (m[i] ** e) % n
        print("Encrypt numb: ", C)
        """Conversion from number to word """
        T = RSA.numb_word(C, alphabet)
        print("encrypt word is: ", T)
        f = open("encrypt.txt", "w")
        f.write("Open key is n: {}  e: {}\nprivate key is d: {} \nencrypt message is: {}".format(n, e, _d, T))
        f.close()
    if inpt == 'q':
        encrypt = False
