import requests
from datetime import date, timedelta
import re

def get_dates(days_period):
    if re.compile(r'\d+').search(days_period):
        date_now = date.today()
        delta_week_ago = timedelta(days = int(days_period))
        date_week_ago = date_now - delta_week_ago
        dates = (date_week_ago, date_now)
        return dates
    else:
        print('Введено некоррекное значение, повторите запуск')
        exit()
    
def get_request(top_size, dates):
    query = 'created:{}..{}'.format(dates[0], dates[1])
    search_rules = {'page': '1', 'per_page': str(top_size), 'q': query, 'sort': 'stars', 'order': 'desc'}
    url = 'https://api.github.com/search/repositories'
    request = requests.get(url, params = search_rules)
    return request

def get_trending_repositories(request):
    repo_list_general = request.json()['items']
    repo_list = [(repo['stargazers_count'], repo['owner']['repos_url']) for repo in repo_list_general]        
    return repo_list
    
def print_trending_repositories(repo_list):
    for repo in repo_list:
        print('\nКол-во звезд: {}\nСсылка: {}'.format(repo[0], repo[1]))

if __name__ == '__main__':
    days_period = input('Ведите период (кол-во дней): ')
    dates = get_dates(days_period)
    top_size = 20
    request = get_request(top_size, dates)
    repo_list = get_trending_repositories(request)
    print_trending_repositories(repo_list)