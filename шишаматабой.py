import random

# Размеры игрового поля
WIDTH = 5
HEIGHT = 5

def создать_поле(кот, мышка):
    поле = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]
    поле[кот[1]][кот[0]] = "К"  # Кот
    поле[мышка[1]][мышка[0]] = "М"  # Мышка
    return поле

def показать_поле(поле):
    for строка in поле:
        print(" ".join(строка))
    print()

def переместить_кот(кот, мышка):
    if кот[0] < мышка[0]:
        кот[0] += 1
    elif кот[0] > мышка[0]:
        кот[0] -= 1
    
    if кот[1] < мышка[1]:
        кот[1] += 1
    elif кот[1] > мышка[1]:
        кот[1] -= 1

def игра():
    кот = [0, 0]  # Начальная позиция кота
    мышка = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]  # Случайная позиция мышки

    while True:
        поле = создать_поле(кот, мышка)
        показать_поле(поле)

        if кот == мышка:
            print("Кот поймал мышку! Игра окончена.")
            break

        команда = input("Введите команду (вверх, вниз, влево, вправо) или 'выход' для завершения игры: ").lower()

        if команда == "выход":
            print("Вы вышли из игры.")
            return

        if команда == "вверх" and мышка[1] > 0:
            мышка[1] -= 1
        elif команда == "вниз" and мышка[1] < HEIGHT - 1:
            мышка[1] += 1
        elif команда == "влево" and мышка[0] > 0:
            мышка[0] -= 1
        elif команда == "вправо" and мышка[0] < WIDTH - 1:
            мышка[0] += 1
        else:
            print("Неверная команда или выход за границы поля!")

        переместить_кот(кот, мышка)

def main():
    while True:
        игра()
        ещераз = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if ещераз != "да":
            print("Спасибо за игру!")
            break

main()
