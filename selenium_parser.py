import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumParser:
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/macbookair/Downloads/chromedriver')
        self.driver.maximize_window()

    def load_all_news(self):
        self.driver.get('https://info.urfu.ru/ru/novosti/')
        while True:
            try:
                self.scroll_and_click('span.text')
            except:
                break

    def scroll_and_click(self, selector):
        element = self.driver.find_element_by_css_selector(selector)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()
        time.sleep(0.3)

    def save_news(self):
        self.load_all_news()

        divs = self.driver.find_elements_by_class_name('div.news-item')

        rows = []

        for div in divs:
            # Разделяем данные по знаку переноса
            splited_text = div.text.split('\n')
            rows.append([splited_text[0], splited_text[1], splited_text[2][2:]])

        dataframe = pd.DataFrame(rows, columns=['date', 'title', 'description'])
        dataframe.to_csv('info_news.csv')


if __name__ == '__main__':
    parser = SeleniumParser()
    parser.save_news()
