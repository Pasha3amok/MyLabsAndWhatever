# Индивидуальное творческое задание
#Полезная программа для менеджера банка
import sys	#работа с файлами
import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
from prettytable import PrettyTable

def add_menu():
        print()
        input("Чтобы продолжить нажмите Enter ➤ ")
        general()

def personal_data():
    print()
    print("-" * 90)
    print(""" 
      | Программа была сделана студентом ДонНУ, Гуменчуком Павлом Сергеевичем, |
    
      | группа КН122-Б, в 2022-м году, специально для менеджеров банка Украины. |
    
      | Контакты разработчика: humenchuk.p@donnu.edu.ua (поддержка с 9 до 22 )  |
                
                """)
    print("-" * 90)
    add_menu()

def gen_currency():
    class Currency:
        # Ссылка на курсы
        DOLLAR_UAH = 'https://www.google.com/search?q=1+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B3%D1%80%D0%BD&oq=1+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B3%D1%80%D0%BD&aqs=chrome..69i57.9948j0j15&sourceid=chrome&ie=UTF-8'
        EURO_UAH = 'https://www.google.com/search?q=1+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%BD&sxsrf=ALiCzsa2O9j7BY8ZoaaPQzCpZUzrZAjpPw%3A1651151565181&ei=zZJqYpjNCsGIrwTA17SgDQ&ved=0ahUKEwjY54z06rb3AhVBxIsKHcArDdQQ4dUDCA4&uact=5&oq=1+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%BD&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggI6BwgjELADECc6BwgAEEcQsAM6BggAEAcQHjoECAAQDToJCAAQDRBGEIICSgQIQRgASgQIRhgAUP8GWME0YOo2aAJwAHgAgAGRAYgByweSAQMwLjeYAQCgAQHIAQnAAQE&sclient=gws-wiz'
        GBP_UAH = 'https://www.google.com/search?q=1+%D1%84%D1%83%D0%BD%D1%82+%D1%81%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2+%D0%BA+%D0%B3%D1%80%D0%BD&sxsrf=ALiCzsYRKtB-9I-OPARmEFXQwGa80oMA0Q%3A1651158268146&ei=_KxqYvq8CO2trgTNyKGgAg&oq=1++%D0%BA+%D0%B3%D1%80%D0%BD&gs_lcp=Cgdnd3Mtd2l6EAEYAzIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeOgcIABBHELADOgcIIxCwAhAnSgQIQRgASgQIRhgAULUIWOYPYOIjaAFwAXgAgAHgAYgBsAWSAQUwLjMuMZgBAKABAcgBCMABAQ&sclient=gws-wiz'
        # Заголовки для передачи вместе с URL
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}

        current_converted_price = 0
        difference = 5 # Разница после которой будет отправлено сообщение на почту

        def __init__(self):
            # Установка курса валюты при создании объекта
            self.current_converted_price = float(self.get_currency_price(self.DOLLAR_UAH).replace(",", "."))
            self.current_converted_price = float(self.get_currency_price(self.EURO_UAH).replace(",", "."))
            self.current_converted_price = float(self.get_currency_price(self.GBP_UAH).replace(",", "."))

        # Метод для получения курса валюты
        def get_currency_price(self, x):
            self.x = x
            
            # Парсим всю страницу
            full_page = requests.get(self.x, headers=self.headers)

            # Разбираем через BeautifulSoup
            soup = BeautifulSoup(full_page.content, 'html.parser')

            # Получаем нужное для нас значение и возвращаем его
            convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
            return convert[0].text

        
        # Проверка изменения валюты
        def check_currency(self):
            print("""
            [1] Получить данные об валюте 
            [0] Выйти в главное меню
            """)
            choice = int(input("➤ "))
            if choice == 1:
                file = open('currency_rate.txt', 'w', encoding='utf-8')
                sys.stdout = file
                currency = float(self.get_currency_price(self.DOLLAR_UAH).replace(",", "."))
                print('______Курс на сегодня________')
                print("Доллар = " + str(currency),'грн')
                currency2 = float(self.get_currency_price(self.EURO_UAH).replace(",", "."))
                print("Евро = " + str(currency2),'грн')
                currency3 = float(self.get_currency_price(self.GBP_UAH).replace(",", "."))
                print("Фунт стерлингов = " + str(currency3),'грн')
                file.close()

            if choice == 0:
                sys.stdout = sys.__stdout__
                general()
                
            sys.stdout = sys.__stdout__
            
            self.check_currency()
    # Создание объекта и вызов метода
    currency = Currency()
    currency.check_currency()


def general():
    print("""
    ╔═══════════════════════════════════════════════╗
    ║         Инструмент Менеджера банка            ║
    ╠═══════════════════════════════════════════════╣
    ║ [1] Отслеживание курса валют к гривне         ║
    ║ [2] Покупка и продажа валют                   ║
    ║ [3]                                           ║
    ║ [4] Расчёт процентов по кредиту               ║
    ║ [5]                                           ║
    ║ [6] Расчёт сложных и простых процентов        ║
    ║ [7] О программе                               ║
    ║ [0] Выход                                     ║
    ╚═══════════════════════════════════════════════╝""")


    ans = int(input("Виберите пункт меню ⟹  "))
    if ans == 1:
        gen_currency()  
    if ans == 2:  
        schedule()
    if ans == 3:  
        literature()
    if ans == 4:  
        translator()
    if ans == 5:  
        tutor()
    if ans == 6:  
        game()
    if ans == 7:  personal_data()
    if ans == 0:  
        quit()
    general()
general()
