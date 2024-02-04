from urllib.request import urlopen
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://jsonplaceholder.typicode.com/albums"
response = urlopen(url)
data_json = json.loads(response.read())

validation_data = [{'quidem molestiae enim'}, {'sunt qui excepturi placeat culpa'},
                   {'omnis laborum odio'}, {'non esse culpa molestiae omnis sed optio'},
                   {'eaque aut omnis '}]
# Iterate through the elements in data_json to check if they exist in validation_data
for elemento in data_json:
    if elemento['id'] < len(validation_data):
        if elemento['title'] in str(validation_data):
            print(f"El título {elemento['title']}, Tiene el valor deseado.")
        else:
            print(f"El título {elemento['title']}, No Tiene el valor deseado.")
    else:
        break
