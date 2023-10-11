import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем рандомное число, а потом воссоздаем 
    его посимвольно при помощи использования строк и циклов.
        Функция принимает загаданное число и возвращает число попыток.
        
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    #Инициализируем список со всеми существующими цифрами
    lst_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0
    result_number = ''
    predict = np.random.randint(1, 101)
    
    #Итерируем рандомное число по символам и список по элементам
    while number != predict:
        for i in str(predict):
            for n in lst_of_numbers:
                if n == i:
                    #Заносим подходящий символ в результирующую переменную и увеличиваем число попыток на 1
                    result_number += n
                    count += 1
        number = int(result_number)            

    return count