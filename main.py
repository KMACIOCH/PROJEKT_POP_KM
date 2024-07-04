from model.data import users, publications, workers, customers
from utils.crud import show_library, add_new_library, delete_library, edit_library, library_workers, map_workers, add_publicator, update_publicator, show_publicator, update_worker, library_customers, delete_publicator, show_workers, add_workers, delete_workers, show_customers, map_users, map_publications
correct_password = "l"
while True:
    password = input('Wprowaź hasło: ')
    if password == correct_password:
        print('Poprawne')
        break
    else:
        print('Niepoprawne hasło spróbuj ponownie')

if __name__ == '__main__':
    print('Witaj')

    while True:
        print('0. Wyjście ')
        print('1. Wyświetl księgarnie')
        print('2. Dodaj księgarnie ')
        print('3. Usuń księgarnie')
        print('4. Edytuj księgarnie ')
        print('5. Wyświetl wydawców')
        print('6. Dodaj wydawce')
        print('7. Usuń wydawce')
        print('8. Edytuj wydawce')
        print('9. Wyświetl pracowników')
        print('10. Dodaj pracownika')
        print('11. Usuń pracownika')
        print('12. Edytuj pracownika')
        print('13. Wyświetl wszystkich klientów')
        print('14. Wyświetl klientów wybranej księgarni')
        print('15. Wyświetl pracowników wybranej księgarni')
        print('16. Pokaż mapę wszystkich księgarni')
        print('17. Pokaż mapę wszystkich pracowników')
        print('18. Pokaż mapę  wszystkich wydawców')
        menu_option = input('wybierz opcje menu: ')
        if menu_option == '0': break
        if menu_option == '1': show_library(users)
        if menu_option == '2': add_new_library(users)
        if menu_option == '3': delete_library(users)
        if menu_option == '4': edit_library(users)
        if menu_option == '5': show_publicator(publications)
        if menu_option == '6': add_publicator(publications)
        if menu_option == '7': delete_publicator(publications)
        if menu_option == '8': update_publicator(publications)
        if menu_option == '9': show_workers(workers)
        if menu_option == '10': add_workers(workers)
        if menu_option == '11': delete_workers(workers)
        if menu_option == '12': update_worker(workers)
        if menu_option == '13': show_customers(customers)
        if menu_option == '14': library_workers(users, customers)
        if menu_option == '15': library_customers(users, workers)
        if menu_option == '16': map_users(users)
        if menu_option == '17': map_workers(workers)
        if menu_option == '18': map_publications(publications)

