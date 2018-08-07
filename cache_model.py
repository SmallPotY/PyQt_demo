import pickle
import codecs
import os

class DataManagement:
    books = []

    def insert_db(self, bookinfo):
        self.books = self.load()
        for book in self.books:
            if book["isbn"] == bookinfo["isbn"]:
                return -1
        else:
            self.books.append(bookinfo)
            with codecs.open("book.dat", "wb") as f:
                pickle.dump(self.books, f)
            return 1

    def save_db(self, bookinfoes):
        with codecs.open("book.dat", "wb") as f:
            pickle.dump(bookinfoes, f)

    def query_db(self, isbn="", author="", bookname=""):
        self.books = self.load()
        if isbn:
            for i, book in enumerate(self.books):
                if book["isbn"] == isbn:
                    return i
                else:
                    return -1
        if author:
            for i, book in enumerate(self.books):
                if book["author"] == author:
                    return i
                else:
                    return -1
        if bookname:
            for i, book in enumerate(self.books):
                if book["subtitle"] == bookname:
                    return i
                else:
                    return -1

    def load(self):
        pathname = "book.dat"

        if not (os.path.exists(pathname) and os.path.isfile(pathname)):
            with codecs.open("book.dat", "wb") as f:
                pickle.dump(self.books, f)
        with codecs.open("book.dat", "rb") as f:
            books = pickle.load(f)
        return books