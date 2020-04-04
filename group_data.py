import requests
from access_token import TOKEN
import regex as re


def write_group_info(response):
    with open('content.csv', 'a', encoding='utf-8') as file:
        try:
            name = response["groups"][0]['name']
            id_group = response["groups"][0]['id']
            group_content = response["groups"][0]["description"]

            for post_text in response["items"]:
                group_content += post_text['text']

            clean_group_content = re.compile('[^a-zA-Zа-яА-Я]').sub('', group_content)
            clean_name = re.compile('[^a-zA-Zа-яА-Я ]').sub('', name)
            file.write(f"{id_group};{clean_name};{clean_group_content}\n")
        except Exception as e:
            print(f"Что-то пошло не так: {e.__class__}")


def get_wall(group_id: str):
    params = {
        'access_token': TOKEN,
        'v': 5.103,
        'owner_id': f"-{group_id}",
        'count': 100,
        'extended': 1,
        'fields': 'description'
    }
    response = requests.get(f'https://api.vk.com/method/wall.get', params)
    print(group_id, end="\t")
    try:
        return response.json()["response"]
    except Exception as e:
        print(f"Что-то пошло не так: {e.__class__}")


def main() -> None:
    """5000 запросов в день """
    counter = 0
    with open("./data/unique_groups_id.csv") as file:
        for line in file:
            line = line.strip().split(',')
            write_group_info(get_wall(line[1]))
            counter += 1
            print(f"{(1/50) * counter} %")
            if counter >= 5000:
                break


if __name__ == "__main__":
    main()
