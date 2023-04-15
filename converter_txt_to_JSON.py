import json


with open('data/1212323123132.txt', 'r') as file:
    content = file.read()
    data = json.loads(content)


with open('data/readable_eq_data_30_days_m4.5_14.04.2023.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Конвертация завершена!")
