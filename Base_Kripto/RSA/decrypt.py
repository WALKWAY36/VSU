import cv2
import numpy as np
import RSA

""" Enter open key"""
n = int(input("Enter n"))
e = int(input("Enter e"))
""" Enter private key"""
_d = int(input("Enter d"))

decr = True
while decr:
    inpt = input("Enter i if you want encrypting image "
                 "\n Enter w if you want encrypting text "
                 "\n Enter q if you want exit")
    """Encryption image"""
    if inpt == 'i':
        img = cv2.imread('encrypt.jpg',cv2.COLOR_BGR2GRAY)
        cv2.imwrite('decr.jpg', img)
        WIDTH = img.shape[1]
        HEIGHT = img.shape[0]
        C = [[0 for j in range(WIDTH)] for i in range(HEIGHT)]
        print(type(C))
        for i in range(HEIGHT):
            for j in range(WIDTH):
                C[i][j] = (img[i][j] ** _d) % n
        C = np.array(C, dtype=np.uint8)
        print("you decrypt: ", C)
        cv2.imshow('Decrypt_img', C)
        cv2.waitKey(0)
        filename = 'decrypt.jpg'
        cv2.imwrite(filename, C)
    """Decryption words"""
    if inpt == 'w':
        T = input("Enter encrypt word")
        alphabet = RSA.key
        Z = RSA.word_numb(T, alphabet)
        print(Z)
        """Generation matrix of simbols 8x8"""
        matrix = RSA.Generate_Symbol(alphabet)
        """Decryption"""
        """Filling symbols from T to q(array for helping) """
        """Array for filling decrypt number"""
        M = [0 for i in range(len(Z))]
        print(Z)
        """Filling decrypt number"""
        for i in range(len(Z)):
            M[i] = Z[i] ** _d % n
        print("you decrypt number : ", M)
        """Conversion from number to word"""
        decrypt = RSA.numb_word(M, alphabet)
        print('You decrypt word: ', decrypt)
        """writing to file"""
        f = open("decrypt.txt", "w")
        f.write("Open key is {} {} \n decrypt message is {}".format(n, e, decrypt))
        f.close()
    if inpt == 'q':
        decr = False
