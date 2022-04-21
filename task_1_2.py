# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

# a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!

# b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.

# c) * Решить задачу под пунктом b, не создавая новый список.

# 1й вариант решения:
# Создаем список из кубов нечетных чисел от 1 до 1000
cubes = []
for num in range(1, 1000, 2):
    cubes.append(num ** 3)
print("кубы: ", cubes)

# а) Создаем список из сумм цифр каждого числа из списка cubes
# сначала создал цикл while для суммирования цифр для 1 числа, затем добавил цикл for и сделал перебор чисел из списка cubes.
sums = []
for cube in cubes:
    sum = 0
    while cube != 0:
        sum += cube % 10
        cube = cube // 10
    sums.append(sum) # вернул получившуюся сумму в список sum для каждого элемента
# print("суммы чисел: ", sums)
# перечисляем числа, которые делятся на 7 без остатка и отправляем их в список division_by_seven
division_by_seven = []
for seven in sums:
    if seven % 7 == 0:
        #seven = seven + 17
        division_by_seven.append(seven)
print("1е деление на 7: ", division_by_seven)

# b)
for i in range(len(cubes)):
    cubes[i] += 17
print("кубы + 17: ", cubes)

sums2 = []
for cube in cubes:
    sum = 0
    while cube != 0:
        sum += cube % 10
        cube = cube // 10
    sums2.append(sum)
# print("суммы чисел: ", sums2)

division_by_seven2 = []
for seven in sums2:
    if seven % 7 == 0:
        division_by_seven2.append(seven)
print("2е деление на 7: ", division_by_seven2)

# 2й вариант решения(правильный):
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
