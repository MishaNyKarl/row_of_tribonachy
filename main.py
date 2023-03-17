import time
from functools import lru_cache


def use_lru_cache(n):
    pass

def tribonachy(number):
    """Главная Функция для нахождения чисел трибоначи"""
    if number == 0 or number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return tribonachy(number - 1) + tribonachy(number - 2) + tribonachy(number - 3)


user_dicision = 'ok'

while user_dicision != 'stop':
    print(
        '____________________________________________________________________________________________________________________')
    print('Для получение некоторой интересной статистики введите "test"\n'
          'Для остановки введите "stop"')
    user_dicision = (input(
        'Введите число неотрицательное число, чтобы получить его значение в ряду Трибоначи: '))  # Сообщение от пользователя

    t1 = time.time()

    if user_dicision == 'test':
        last_proc_time = 0.0
        delta_proc = 0
        row_of_trib_num = []

        for i in range(1, 31):
            t_test = time.time()
            test_number = tribonachy(i)
            time_of_work = time.time() - t_test
            if time_of_work != 0.0:
                delta_proc = (last_proc_time / time_of_work) * 100

            print(
                f'Число {i} = {test_number} найдено за {round(time_of_work, 2)} секунд, что больше предыдущего на {round(delta_proc, 3)}%')

            row_of_trib_num.append(test_number)
            last_proc_time = time_of_work

        print(f'Ряд фибоначи до 30: {row_of_trib_num}')

    elif type(int(user_dicision)) == int:
        if int(user_dicision) >= 0:
            t1 = time.time()
            output = tribonachy(int(user_dicision))
            time_of_work = time.time() - t1

            print(f'\nВаше число: {output} найдено за {time_of_work}')

    elif user_dicision == 'stop':
        print(
            'До свидания\n____________________________________________________________________________________________________________________')
        break

    else:
        print('\nЯ вас не понял')
