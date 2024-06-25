import requests

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'

r = requests.get(URL)

print(r.status_code , r.headers['Date'] , r.request.headers['User-Agent'] , r.request.body , r.encoding , r.text)


