import requests
from datetime import date, timedelta

def get_trending_repositories(top_size):
    date_now = date.today()
    delta_week_ago = timedelta(days=7)
    date_week_ago = date_now - delta_week_ago
    url = ('https://api.github.com/search/repositories?q=language:python+created:{}..{}&sort=stars&order=desc').format(date_week_ago, date_now)
    result = requests.get(url)
    repo_list_general = result.json()['items']
    repo_count = 0
    repo_list  = []
    for repo in repo_list_general:
        repo_count += 1
        if repo_count <= top_size:
            repo_star = str(repo['stargazers_count'])
            repo_url  = repo['owner']['repos_url']
            repo_list.append((repo_star, repo_url))
        else:
            break
    return repo_list
    
def print_trending_repositories(repo_list):
    for repo in repo_list:
        print(' - '.join(item for item in repo))

if __name__ == '__main__':
    top_size = 20
    repo_list = get_trending_repositories(top_size)
    print_trending_repositories(repo_list)