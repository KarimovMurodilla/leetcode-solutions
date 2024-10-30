def parse_config():
    # Количество объектов в корне
    objects = {}
    stack = [objects]
    
    while True:
        line = input().strip()
        if line.isdigit():  # Проверяем, если это число, значит, это количество запросов K
            return objects, int(line)
        
        parts = line.split()
        name = parts[0]
        
        if parts[1] == '0':
            # Это объект второго типа, сохраняем значение
            value = int(parts[2])
            stack[-1][name] = value
        else:
            # Это объект первого типа, создаем новый вложенный объект
            count = int(parts[1])
            new_obj = {}
            stack[-1][name] = new_obj
            stack.append(new_obj)

def process_queries(objects, k):
    for _ in range(k):
        query = input().strip().split('.')
        current = objects
        for key in query:
            if key in current:
                current = current[key]
            else:
                print("not found")
                break
        else:
            if isinstance(current, int):
                print(current)
            else:
                print("not found")

def main():
    # Читаем конфигурацию и запросы
    objects, k = parse_config()
    
    # Обрабатываем запросы
    print("result:")
    process_queries(objects, k)

# Вызов основного процесса
if __name__ == "__main__":
    
    main()
