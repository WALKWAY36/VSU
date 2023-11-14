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

# Расшифрование символов попарно
def playfair_decrypt(ciphertext, key):
    # Создаем матрицу для расшифрования
    matrix = create_playfair_matrix(key)

    # Расшифровываем символы попарно
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        # Находим координаты символов в матрице
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        row1, col1 = find_char(matrix, char1)
        row2, col2 = find_char(matrix, char2)

        # Расшифровываем символ
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

        if plaintext[-1] == 'x': plaintext = plaintext[:-1]
    return plaintext

key = input("Введите Кодовое слово")
plainText = input("Введите слово, которое хотите расшифровать")

print("Получен изначальное слово: ", playfair_decrypt(plainText, key))