import requests
from bs4 import BeautifulSoup


class Book:
    def __init__(self, title, price, rating):
        self.title = title
        self.price = price
        self.rating = rating

    def show(self):
        print(self.title)
        print("Цена:", self.price)
        print("Рейтинг:", self.rating)
        print("---")


class Parser:
    def __init__(self):
        self.books = []

    def get_rating(self, word):
        if word == "One":
            return 1
        elif word == "Two":
            return 2
        elif word == "Three":
            return 3
        elif word == "Four":
            return 4
        elif word == "Five":
            return 5
        else:
            return 0

    def parse_page(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("article", class_="product_pod")

        for card in cards:
            title = card.find("h3").find("a")["title"]
            price = card.find("p", class_="price_color").text
            rating_word = card.find("p", class_="star-rating")["class"][1]
            rating = self.get_rating(rating_word)

            book = Book(title, price, rating)
            self.books.append(book)

    def run(self):
        for i in range(1, 4):
            url = f"https://books.toscrape.com/catalogue/page-{i}.html"
            print("Парсим страницу", i)
            self.parse_page(url)

        print("Всего книг:", len(self.books))
        print()

        for book in self.books:
            book.show()


parser = Parser()
parser.run()
