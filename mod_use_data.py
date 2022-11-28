import mod_load_save

# BD={'1-Основной нападающий (капитан)': 'Карим Бензема (Франция)', '2-Основной полузащитник':'Федерико Вельвердус (Уругвай)',
#     '3-Основной защитник':'Ферлан Менди (Франция)', '4-Основной вратарь':'Куртуа, Тибо (Бельгия)', '5-Запасной нападающий':'Винисиус Жуниор (Бразилия)',
#     '6-Запасной полузащитник':'Тони Кроос (Германия)', '7-Запасной защитник':'Эден Милитиан (Бразилия)', '8-Запасной вратарь':'Луис Лопес (Испания)' }

def use_data(BD, A, creat_del): # A - номер игрока, creat_del- параметр для добавления и удаления игрока (1-удалиение, 2- добавление)
    if A==0 and creat_del==0: 
        return BD
    elif A in range(1,5) and creat_del==0:
        B=A+4 # номер запасного игрока (всего в команде с запасными 8)
        # print(B)
        for ind in BD.items():
            keys=ind[0]
            # print(keys)
            if str(A) in keys:
                buf_one=BD.get(keys)
                key_one=keys
            elif str(B) in keys:
                buf_two=BD.get(keys)
                key_two=keys
                BD[key_one]=buf_two
                BD[key_two]=buf_one
                mod_load_save.save(BD)
                break
        return BD
    elif creat_del==1:
        for ind in BD.items():
            keys=ind[0]
            if str(A) in keys:
                BD[keys]='  '
                mod_load_save.save(BD)
                break
        return BD
    elif creat_del==2:
        for ind in BD.items():
            items=ind[1]
            if '  ' in items:
                BD[ind[0]]=A
                mod_load_save.save(BD)
                print('Добавлен новый член команды')
                break
        return BD

# use_data(BD,4,2)

# # def print_BD(data):
# #     '''Печатает вертикально данные из словаря'''
# #     for key,value in data.items():
# #             print(key,':', value)
# # print_BD(BD)
# # a=2
# # if a in range(0,3):
# #     print('ok')       



# for keys in BD.items():
#     print(keys)
