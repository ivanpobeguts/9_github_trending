import requests
from datetime import timedelta, date


def get_trending_repositories(search_period, top_size=20):
    base_url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'created:>={}'.format(search_period),
        'sort': 'stars',
        'order': 'desc',
    }
    response = requests.get(base_url, params=params)
    return response.json()['items'][:top_size]


def get_open_issues_amount(repo_full_name):
    base_url = 'https://api.github.com/repos/{}/issues'.format(repo_full_name)
    response = requests.get(base_url)
    return len(response.json())


def get_search_period(delta=7):
    return date.today() - timedelta(delta)


def print_search_results(repos):
    for repo in repos:
        full_name = repo['full_name']
        url = repo['html_url']
        stars_amount = repo['stargazers_count']
        issues = get_open_issues_amount(full_name)
        print(
            'url: ', url,
            ', stars: ', stars_amount,
            ', issues: ', issues,
            sep=''
        )


if __name__ == '__main__':
    search_period = get_search_period()
    try:
        top_repos = get_trending_repositories(search_period)
        print_search_results(top_repos)
    except KeyError:
        print('Query limit exceeded. Try in a minute')
