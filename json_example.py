import pandas
import requests

url = 'https://reqres.in/api/users?page=2'

# Получаем данные из API 
response = requests.get(url).json()

# Получаем информацию о пользователях
data = response['data']

# Выводим данные о пользователях
for user in data:
    print(user)

# Загружаем данные о пользователях в dataframe
dataframe = pandas.DataFrame.from_records(data)

# Сохраняем данные о пользотелях в формате CSV
dataframe.to_csv('users.csv', index=False)
