from random import randint
from balans import many
slot = randint(1,2)
bank = many
def game():
    global bank
    while 1:
        print(f'Ваш нынешний баланс: {bank}')
        com = input('1 Начало... \n2 конец...')
        if com == '1':
            insrt = int(input('Выберите слот: '))
            stav = int(input('Сколько хотите поставить: '))
            if insrt == slot:
                bank += (stav*2)
                print('Вы угодали!')
            elif slot != insrt and stav <= bank:
                if bank > 0 and stav <= bank:
                    bank -= stav
                    print('Вы не угодали!')
                else:
                    print('У вас не хватет денег!')
        elif com == '2':
            if bank < 1000:
                print('Вы в проиграше')
                print('Игра окончена')
                print(f'Ваша баланс {bank}')
                break
            elif bank > 1000:
                print('ВЫ в выйграше')
                print('Игра окончена')
                print(f'Ваш баланс {bank}')
                break
            else:
                print('Нет такой меню!')




