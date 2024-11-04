from book import Book

class TextBook(Book):
    def get_info(self):
        return f"{self.title} ({self.author}, {self.year}, {self.pages} stron -> Podręcznik)."

    def read(self):
        print(f'przeczytano podręcznik {self.title}. Zawiera dodtakowe materiały!')
