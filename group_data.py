import requests
from access_token import TOKEN
import regex as re


def write_group_info(response):
    with open('content.csv', 'a', encoding='utf-8') as file:
        try:
            name = response["groups"][0]['name']
            id_group = response["groups"][0]['id']
            description = response["groups"][0]["description"]

            for post_text in response["items"]:
                description += post_text['text']

            clean_description = re.compile('[^a-zA-Zа-яА-Я]').sub('', description)
            clean_name = re.compile('[^a-zA-Zа-яА-Я ]').sub('', name)
            file.write(f"{id_group};{clean_name};{clean_description}\n")
        except Exception:
            pass


def get_wall(group_id: str):
    params = {
        'access_token': TOKEN,
        'v': 5.103,
        'owner_id': f"-{group_id}",
        'count': 10,
        'extended': 1,
        'fields': 'description'
    }
    response = requests.get(f'https://api.vk.com/method/wall.get', params)
    print(response.status_code, group_id)
    try:
        return response.json()["response"]
    except Exception:
        pass


def main() -> None:
    """5000 запросов в день """
    with open("unique_groups_id.csv") as file:
        for line in file:
            line = line.strip().split(',')
            write_group_info(get_wall(line[1]))


if __name__ == "__main__":
    main()
