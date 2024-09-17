import random
import time

def print_status(mouse, cats, dog):
    print(f"\nМышка находится на позиции {mouse}.")
    print("Кошки на позициях:", ', '.join(map(str, cats)))
    print(f"Собака находится на позиции {dog}.")

def move_mouse(mouse):
    move = input("Куда движется мышка? (влево/вправо): ").strip().lower()
    if move == "влево":
        return max(mouse - 1, 0)
    elif move == "вправо":
        return mouse + 1
    else:
        print("Некорректный ввод. Мышка не двигается.")
        return mouse

def move_cats(cats):
    for i in range(len(cats)):
        if random.choice([True, False]):
            cats[i] += random.choice([-1, 1])  # Кошки могут двигаться влево или вправо
    return list(set(cats))  # Убираем дубликаты

def move_dog(dog):
    return dog + random.choice([-1, 1])  # Собака может двигаться влево или вправо

def main():
    mouse = 5
    cats = [3, 7]
    dog = 4
    while True:
        print_status(mouse, cats, dog)
        
        # Проверка на ловлю
        if mouse in cats:
            print("Кошка поймала мышку! Игра окончена.")
            break
        
        if mouse == dog:
            print("Собака поймала мышку! Игра окончена.")
            break
        
        mouse = move_mouse(mouse)
        cats = move_cats(cats)
        dog = move_dog(dog)
        
        time.sleep(1)  # Задержка, чтобы игра выглядела более плавной

if __name__ == "__main__":
    main()
