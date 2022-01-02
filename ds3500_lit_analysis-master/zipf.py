import collections
import numpy as np
from matplotlib import pyplot as plt

def generate_zipf_table(text, top):
    '''
    Create a list of dictionaries containing the  most frequent words with their frequencies (and other data)
    params: 'text': body of text, 'top': most frequent words
    returns: dictionaries containing most frequent words (keys) and their frequencies (values)
    '''

    text = remove_punctuation(text)

    text = text.lower()

    word_frequencies = top_word_counts(text, top)

    zipf_table = create_zipfs_table(word_frequencies)

    return zipf_table


def remove_punctuation(text):
    '''
    Removes punctuation characters
    params: 'text': body of text
    returns: modifed text with punctuation removed
    '''

    remove_chars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"

    translated = str.maketrans('', '', remove_chars)

    return text.translate(translated)


def top_word_counts(text, top):
    '''
    List of tuples containing the most frequent words and their frequencies (descending order)
    params: 'text': body of text, 'top': most frequent words
    returns: list of tuples (word: frequency)
    '''

    words = text.split()

    word_frequencies = collections.Counter(words)

    top_word_counts = word_frequencies.most_common(top)

    return top_word_counts


def create_zipfs_table(frequencies):
    '''
    Inserts list created by top_word_counts into a list of dictionaries
    params: 'frequencies': word frequencies
    returns: list of dictionaries
    '''

    zipf_table = []

    top_frequency = frequencies[0][1]

    for index, item in enumerate(frequencies, start=1):

        relative_frequency = '1/{}'.format(index)
        zipf_frequency = top_frequency * (1 / index)
        difference_actual = item[1] - zipf_frequency
        difference_percent = (item[1] / zipf_frequency) * 100

        zipf_table.append({'word': item[0],
                           'actual_frequency': item[1],
                           'relative_frequency': relative_frequency,
                           'zipf_frequency': zipf_frequency,
                           'difference_actual': difference_actual,
                           'difference_percent': difference_percent})

    return zipf_table


def print_zipf_table(zipf_table):
    '''
    Prints the table formatted list created by generate_zipf_table (with column headings)
    params: 'zipf_table': table of word rank & frequency distribution
    returns: terminal shell output of zipf analysis (in table format)
    '''

    print('|Rank|    Word    |Actual Freq | Zipf Frac  | Zipf Freq  |Actual Diff |Pct Diff|')


    format_string = '|{:4}|{:12}|{:12.0f}|{:>12}|{:12.2f}|{:12.2f}|{:7.2f}%|'
    word_ranks = []
    word_frequencies = []
    for index, item in enumerate(zipf_table, start=1):
        word_ranks.append(index)
        word_frequencies.append(item['actual_frequency'])
        print(format_string.format(index,
                                   item['word'],
                                   item['actual_frequency'],
                                   item['relative_frequency'],
                                   item['zipf_frequency'],
                                   item['difference_actual'],
                                   item['difference_percent']))
    return word_ranks, word_frequencies

def zipf_grapher(x, y):
    """
    Graphs the Zipfian data in a line graph
    params: 'x': x axis data, 'y': y axis data
    returns: line graph
    """

    # Creating figure and axes
    
    plt.plot(x, y)
    plt.title("Zipf's law: Dracula")
    plt.xlabel('Word Ranks')
    plt.ylabel('Word Frequencies')
    plt.show()

    return