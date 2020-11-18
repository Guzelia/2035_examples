import string

from nltk import sent_tokenize, word_tokenize
import pymorphy2

# Задаем морфологический анализатор
morph = pymorphy2.MorphAnalyzer()

# Загрузка текста из файла
with open('text.txt', 'r') as f:
    text = f.read()

# Разделение текста на предложения
tokenized_sentences = [sent for sent in sent_tokenize(text)]

# Инициализация списка для нормализованных предложений
normalized_sentences = []

# Разделение слов в предложениях
for sentence in tokenized_sentences:
    words = [word.lower() for word in word_tokenize(sentence) if word not in string.punctuation]
    
    # Инициализация списка для нормализованных слов
    normalized_words = []

    # Приведение к нормальной форме
    for word in words:
        normalized_words.append(morph.parse(word)[0].normal_form)
    
    # Добавление нормализованных слов в список нормализованных предложений
    normalized_sentences.append(normalized_words)
