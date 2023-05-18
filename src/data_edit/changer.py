from const import FILE_PATH


def add_contact() -> None:
    first_name = input('Введите Имя: ')
    middle_name = input('Введите Отчество: ')
    last_name = input('Введите Фамилию: ')
    phone_number = input('Введите номер телефона: ')
    with open(FILE_PATH, 'a', encoding='utf8') as contact_data:
        contact_data.write(f'\n{first_name};{last_name};{middle_name};{phone_number}')


def edit_contacts() -> None:
    with open(FILE_PATH, 'r', encoding='utf8') as contact_data:
        all_contacts_info = contact_data.readlines()

    contact_search = input('Введите данные для поиска: ')
    contacts = [line for line in all_contacts_info if contact_search.lower() not in line.lower()]

    for line in all_contacts_info:
        if contact_search.lower() in line.lower():
            first_name = input('Введите Имя: ')
            middle_name = input('Введите Отчество: ')
            last_name = input('Введите Фамилию: ')
            phone_number = input('Введите номер телефона: ')
            contacts.append(f"{first_name};{last_name};{middle_name};{phone_number}")

    with open(FILE_PATH, 'w', encoding='utf8') as contact_data:
        for line in contacts:
            contact_data.write(line)


def del_contacts() -> None:
    with open(FILE_PATH, 'r', encoding='utf8') as contact_data:
        all_contacts_info = contact_data.readlines()

    del_contact = input('Введите данные для поиска: ')
    result = [line for line in all_contacts_info if del_contact.lower() not in line.lower()]

    with open(FILE_PATH, 'w', encoding='utf8') as contact_data:
        for line in result:
            contact_data.write(line)
