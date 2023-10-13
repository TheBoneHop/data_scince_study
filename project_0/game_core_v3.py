import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, проверяем больше или меньше наше 
    число от загаданного и устанавливаем его как границу промежутка в зависимости от результата
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    # Инициализируем переменные
    low = 1
    high = 101
    predict = 0
    count = 0

    # Пока не угадаем число
    while predict != number:
        # Проверяем условие больше или меньше загаданного числа
        predict = np.random.randint(low, high)
        count += 1
        
        if predict > number:
            if predict - 1 == number:
                predict -= 1
            else:
                high = predict - 1
        elif predict < number:
            low = predict + 1
    
    return count
