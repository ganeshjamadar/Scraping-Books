from app import books
import logging

logger = logging.getLogger('scraping.menu')


USER_CHOICE = '''
Enter one of the following
    - 'l' to list all books
    - 'b' to look at 5-star books
    - 'c' to look at cheapest books
    - 'n' to just get next avilable book on catalogue
    - 'q' to exit

Enter your choice: '''

def list_all_books():
    logger.info('Finding all books.......')
    for book in books:
        print(book)

def print_best_books():
    logger.info('Finding best books.......')
    best_books = sorted(books, key= lambda x : (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)

def print_cheapest_books():
    logger.info('Finding cheap books.......')
    cheap_books = sorted(books, key= lambda x : (x.price))[:10]
    for book in cheap_books:
        print(book)

books_generator = (x for x in books)

def get_next_book():
    logger.info('Getting next book from the genrator of all books.......')
    print(next(books_generator))

user_choices = {
    'l': list_all_books,
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('l','b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command,')
        user_input = input(USER_CHOICE)

menu()
        