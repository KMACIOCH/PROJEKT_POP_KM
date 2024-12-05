import folium
import requests
from bs4 import BeautifulSoup
from model.data import users, publications, workers, customers


def show_library(users: list[dict[str, str]]) -> None:
    for user in users[0:]:
        print(f"Nazwa: {user['name']} , Lokalizacja: {user['location']}")


def add_new_library(users: list[dict[str, str]]) -> None:
    name = input("Nazwa księgarni: ")
    location = input("Lokalizacja: ")
    new_user = {"name": name, "location": location}
    print(new_user)
    users.append(new_user)


def delete_library(users: list[dict[str, str]]) -> None:
    user_name = input("Jaką księgarnie usunąć?: ")
    for user in users:
        if f"{user['name']}" == user_name:
            users.remove(user)


def edit_library(users: list[dict[str, str]]) -> None:
    user_name = input("Jaką księgarnie uaktualnić?: ")
    for user in users:
        if f"{user['name']}" == user_name:
            user["name"] = input("Nazwa księgarni: ")
            user["location"] = input("Lokalizacja: ")
            print(user)
            users.append(user)


def show_publicator(publications: list[dict]) -> None:
    for publicator in publications:
        print(f" Imię: {publicator['name']} Nazwisko: {publicator['surname']}, nazwa książki: {publicator['bookname']}, lokalizacja: {publicator['location']}")

def add_publicator(publications: list[dict]) -> None:
    publicator_name = input("Imie publikatora: ")
    publicator_surname = input("Nazwisko publikatora: ")
    publicator_bookname = input("Nazwa książki ")
    publicator_location = input("Lokalizacja: ")
    new_publicator = {"name": publicator_name, "surname": publicator_surname, "bookname": publicator_bookname, "location": publicator_location}
    print(new_publicator)
    publications.append(new_publicator)


def delete_publicator(publications: list[dict]) -> None:
    publicator_name = input("Którego wydawce usunąć?: ")
    for publicator in publications:
        if publicator['name'] == publicator_name:
            publications.remove(publicator)


def update_publicator(publications: list[dict])-> None:
    publicator_name = input("Który wydawce edytować: ")
    for publicator in publications:
        if publicator['name'] == publicator_name:
            publicator['name'] = input("Imię: ")
            publicator['surname'] = input("Nazwisko: ")
            publicator['bookname'] = input("Nazwa książki: ")
            publications.append(publicator)


def show_workers(workers_list: list[dict]) -> None:
    for worker in workers_list:
        print(f"{worker['name']} {worker['surname']}, księgarnia: {worker['library']}, mieszka w: {worker['location']}")


def add_workers(workers: list) -> None:
    worker_name = input("Imie: ")
    worker_surname = input("Nazwisko: ")
    worker_library = input("Księgarnia: ")
    worker_location = input("Mieszka w: ")
    new_workers = {'name': worker_name, 'surname': worker_surname, 'library': worker_library, 'location': worker_location}
    workers.append(new_workers)


def delete_workers(workers: list) -> None:
    worker_name = input("Kogo usunąć?: ")
    for worker in workers:
        if f"{worker['name']}" == worker_name:
            workers.remove(worker)


def update_worker(workers: list) -> None:
    worker_name = input("Kogo edytować?: ")
    for worker in workers:
        if f"{worker['name']}" == worker_name:
            worker['name'] = input("Imie: ")
            worker['surname'] = input("Nazwisko: ")
            worker['library'] = input("Księgarnia: ")
            worker['location'] = input("Mieszka w: ")
            workers.append(worker)


def show_customers(customers_list: list[dict]) -> None:
    for customers in customers_list:
        print(
            f"{customers['name']} {customers['surname']}, księgarnia: {customers['library']}")

def library_workers(users: list[dict[str, str]], workers: list[dict]) -> None:
    user_name = input("Podaj nazwę księgarni: ")
    for user in users:
        if user_name == user['name']:
            for worker in workers:
                if worker['library'] == user_name:
                    print(f" Pracownik: {worker['name']} {worker['surname']}")


def library_customers(users: list[dict[str, str]], customers: list[dict]) -> None:
    user_name = input("Podaj nazwę księgarni: ")
    for user in users:
        if user_name == user['name']:
            for customer in customers:
                if customer['library'] == user_name:
                    print(f" Klient: {customer['name']} {customer['surname']}")


def map_users(users):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for user in users:
        url = (f"https://pl.wikipedia.org/wiki/{user['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{user['name']},\n{user['location']}",
                      icon=folium.Icon(color='green')).add_to(map)

    map.save('utils/map_libraries.html')


def map_workers(workers):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for worker in workers:
        url = (f"https://pl.wikipedia.org/wiki/{worker['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{worker['name']},\n{worker['location']}",
                      icon=folium.Icon(color='black')).add_to(map)

    map.save('utils/map_workers.html')


def map_publications(publications):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for publicator in publications:
        url = (f"https://pl.wikipedia.org/wiki/{publicator['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{publicator['name']},\n{publicator['location']}",
                      icon=folium.Icon(color='blue')).add_to(map)

    map.save('utils/map_publications.html')