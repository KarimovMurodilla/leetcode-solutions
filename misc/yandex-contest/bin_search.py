def main():
    # Чтение первой строки ввода (N, M, K)
    N, M, K = map(int, input().split())

    # Мапа для хранения индексов найденных элементов
    index_map = {}

    # Считываем результаты бинарного поиска
    for _ in range(M):
        number, index = map(int, input().split())
        index_map[number] = index

    # Получаем все известные числа в отсортированном порядке
    known_numbers = sorted(index_map.keys())
    
    # Обрабатываем запросы
    results = []
    for _ in range(K):
        query = int(input())
        
        if query in index_map:
            results.append(str(index_map[query]))  # элемент найден, добавляем индекс в результат
        else:
            # Проверяем, может ли элемент находиться в массиве
            if len(known_numbers) == 0:
                results.append('-1')
                continue
            
            min_value = known_numbers[0]
            max_value = known_numbers[-1]

            # Если элемент меньше минимального известного
            if query < min_value:
                results.append('-1')
            # Если элемент больше максимального известного
            elif query > max_value:
                results.append('-1')
            else:
                # Проверяем, может ли элемент быть между известными числами
                found = False
                for i in range(len(known_numbers) - 1):
                    if known_numbers[i] < query < known_numbers[i + 1]:
                        results.append('-2')
                        found = True
                        break
                if not found:
                    results.append('-1')  # Если не нашли подходящий промежуток, элемент точно не найден

    # Вывод всех результатов
    print('\n'.join(results))

if __name__ == "__main__":
    main()
