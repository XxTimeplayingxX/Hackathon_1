
import requests

resp = requests.get('https://jsonplaceholder.typicode.com/posts')



print(type(resp))


print(resp.json())

print(resp.status_code)

