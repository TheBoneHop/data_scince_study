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
    # Ваш код начинается здесь
    count = 0
    predict = np.random.randint(1, 101)
    #Прописываем условия угадывания числа
    while number != predict:
        count += 1
        if number > predict:
            if predict < 20:
                predict += 1
            elif number >= 20 and number <= 30:
                if predict < 10:
                    predict += 10
                else:
                    predict += 1
            elif number >= 30 and number <= 40:
                if predict < 20:
                    predict += 20
                else:
                    predict += 1
            elif number >= 40 and number <= 50:
                if predict < 40:
                    predict += 30
                else:
                    predict += 1
            elif number >= 50 and number <= 60:
                if predict < 50:
                    predict += 10
                else:
                    predict += 1
            elif number >= 60 and number <= 70:
                if predict < 60:
                    predict += 10
                else:
                    predict += 1
            elif number >= 70 and number <= 80:
                if predict < 70:
                    predict += 10
                else:
                    predict += 1
            elif number >= 80 and number <= 90:
                if predict < 80:
                    predict += 10
                else:
                    predict += 1
            elif number >= 90 and number <= 100:
                if predict < 90:
                    predict += 10
                else:
                    predict += 1

        else:
            if number < 10:
                if predict > 10:
                    predict -= 10
                else:
                    predict -= 1
            elif number >= 90 and number <= 100:
                if predict > 100:
                    predict -= 10
                else:
                    predict -= 1
            elif number >= 80 and number <= 90:
                if predict > 90:
                    predict -= 10
                else:
                    predict -= 1
            elif number >= 70 and number <= 80:
                if predict > 90:
                    predict -= 10
                else:
                    predict -= 1
            elif number >= 60 and number <= 70:
                if predict > 70:
                    predict -= 10
                else:
                    predict -= 1
            elif number >= 50 and number <= 60:
                if predict > 60:
                    predict -= 10
                else:
                    predict -= 1
            elif number >= 40 and number <= 50:
                if predict > 50:
                    predict -= 10
                else:
                    predict -= 1
            elif number >= 30 and number <= 40:
                if predict > 40:
                    predict -= 10
                else:
                    predict -= 1
            elif number >= 20 and number <= 30:
                if predict > 30:
                    predict -= 10
                else:
                    predict -= 1
            elif number >= 10 and number <= 20:
                if predict > 20:
                    predict -= 10
                else:
                    predict -= 1

    # Ваш код заканчивается здесь

    return count
