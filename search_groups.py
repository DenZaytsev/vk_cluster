from access_token import TOKEN
import requests
from time import sleep


def write_csv(list_groups: list) -> None:
    """Записывает id групп в файл (они могут повторяться)"""
    with open('groups_id.csv', 'a', encoding='utf-8') as file:
        for group in list_groups:
            if not group['is_closed']:
                file.write(f"{group['id']}\n")


def get_a_list_of_groups(key_word: str) -> list:
    """по ключевому слову возвращает список групп"""
    params = {
        'q': key_word,
        'access_token': TOKEN,
        'v': 5.103,
        'type': 'group',
        'sort': 0,
        "count": 1000,
        'offset': 0
    }
    response = requests.get(f'https://api.vk.com/method/groups.search', params)
    print(response.status_code)
    list_groups = response.json()['response']['items']
    return list_groups


def main():
    key_words = [
        "Путин",
        "политика",
        "протест",
        "революция",
        "россия",
        "полика новости",
        "путин новости",
        "путин бог",
        "путин госсовет",
        "политика новости",
        "политика россии",
        "политика сегодня",
        "политика в россии",
        'Единая Россия',
        'КПРФ',
        'ЛДПР',
        'Справедливая Россия'
        'Коммунисты России',
        'Яблоко',
        'Российская партия пенсионеров за социальную справедливость',
        'Родина',
        'Партия Роста',
        'Зеленые',
        'ПАРНАС',
        'Патриоты России',
        'Гражданская платформа и Гражданская сила',
        "навальный митинг",
        "навальный новости"
    ]
    for key_word in key_words:
        sleep(1)
        write_csv(get_a_list_of_groups(key_word))


if __name__ == "__main__":
    main()
