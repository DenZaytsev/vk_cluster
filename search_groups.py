from access_token import TOKEN
import requests
import json


def write_csv_from_json(response: json) -> None:
    """"""
    list_group = response['response']['items']


def main():
    key_word = 'a'

    params = {
        'q': key_word,
        'access_token': TOKEN,
        'v': 5.103,
        'type': 'group',
        'sort': 3,
        "count": 1000,
        'offset': 0
    }

    re = requests.get(f'https://api.vk.com/method/groups.search', params)

    write_csv_from_json(re.json())


if __name__ == "__main__":
    main()
