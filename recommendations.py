from scipy.spatial import distance
from scipy.stats import pearsonr

# Задаем оценки пользователей
ivan = (5, 7, 2, 3)
petr = (6, 7, 4, 4)
sergey = (9, 4, 8, 8)
vasiliy = (10, 4, 9, 7)

# Вычисляем евклидово расстояние для оценок Ивана и Петра
dst_1 = distance.euclidean(ivan, petr)

# Вычисляем евклидово расстояние для оценок Ивана и Сергея
dst_2 = distance.euclidean(ivan, sergey)

# Вычисляем евклидово расстояние для оценок Ивана и Василия
dst_3 = distance.euclidean(ivan, vasiliy)

print(dst_1, dst_2, dst_3)

# Вычисляем коэффициент корреляции Пирсона Ивана и Петра
pearson_1 = pearsonr(ivan, petr)[0]

# Вычисляем коэффициент корреляции Пирсона Ивана и Сергея
pearson_2 = pearsonr(ivan, sergey)[0]

# Вычисляем коэффициент корреляции Пирсона Ивана и Василия
pearson_3 = pearsonr(ivan, vasiliy)[0]

print(pearson_1, pearson_2, pearson_3)
