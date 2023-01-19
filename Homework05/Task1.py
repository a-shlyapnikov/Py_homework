# Напишите программу, удаляющую из
# текста все слова содержащие "абв".


def delete_abv(strng):
    strng = list(filter(lambda x: 'абв' not in x, strng.split()))
    return ' '.join(strng)

text = 'абв йойо йой Напишите программу, удаляющую из текста все слова содержащие "абв"'
print(text)
text = delete_abv(text)
print(text)