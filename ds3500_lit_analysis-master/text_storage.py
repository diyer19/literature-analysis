from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_etexts
from gutenberg.query import get_metadata
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import re
from elasticsearch import Elasticsearch
from gutenberg.acquire import get_metadata_cache
from gutenberg.query import get_etexts
from gutenberg.query import get_metadata





def retrieve_clean_text(num):
    """retrieves and cleans the text from the Gutenberg library
    params: index number of the desired book from the Gutenberg library
    returns: string representation of the text """
    text = strip_headers(load_etext(num)).strip()
    text = text.replace('\n', '')
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace(":", "")
    text = text.replace("\"", "")
    text = text.replace("!", "")
    text = text.replace("â€œ", "")
    text = text.replace("â€˜", "")
    text = text.replace("*", "")
    text = text.replace("'", "")
    text = text.replace("'", "")
    text = text.replace('"', "")
    return text


def data_storage(num):
    """stores text from gutenberg library in elastic search database
    params: takes in a number, which serves as an index
    for retrieving the text from the Gutenberg library
    returns: string of the text"""
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}], timeout=30)
    doc = {
        'text': retrieve_clean_text(num)
    }
    # indexing a document
    res = es.index(index="books", id=num, body=doc)

    #getting a document
    res = es.get(index="books", id=num)
    text_string = res['_source']
    return text_string["text"]






