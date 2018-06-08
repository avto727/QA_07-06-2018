import time
from selenium import webdriver




def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')  # Запуск браузера в режиме инкогнито
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://qa-test.expsys.org/")
    driver.implicitly_wait(10)
    print('Запуск Тест кейс № 1 Дополнительное задание"')
    mail = 'avto727@bk.ru'
    name = 'Андрей'
    text = 'Тестирование формы отправки сообщений'
    # Шаг 1
    driver.find_element_by_id('someid').send_keys(name)
    print('Ввод имени произведен')
    time.sleep(1)
    # Шаг 2
    driver.find_element_by_id('feedbackform-email').send_keys(mail)
    print('Ввод e-mail произведен')
    time.sleep(1)
    # Шаг 3
    driver.find_element_by_id('feedbackform-message').send_keys(text)
    print('Ввод сообщения произведен')
    # Шаг 4
    #     Ручками вводим капчу
    print('Ручками вводим капчу')
    time.sleep(15)
    # Шаг 5
    driver.find_element_by_name('contact-button').click()
    print('Клик кнопки Submit произведен')
# Ждем отклика, примерно минуту  + 30 секунд видим рузультат )
    time.sleep(90)


if __name__ == '__main__':
    main()