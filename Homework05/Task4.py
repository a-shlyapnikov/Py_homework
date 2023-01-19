# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data = open('file_encode.txt', 'w')
data.write('AAAAAAABBBBBBBAAAAACCCCCBBBBBAAAAA')
data.close()

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string

data = open('file_encode.txt', 'r')
decoded_string = data.read()
file = open('file_decode.txt', 'w')
encoded_string = rle_encode(decoded_string)
file.write(encoded_string)
print(f'Строка {decoded_string}')
print(f'Сжатая строка {encoded_string}')
