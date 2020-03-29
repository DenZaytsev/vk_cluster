import requests
from access_token import TOKEN


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
    print(response.status_code)
    print(response.json())


def main() -> None:
    get_wall('1776361')


if __name__ == "__main__":
    main()
