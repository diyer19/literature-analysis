from nltk.corpus.reader.chasen import test
import zipf
from text_storage import data_storage
import numpy as np

def main():

    print("-----------------------")
    print("| Zipf's Law Analysis |")
    print("-----------------------\n")

    # Uses Alice in Wonderland as test book
    test_book = data_storage(11)

    
    zipf_table = zipf.generate_zipf_table(test_book, 135)

    word_ranks_x, word_frequencies_y = zipf.print_zipf_table(zipf_table)

    zipf.zipf_grapher(word_ranks_x, word_frequencies_y)



main()