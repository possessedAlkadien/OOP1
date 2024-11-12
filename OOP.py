import requests
from bs4 import BeautifulSoup #извлечение данных с HTML
import webbrowser

#определение браузера для поиска
urL='https://www.google.com'
chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))




def main():
    Ques = str(input("Введите запрос:"))
    url = f"https://en.wikipedia.org/w/index.php?search={Ques}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    result = []
    for i in soup.find_all('div', class_='mw-search-result-heading'):#поиск всех элементов на странице, представляющих собой заголовки статей поисковых результатов
        link = i.find('a')#поиск элементов <a для получения заголовка статьи и URL
        title = link.get_text()#извлечение заголовка
        url = "https://en.wikipedia.org" + link.get('href')#составление полного адреса URL
        result.append((title, url))

    if result:
        print("\nРезультаты поиска:")
        for index, (title, url) in enumerate(result):
            print(f"{index + 1}. {title}")
        choice = int(input("Выберите номер статьи, чтобы открыть её (0 для выхода): "))
        if choice > 0 and choice <= len(result):
                url = result[choice - 1][1]
                webbrowser.open(url)
        elif choice == 0:
            print("Выход из программы.")
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()

