# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

# a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!

# b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.

# c) * Решить задачу под пунктом b, не создавая новый список.


sum1 = 0
def sum(cube):
    num_sum = 0
    while cube != 0:
        num_sum += cube % 10
        cube = cube // 10
    return num_sum
cubes = (i**3 for i in range(1, 1000, 2))
cubes = list(cubes)
print(cubes)
for i in range(len(cubes)):
    if sum(cubes[i]) % 7 == 0:
        sum1 += cubes[i]
print(sum1)
for i in range(len(cubes)):
    if sum(cubes[i] + 17) % 7 == 0:
        sum1 += cubes[i] + 17
print(sum1)
