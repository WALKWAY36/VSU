import string

# Создание матрицы для шифрования и расшифровки
def create_playfair_matrix(key):
    # Удаляем повторяющиеся символы из ключа и объединяем с алфавитом
    key = "".join(dict.fromkeys(key + string.ascii_lowercase.replace("j", "")))

    # Создаем матрицу 5х5, заполненную символами из ключа и алфавита
    matrix = [[0] * 5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            matrix[i][j] = key[i * 5 + j]

    return matrix

# Находим координаты символа в матрице
def find_char(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)

# Шифрование символов попарно
def playfair_encrypt(plaintext, key):
    # Создаем матрицу для шифрования
    matrix = create_playfair_matrix(key)


    # Добавляем "x" для нечетной длины сообщения
    if len(plaintext) % 2 == 1:
        plaintext += "x"

    # Шифруем символы попарно
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        # Находим координаты символов в матрице
        char1 = plaintext[i]
        char2 = plaintext[i + 1]
        row1, col1 = find_char(matrix, char1)
        row2, col2 = find_char(matrix, char2)

        # Шифруем символы по правилам шифра Плейфера
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext

key = input("Введите Кодовое слово")
plainText = input("Введите слово, которое хотите зашифровать")

print(playfair_encrypt(plainText, key))