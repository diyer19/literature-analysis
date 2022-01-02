from nltk.tokenize import wordpunct_tokenize
from text_storage import data_storage
from matplotlib import pyplot as plt

# Uses Sherlock as test book
test_book = data_storage(48320)

# Uses Pride and Prejudice as test book
test_book_two = data_storage(1342)

def heaps_analyzer(tester):
    """
    Tokenizes and enumerates through  length of a document. Counts list of unique words for each iteration.
    params: 'tester': text data being evaluated
    returns: 'doc_len': list of iterations through a document, 'distinct_words': list of distinct words for each iteration
    """
    tokens = wordpunct_tokenize(tester)
    distinct_word = set()
    doc_len = []
    distinct_words = []
    for i, token in enumerate(tokens):
        distinct_word.add(token)
        doc_len.append(i)
        distinct_words.append(len(distinct_word))
    return doc_len, distinct_words


def heaps_grapher(book):
    """Graphs the Heapsian data in a line graph
    params: 'x': x axis data, 'y': y axis data
    returns: line graph
    """

    book_length_x = heaps_analyzer(book)[0]
    num_unique_words_y = heaps_analyzer(book)[1]

    # Creating figure and axes
    
    plt.plot(book_length_x, num_unique_words_y)
    plt.title("Heaps' law: Pride and Prejudice")
    plt.xlabel('Length of Document (total # of words)')
    plt.ylabel('Number of Unique Words')
    plt.show()

    return

heaps_grapher(test_book_two)