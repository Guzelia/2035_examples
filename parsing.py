import requests
from lxml import html

url = 'https://info.urfu.ru/ru/departures/kafedry/'

# Получение исходного кода страницы
response = requests.get(url)

# Преобразование тела документа в дерево элементов
parsed_body = html.fromstring(response.text)

# Получение всех элементов класса 'course-box'
course_boxes = parsed_body.find_class('course-box')

# Создание пустого списка для последующего добавления кафедр
departments = []

for box in course_boxes:
    # Получение содержания элемента с тегом <a>
    link = box.find('a')
    # Получение содержания элемента с тегом <p>
    text = link.find('p')
    # Добавление названия кафедры в заготовленный список
    departments.append(text.text_content())
