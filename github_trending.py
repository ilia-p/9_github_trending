import requests
from datetime import date, timedelta

def get_trending_repositories(top_size):
    date_now = date.today()
    delta_week_ago = timedelta(days=days_period)
    date_week_ago = date_now - delta_week_ago
    query = ('created:{}..{}').format(date_week_ago, date_now)
    search_rules = {'page': '1', 'per_page': str(top_size), 'q': query, 'sort': 'stars', 'order': 'desc'}
    url = 'https://api.github.com/search/repositories'
    result = requests.get(url, params = search_rules)
    repo_list_general = result.json()['items']
    repo_list = [(str(repo['stargazers_count']), repo['owner']['repos_url']) for repo in repo_list_general]        
    return repo_list
    
def print_trending_repositories(repo_list):
    for repo in repo_list:
        print(' - '.join(item for item in repo))

if __name__ == '__main__':
    top_size = 20
    days_period = int(input('Ведите период (кол-во дней): '))
    repo_list = get_trending_repositories(top_size)
    print_trending_repositories(repo_list)