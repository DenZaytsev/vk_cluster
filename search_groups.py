from access_token import TOKEN
import requests
import json


def write_csv(list_groups: list) -> None:
    """"""
    pass


def get_a_list_of_groups(key_word: str) -> list:
    """по ключевому слову возвращает список групп"""
    params = {
        'q': key_word,
        'access_token': TOKEN,
        'v': 5.103,
        'type': 'group',
        'sort': 3,
        "count": 1000,
        'offset': 0
    }

    response = requests.get(f'https://api.vk.com/method/groups.search', params)
    print(response.status_code)
    list_groups = response.json()['response']['items']

    return list_groups


def main():
    get_a_list_of_groups("sdf")


if __name__ == "__main__":
    main()
