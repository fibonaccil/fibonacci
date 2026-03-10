import json
import os

FILE_NAME = "library.json"

def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book(books):
    title = input("Название: ")
    author = input("Автор: ")
    genre = input("Жанр: ")
    year = input("Год: ")
    desc = input("Описание: ")
    books.append({
        "title": title, "author": author, "genre": genre,
        "year": year, "description": desc,
        "status": "Не прочитана", "favorite": False
    })
    print("Добавлено!")

def view_books(books):
    if not books:
        print("Пусто")
        return
    for i, b in enumerate(books, 1):
        fav = "★" if b["favorite"] else "☆"
        print(f"{i}. {fav} {b['title']} - {b['author']} ({b['year']}) - {b['status']}")

def main():
    books = load_books()
    while True:
        print("\n1. Добавить\n2. Все книги\n3. В избранное\n4. Статус\n5. Избранное\n6. Удалить\n0. Выход")
        c = input("Выбор: ")
        if c == "1": add_book(books)
        elif c == "2": view_books(books)
        elif c == "3":
            view_books(books)
            i = int(input("Номер: ")) - 1
            if 0 <= i < len(books): books[i]["favorite"] = True
        elif c == "4":
            view_books(books)
            i = int(input("Номер: ")) - 1
            if 0 <= i < len(books):
                books[i]["status"] = "Прочитана" if books[i]["status"] == "Не прочитана" else "Не прочитана"
        elif c == "5":
            favs = [b for b in books if b["favorite"]]
            for i, b in enumerate(favs, 1):
                print(f"{i}. {b['title']}")
        elif c == "6":
            view_books(books)
            i = int(input("Номер: ")) - 1
            if 0 <= i < len(books):
                del books[i]
        elif c == "0":
            save_books(books)
            break
        save_books(books)

if __name__ == "__main__":
    main()
