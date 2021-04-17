def voproc():
    """Замена всех знаков на '?'"""
    for i in range(len(lst)):
        lst[i] = '?'
    print(f'Загаданное слово:{lst}')

def razbif():
    """Ввод числа и разбиение его на список"""
    slovo = input('Загадайте слово:')
    for i in slovo:
        lst.append(i)
        lst2.append(i)

def change(life):
    """Отгадывание букв и весь процесс игры"""
    while True:
        if life != 0 and '?' in lst:
            word2 = input('Введите букву:')
            if word2 in lst2 and word2 not in lst:
                for i in range(len(lst)):
                    if word2 == lst2[i]:
                        lst[i] = word2
                        print(lst)
            else:
                print('Такой буквы нет или эта буква уже открыта.')
                life = life - 1
                print(f'У вас {life} жизней')
        else:
            print('Вы победили! Все буквы открыты.')
            break

if __name__ == '__life9__':
    lst = []
    lst2 = []
    razbif()
    voproc()
    change(9)