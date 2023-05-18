import data_edit


def start_menu():
    while True:
        user_input = int(input('\n1. Вывести все контакты.'   
                               '\n2. Поиск контакта ...'
                               '\n3. Добавить контакт'
                               '\n4. Изменить контакт'
                               '\n5. Удалить контакт'
                               '\n6. Сохранить в ...'
                               '\n7. Выйти'
                               '\n--> '))

        match(user_input):
            case 1:
                data_edit.get_all_contacts()
            case 2:
                data_edit.search_contact()
            case 3:
                data_edit.add_contact()
            case 4:
                data_edit.edit_contacts()
            case 5:
                data_edit.del_contacts()
            case 6:
                pass
            case default:
                break
