import requests


def create_user():
    response = requests.post('http://127.0.0.1:8080/user',
                             json={'username': 'marina', 'email': 'm@gmail.com', 'password': '12345'})
    data = response.json()
    print(data)


def get_user():
    response = requests.get('http://127.0.0.1:8080/user/1')
    print(response.text)


def get_users():
    response = requests.get('http://127.0.0.1:8080/users')
    print(response.text)


def create_advertisement():
    response = requests.post('http://127.0.0.1:8080/advertisement',
                             json={'title': 'good_frog', 'text': 'ddddog', 'author': 1})
    data = response.text
    print(data)


def get_advertisement():
    response = requests.get('http://127.0.0.1:8080/advertisement/1')
    print(response.text)


def get_advertisements():
    response = requests.get('http://127.0.0.1:8080/advertisements')
    print(response.text)


def patch_advertisement():
    response = requests.patch('http://127.0.0.1:8080/advertisement/2',
                              json={'text': 'good_cat'})
    print(response.text)


def delete_advertisement():
    response = requests.delete('http://127.0.0.1:8080/advertisement/4')
    print(response.text)


create_user()
