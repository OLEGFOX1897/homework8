import mod_use_data
import mod_load_save


print('Приветствую нового управляющего команды Real Madrid')
manager_name=input('Введите свое имя: ')
BD_start=mod_load_save.load()
def start_action(manager_name, BD_start): 
        print('-----------------------------------------------------------------------------------------')
        print(f'Главное меню: {manager_name}, введите номер варианта того, что вы хотите сделать с вашей командой')
        print('1 - Показать информацию о команде', '2 - Изменить команду', '3 - Завершить работу',
                '4 - Восстановить исходную версию команды', sep = '\n')
        action=input('Выбор = ')
        if action=='1':
            show_inf(manager_name)
            start_action(manager_name, BD_start)
                # модуль просмотра
        elif action=='2':
            change_comand(manager_name)
            start_action(manager_name, BD_start)
                # модуль изменения
        elif action=='3':
            print(f'{manager_name}, досвидания. Все изменения записаны в исходный фаил')
            return
                # Добавить запись в исходный фаил
        elif action=='4':
            mod_load_save.save(BD_start)
            print('-----------------------------------------------------------------------------------------')
            print_BD(mod_load_save.load())
            start_action(manager_name, BD_start)
        else:
            print('Повторите ввод действия')
            start_action(manager_name, BD_start)

def show_inf(manager_name): # 2 вариант Главного меню
    print('-----------------------------------------------------------------------------------------')
    print(f'Информационное меню: {manager_name}, введите номер варианта того, что вы хотите сделать с вашей командой')
    print('1 - Показать всех', '2 - Вернуться в главное меню', sep = '\n')
    action=input('Введите вариант действия: ')
    if action=='1':
        print_BD(mod_use_data.use_data(mod_load_save.load(),0,0))
    elif action=='2':
        start_action(manager_name)
                # модуль изменения
    else:
        print('Повторите ввод действия')
        show_inf(manager_name)

def change_comand(manager_name): # 3 вариант Главного меню
    print('-----------------------------------------------------------------------------------------')
    print(f'Меню изменений: {manager_name}, введите номер варианта того, что вы хотите сделать с вашей командой')
    print('1 - Изменить основной состав ', '2 - Удалить игрока', '3 - Добавить игрока, если есть вакантная должность',
             '4 - Вернуться в главное меню', sep = '\n')
    action=input('Введите вариант действия: ')
    if action=='1':
        print('-----------------------------------------------------------------------------------------')
        data=mod_use_data.use_data(mod_load_save.load(), 0,0)
        print_BD(data)
        while True:
            print('Введите номер игрока из основного состава, которого хотите поменять')
            num_footballer=inp_num(1)
            if num_footballer in range(1,5): # т.к. в основном составе 4 игрока
                break
            else:
                print('Вы ввели номер не из основного состава. Повторите ввод.')
        data1=mod_use_data.use_data(mod_load_save.load(), num_footballer, 0)
        print('-----------------------------------------------------------------------------------------')
        print('Ваша новая команда:')
        print_BD(data1)
    elif action=='2':
        print('-----------------------------------------------------------------------------------------')
        print_BD(mod_use_data.use_data(mod_load_save.load(), 0,0))
        while True:
            print('Введите номер игрока из основного состава, которого хотите удалить')
            num_footballer=inp_num(1)
            if num_footballer in range(1,9): # т.к. в основном составе 4 игрока
                break
            else:
                print('Вы ввели несуществующий номер.')
        data1=mod_use_data.use_data(mod_load_save.load(), num_footballer, 1)
        print('-----------------------------------------------------------------------------------------')
        print('Ваша новая команда:')
        print_BD(data1)
    elif action=='3':
        print('-----------------------------------------------------------------------------------------')
        data=mod_use_data.use_data(mod_load_save.load(), 0,0)
        print_BD(data)
        count=1
        for ind in data.items():
            count+=1
            if ind[1]=='  ':
                num_footballer=str(input(f'Введите как будут звать {ind[0]} : '))
                print('-----------------------------------------------------------------------------------------')
                print('Ваша новая команда:')
                print_BD(mod_use_data.use_data(data, num_footballer, 2))
                break
            elif count==8:
                print('У вас нет вакантных должностей. Сначала кого нибудь увольте!')
                change_comand(manager_name)
                break
    elif action=='4':
        start_action(manager_name, BD_start)



def inp_num(type_num): 
	'''Функция возвращает либо целое, либо вещественное введенное число. Проверяет правильность ввода.
	При вх 1 - проверяет, что введенное число целое.
	При вх 0 - проверяет, что введенное число вещественное, а не буквы или знаки.'''
	ind=0
	while ind==0:
		if type_num==1: #целое
			try:
				num=int(input('n='))
				ind=1
			except:
				ind=0
				print('Повторите ввод')

		elif type_num==0:
			try:
				num=float(input('n='))
				ind=1
			except:
				ind=0
				print('Повторите ввод')
		else:
			print('В функции inp_num указан неверный вх параметр (может быть 0 или 1)')
	return num

def print_BD(data):
    '''Печатает вертикально данные из словаря'''
    for key,value in data.items():
            print(key,':', value)

start_action(manager_name, BD_start)   
