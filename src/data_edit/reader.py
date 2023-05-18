from const import FILE_PATH


def get_all_contacts() -> None:
    with open(FILE_PATH, 'r', encoding='utf8')as contact_data:
        for line in contact_data:
            print(line.strip())


def search_contact() -> None:
    with open(FILE_PATH, 'r', encoding='utf8') as contact_data:
        type_request = int(input('\n1. Поиск по имени.'
                                 '\n2. Поиск по фамилии'
                                 '\n3. Поиск по отчеству'
                                 '\n4. Поиск по номеру телефона'
                                 '\n5. Назад'
                                 '\n--> '))

        match type_request:
            case 1:
                request = 0
            case 2:
                request = 1
            case 3:
                request = 2
            case 4:
                request = 3
            case default:
                return

        user_search = input('Введите данные для поиска: ').lower()
        for line in contact_data:
            contact = line.strip().split(';')
            if user_search in contact[request].lower():
                print(" ".join(contact))

    return