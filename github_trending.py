import requests
from datetime import timedelta, date


def get_trending_repositories(search_period, top_size=20):
    base_url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'created:{}'.format(search_period),
        'sort': 'stars',
        'order': 'desc',
    }
    r = requests.get(base_url, params=params)
    return r.json()['items'][:top_size]


def get_open_issues_amount(repo_full_name):
    base_url = 'https://api.github.com/repos/{}/issues'.format(repo_full_name)
    r = requests.get(base_url)
    return len(r.json())


def get_search_period(delta=7):
    return date.today() - timedelta(delta)


if __name__ == '__main__':
    search_period = get_search_period()
    try:
        top_repos = get_trending_repositories(search_period)
        for repo in top_repos:
            print(repo['full_name'], ': ', repo['stargazers_count'], sep='')
    except KeyError:
        print('Query limit exceeded. Try in a minute')
