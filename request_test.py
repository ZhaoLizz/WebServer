import requests


url = 'http://127.0.0.1:8000'

session = requests.Session()
r = session.get(url)
# session.headers.update({
#     'Referer': url,
#     'X-CSRFToken': r.cookies['csrftoken'],
# })

r = requests.get(url)
print(r.status_code)
print(r.url)
# print(r.text) # html
print(r.encoding)
print(r.request)
