# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2])
# для всех значений предикат.
def check_statement(x, y, z):
    if not (x or y or z) == (not x and not y and not z):
        return True
    else:
        return False


if (check_statement(0, 0, 0) and check_statement(0, 0, 1) and
        check_statement(0, 1, 0) and check_statement(0, 1, 1) and
        check_statement(1, 0, 0) and check_statement(1, 0, 1) and
        check_statement(1, 1, 0) and check_statement(1, 1, 1)):
    print('True')
else:
    print('False')
