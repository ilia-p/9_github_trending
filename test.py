import requests
from datetime import date, timedelta

date_now = date.today()
delta_week_ago = timedelta(days=7)
date_week_ago = date_now - delta_week_ago
url = ('https://api.github.com/search/repositories?q=language:python+created:{}..{}&sort=stars&order=desc').format(date_week_ago, date_now)
result = requests.get(url)
if result.status_code == 200:
   mylist = result.json()['items']
else:
    print('Smth went wrong')
repo_number = 20 # подается на вход функции
repo_count  = 0
for item in mylist:
    repo_count += 1
    if repo_count <= repo_number:
        print(item['stargazers_count'])
        print(item['url'])
    else:
        break
   
    