# # для секунд
# duration = int(input("duration = "))
# print(duration, 'сек')
# # для минут
# duration = int(input("duration = "))
# if duration > 60:
#     min = duration // 60
#     sec = duration % 60
# print(min, 'мин', sec, 'sec')
# # для часов
# duration = int(input("duration = "))
# if duration > 3600:
#     hour = duration // 3600
#     remainder_hour = duration % 3600
#     min = remainder_hour // 60
#     sec = duration % 60
# print(hour, 'час(а)', min, 'мин', sec, 'сек')
# # для дней
# duration = int(input("duration = "))
# if duration > 86400:
#     day = duration // 86400
#     remainder_hour = duration % 86400
#     hour = remainder_hour // 3600
#     remainder = duration % 3600
#     min = remainder // 60
#     sec = duration % 60
# print(day, 'день', hour, 'час(а)', min, 'мин', sec, 'сек')

# duration = int(input("duration = "))
# if duration < 60:
#     print(duration, 'сек')
# elif 3600 > duration >= 60:
#     min = duration // 60
#     sec = duration % 60
#     print(min, 'мин', sec, 'sec')
# elif 86400 > duration >= 3600:
#     hour = duration // 3600
#     remainder_hour = duration % 3600
#     min = remainder_hour // 60
#     sec = duration % 60
#     print(hour, 'час(а/ов)', min, 'мин', sec, 'сек')
# else:
#     duration >= 86400
#     day = duration // 86400
#     remainder_hour = duration % 86400
#     hour = remainder_hour // 3600
#     remainder = duration % 3600
#     min = remainder // 60
#     sec = duration % 60
#     print(day, 'день', hour, 'час(а/ов)', min, 'мин', sec, 'сек')

# my_list = [3, 61, 3698, 654789]
# for i in range(len(my_list)):
#     if my_list[i] < 60:
#         print(my_list[i], 'сек')
#     elif 3600 > my_list[i] >= 60:
#         min = my_list[i] // 60
#         sec = my_list[i] % 60
#         print(min, 'мин', sec, 'sec')
#     elif 86400 > my_list[i] >= 3600:
#         hour = my_list[i] // 3600
#         remainder_hour = my_list[i] % 3600
#         min = remainder_hour // 60
#         sec = my_list[i] % 60
#         print(hour, 'час(а/ов)', min, 'мин', sec, 'сек')
#     else:
#         my_list[i] >= 86400
#         day = my_list[i] // 86400
#         remainder_hour = my_list[i] % 86400
#         hour = remainder_hour // 3600
#         remainder = my_list[i] % 3600
#         min = remainder // 60
#         sec = my_list[i] % 60
#         print(day, 'день', hour, 'час(а/ов)', min, 'мин', sec, 'сек')

