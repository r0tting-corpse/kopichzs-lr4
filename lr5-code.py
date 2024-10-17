def check_sign(arr):
    """Проверяет, составляют ли все элементы массива одного знака."""
    if not arr:  # Проверяем, что массив не пустой
        return False
    
    first_sign = arr[0] > 0  # Определяем знак первого элемента
    for num in arr:
        if (num > 0) != first_sign:  # Если знак отличается, возвращаем False
            return False
    return True  # Все элементы одного знака

def main():
    """Основная функция для ввода массивов и проверки их знака."""
    arrays = []  # Список для хранения массивов
    num_arrays = 5  # Количество массивов
    
    # Вводим массивы
    for i in range(num_arrays):
        array_input = input(f"Введите элементы массива {i + 1} через пробел: ")
        array = list(map(float, array_input.split()))  # Преобразуем ввод в список вещественных чисел
        arrays.append(array)

    found = False  # Флаг для отслеживания найденных массивов одного знака
    
    # Проверяем каждый массив
    for i in range(num_arrays):
        if check_sign(arrays[i]):
            print(f"Элементы массива {i + 1} составляют одного знака.")
            found = True
            
    if not found:
        print("Нет массивов с элементами одного знака.")

# Запуск основной программы
if __name__ == "__main__":
    main()
