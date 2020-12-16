from bs4 import BeautifulSoup
import re
import logging

from locators.all_books_page import AllBooksPageLocators
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.all_book_page')

class AllBooksPage: 

    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup html parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')
    
    @property
    def books(self):
        logger.debug('Finding all books.')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages availble.')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        pattern = r'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages



