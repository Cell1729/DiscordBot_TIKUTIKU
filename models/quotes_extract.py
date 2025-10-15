# models/quotes_extract.py
from models.models import Quotes
import random

class RandomQuoteExtractor:
    def __init__(self, session):
        self.session = session

    def get_random_quote(self):
        quotes = self.session.query(Quotes).all()
        if not quotes:
            return None, None
        quote_obj = random.choice(quotes)
        return quote_obj.quote, getattr(quote_obj, 'url', None)
