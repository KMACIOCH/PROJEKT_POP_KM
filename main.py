from model.data import users
from utils.crud import read_user, add_user, search_user, remove_user, update_user
from utils.map import single_map, full_map

correct_password = "Dol"
while True:
    password = input('Wprowaź hasło: ')
    if password == correct_password:
        print('Poprawne')
        break
    else:
        print('Niepoprawne hasło spróbuj ponownie')

def main() -> None:
    while True:
        print("Witamy w menu  ")
        print("0. Wyjście ")
        print("1. Wyświetl liste firm ")
        print("2. Dodaj nową firmę")
        print("3. Wyszukaj firmę")
        print("4. Usuń firmę")
        print("5. Zaktualizuj firmę")
        print("6. Wygeneruj mape dla jednej firmy")
        print("7. Wygeneruj mape dla wszystkich firm")

        menu_option = input("Choose an option:")
        if menu_option == "0": break
        if menu_option == "1": read_user(users)
        if menu_option == "2": add_user(users)
        if menu_option == "3": search_user(users)
        if menu_option == "4": remove_user(users)
        if menu_option == "5": update_user(users)
        if menu_option == "6": single_map(search_user(users)['location'])
        if menu_option == "7": full_map(users)


if __name__ == '__main__':
    main()
