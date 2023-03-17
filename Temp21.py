def menu():
    dict_phnbk = {}
    while True:
        anc = int(input('Введите запрос: 1:Сохранить телефонную книгу, 2: Показать все контакты, 3:Найти контакт '
                        '4:Добавить контакт, 5:Изменить контакт,  6: Удалить контакт, 7: Выход :'))
        if anc == 1:
            save_dir(dict_phnbk)
            print('save')
        elif anc == 2:
            if len(dict_phnbk) == 0:
                dict_phnbk = open_read_dir()
            if len(dict_phnbk) == 0:
                print('Справочник пуст')
            else:
                print(dict_phnbk)
        elif anc == 3:
            cntc_find(dict_phnbk)
        elif anc == 4:
            value_new_cnt = add_cntc(dict_phnbk)
            print(value_new_cnt)
            dict_phnbk.update(value_new_cnt)
            print('Сохранись!')
        elif anc == 5:
            new_cntc = cntc_find(dict_phnbk)
            add_cntc(dict_phnbk, new_cntc)
        elif anc == 6:
            new_cntc = cntc_find(dict_phnbk)
            print(f'Удалили контант:{new_cntc[0]}: {dict_phnbk.pop(new_cntc[0])}')
            print('Сохранись!')
        elif anc == 7:
            print('End')
            break
        else:
            print('Введите ещё раз')


def open_read_dir():
    dict_phnbk = {}
    with open('phonebook.txt', 'r') as f:
        for line_cntc in f.readlines():
            key, value = line_cntc.split(':')
            dict_phnbk[key] = value
        # print(dict_phnbk)
        return dict_phnbk


def save_dir(dict_phnbk):
    str_phnbk = ''
    print(dict_phnbk)
    for key, value in dict_phnbk.items():
        str_phnbk += f'{key}:{value} \n'
    with open('phonebook.txt', 'w') as f:
        f.write(str_phnbk)


def add_cntc(dict_phnbk, new_cntc_in = [0]):
    if len(new_cntc_in) < 2:
        name_cntc = input('Введите Имя Фамилию')
        phone_cntc = input('Введите телефон')
        comment_cntc = input('Введите комментарий')
        cntc_list = [phone_cntc, comment_cntc]
    else:
        name_cntc, cntc_list = tuple(new_cntc_in)
    # dict_phnbk[name_cntc] = dict_phnbk.setdefault(name_cntc, cntc_list)
    dict_phnbk.setdefault(name_cntc, cntc_list)
    print(f'{name_cntc}, {dict_phnbk[name_cntc]}')
    return dict_phnbk


def cntc_find(dict_phnbk):
    name_cntc = input('Введите Имя Фамилию')
    if name_cntc in dict_phnbk:
        print(f'{name_cntc}: {dict_phnbk[name_cntc]}')
        return [name_cntc, dict_phnbk[name_cntc]]
    else:
        print(f'Не найдено')


menu()