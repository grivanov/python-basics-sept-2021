needed_book = input()
checked_books = 0
book_found = False

while not(book_found):
    check_book = input()

    if check_book == "No More Books":
        break
    elif check_book == needed_book:
        book_found = True
        break
    else:
        checked_books += 1

if book_found:
    print(f"You checked {checked_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")
