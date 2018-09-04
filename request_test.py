import requests


url = 'http://120.77.182.38/blog/'

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
