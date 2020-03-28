from access_token import TOKEN
import requests


def main():
    r = requests.get(f'https://api.vk.com/method/groups.search', params={'q': 'qwd', 'access_token': TOKEN, 'v': 5.103})
    print(r.json())


if __name__ == "__main__":
    main()