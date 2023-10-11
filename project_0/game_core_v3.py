import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
        Функция принимает загаданное число и возвращает число попыток.
        
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    
    count = 0
    predict = np.random.randint(1, 101)
    #Прописываем условия угадывания числа
    while number != predict:
        count += 1
        if number < predict:
            if predict < 20:
                number += 1
            elif predict >= 20 and predict <= 30:
                if number < 10:
                    number += 10
                else:
                    number += 1
            elif predict >= 30 and predict <= 40:
                if number < 20:
                    number += 20
                else:
                    number += 1
            elif predict >= 40 and predict <= 50:
                if number < 40:
                    number += 30
                else:
                    number += 1
            elif predict >= 50 and predict <= 60:
                if number < 50:
                    number += 10
                else:
                    number += 1
            elif predict >= 60 and predict <= 70:
                if number < 60:
                    number += 10
                else:
                    number += 1
            elif predict >= 70 and predict <= 80:
                if number < 70:
                    number += 10
                else:
                    number += 1
            elif predict >= 80 and predict <= 90:
                if number < 80:
                    number += 10
                else:
                    number += 1
            elif predict >= 90 and predict <= 100:
                if number < 90:
                    number += 10
                else:
                    number += 1

        else:
            if predict < 10:
                if number > 10:
                    number -= 10
                else:
                    number -= 1
            elif predict >= 90 and predict <= 100:
                if number > 100:
                    number -= 10
                else:
                    number -= 1
            elif predict >= 80 and predict <= 90:
                if number > 90:
                    number -= 10
                else:
                    number -= 1
            elif predict >= 70 and predict <= 80:
                if number > 90:
                    number -= 10
                else:
                    number -= 1
            elif predict >= 60 and predict <= 70:
                if number > 70:
                    number -= 10
                else:
                    number -= 1
            elif predict >= 50 and predict <= 60:
                if number > 60:
                    number -= 10
                else:
                    number -= 1
            elif predict >= 40 and predict <= 50:
                if number > 50:
                    number -= 10
                else:
                    number -= 1
            elif predict >= 30 and predict <= 40:
                if number > 40:
                    number -= 10
                else:
                    number -= 1
            elif predict >= 20 and predict <= 30:
                if number > 30:
                    number -= 10
                else:
                    number -= 1
            elif predict >= 10 and predict <= 20:
                if number > 20:
                    number -= 10
                else:
                    number -= 1

    # Ваш код заканчивается здесь

    return count