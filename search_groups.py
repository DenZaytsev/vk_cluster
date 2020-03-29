from access_token import TOKEN
import requests
import regex as re


def write_csv(list_groups: list) -> None:
    with open('groups_id.csv', 'a', encoding='utf-8') as file:
        for group in list_groups:
            if not group['is_closed']:
                clean_name = re.compile('[^a-zA-Zа-яА-Я ]').sub('', group['name'])
                file.write(f"{group['id']};{clean_name}\n")


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
    key_words = [
        'гадание',
        'приворот',
        'ведьма'
    ]
    for key_word in key_words:
        write_csv(get_a_list_of_groups(key_word))


if __name__ == "__main__":
    main()
