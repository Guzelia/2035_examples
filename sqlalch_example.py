import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Создаем соединение с БД
engine = create_engine('sqlite:///database.db', echo=True)

# Создаем базовый класс
Base = declarative_base()


# Описываем структуру таблицы
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Integer)


# Создаем таблицу
Base.metadata.create_all(engine)

# Создаем экземляр фабрики сессий
Session = sessionmaker(bind=engine)

# Задаем сессию
session = Session()

# Создаем первый продукт
apple = Product(name='apple', amount=3)

# Добавляем первый продукт
session.add(apple)

# Создаем следующие продукты
orange = Product(name='orange', amount=6)
grape = Product(name='grape', amount=5)

# Добавляем их к сесссии
session.add_all([orange, grape])

# Извлекаем продукт с наименование "apple"
product = session.query(Product).filter_by(name='apple').first()
# Меняем значение
product.amount = 12

print(product.amount)

# Получаем все продукты, отсортированные в порядке возрастания id
query = session.query(Product).order_by(Product.id)
# Выводим наименования продуктов
for product in query:
    print(product.name)


# Отправляем изменения, сделанные во время сессии
session.commit()

# Экспортируем все данные в CSV
table_df = pd.read_sql_table('product', con=engine)
table_df.to_csv('products.csv', index=False)

# Импортируем таблицу с данными из CSV
api_users_df = pd.read_csv('users.csv')
api_users_df.to_sql(con=engine, name='api_user')

# Закрываем сессию
session.close()
