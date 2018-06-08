import time
from selenium import webdriver
from bs4 import BeautifulSoup



def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')  # Запуск браузера в режиме инкогнито
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.google.ru/")
    driver.implicitly_wait(10)
    print('Тест кейс № 1 Тестовое задание"')
    text = 'habrahabr'
# Шаг 1
    driver.find_element_by_name('q').send_keys(text)
    print('Ввод habrahabr произведен')
    driver.find_element_by_name('btnK').click()
    print('Клик кнопки "Поиск в Google" произведен')
    time.sleep(1)
# Шаг 2
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find_all('cite')
    for ad in ads:
        url = ad.text
        if 'habrahabr.ru' in url:
            urlh = url
    print('Найдена ссылка содержащая habrahabr.ru :  ', urlh)
    driver.get(urlh)
    time.sleep(3)
# Шаг 3
    driver.find_element_by_xpath('.//a[text()="Песочница"]').click()
    print('Клик "Песочница" произведен')
    time.sleep(2)
# Шаг 4
    driver.find_element_by_xpath('.//a[text()="2"]').click()
    print('Клик 2 второй страницы "Песочница" произведен')
    time.sleep(3)


if __name__ == '__main__':
    main()