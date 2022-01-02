import collections
import pandas as pd
import plotly.express as px
from text_storage import data_storage
from text_storage import retrieve_clean_text
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from wordcloud import STOPWORDS
from most_common import most_common_one_book

list_of_horror_words = ["horror", "blood", "murder",
                        "fright", "fear", "panic",
                        "tragedy","dread", "frighten",
                        "fearful", "hysteria", "acrid", "dark",
                        "foul", "black", "trembling", "aghast", "scream", "knife", "night", "dead", "terror"]

list_of_romance_words = ["love", "kiss", "embrace", "flower", "eyes",
                         "behold", "desire", "courtship", "romance", "darling",
                         "dearest", "beautiful", "betrothal", "cheeks", "flustered", "passion", "heart",
                         "engagement", "marriage", "vow", "ring", "elope", "smitten", "entranced", "lust", "dowry"]

list_of_christmas_words = ["christmas", "joy", "snow", "warmth", "santa",
                           "giving", "winter", "merry", "cold", "frigid", "jesus", "fire",
                           "gift", "jolly"]

list_of_mystery_words = ["death", "murder", "missing", "blood", "crime",
                         "stolen", "mystery", "deduce", "inspector", "detective", "guns",
                         "evidence", "fingerprints", "suspect", "interrogation", "solve",
                         "kidnap", "stab", "clue", "perpetrator"]

def theme_words(num,list_of_thematic_words):
    """ params: the index of the desired book from the Gutenberg library and
    a list of thematic or genre specific words.
    returns: a dataframe consisting of
    the genre-specific words present in the book """

    word_counter = most_common_one_book(num)

    list_of_theme_words_present = []
    for word, count in word_counter.items():
        if word in list_of_thematic_words:
            tuple1 = (word, count)
            list_of_theme_words_present.append(tuple1)

    df = pd.DataFrame(list_of_theme_words_present, columns=['Word', 'Count'])
    df["Count"] = df["Count"] /df["Count"].abs().max()
    return df


def graph_theme_words(books, list_of_thematic_words):
    """ params: a list of the indexes of the books from the Gutenberg library and
    a list of thematic or genre specific words.
    returns: a graph of the normalized amount of words
     from the given list of genre specific words that are present in the books"""
    list_of_df = []
    for book in books:
        df = theme_words(book, list_of_thematic_words)
        df['text'] = book
        list_of_df.append(df)

    res = pd.concat(list_of_df)
    plt.figure(figsize=(12, 12))
    barplot = sns.barplot(x='Word', y="Count", data=res, hue='text')
    barplot.set_title("Genre Specific Words Present in the Given Books: " + str(books))
    plt.xticks(rotation=70)
    plt.show()


# This list includes Anne of Green Gables, Pride and Prejudice, Wuthering Heights, Emma, Scarlet Letter, Romeo and Juliet
list_love_stories = [45,1342,768,158,25344,1513]

# Thematic (Romance related) Words Present in Pride and Prejudice, Emma, and Sense and Sensibility
# All by Jane Austen
list_jane_austen = [1342,158,105]

# Thematic (Horror related) Words Present in The Strange Case of Dr.Jekyll and Mr. Hyde,
# The Phantom of the Opera, Frankenstein, and Dracula
list_horror_tales = [43,175,84,345]

#Thematic (Mystery related) Words Present in The Murder on the Links, The Mysterious Affair at Styles,
# The Secret Adversary, Crime and Punishment, Shadow in the House, The Hound of the Baskervilles,
# A Study in Scarlet, and The Sign of the Four
list_mysteries = [58866, 863,1155, 2554, 2852, 244, 2097, 66859]

# Thematic (Mystery related) Words Present in The Hound of the Baskervilles,
# A Study in Scarlet, and The Sign of the Four
list_arthur_conan = [2852, 244, 2097]

# Thematic (Mystery related) Words Present in Murder on the Links,
# The Mysterious Affair at Styles, and The Secret Adversary
# All by Agatha Christie
list_agatha_christie = [58866, 863, 1155]

# Thematic (Christmas related) Words Present in A Christmas Carol,
# Twas' the Night before Christmas, and A Pilgrim's First Christmas
christmas = [17135,46,66828]


#Example Graphs
horror_graph = graph_theme_words(list_horror_tales, list_of_horror_words)
jane_graph = graph_theme_words(list_jane_austen, list_of_romance_words)
christmas_graph = graph_theme_words(christmas, list_of_christmas_words)
romance_graph = graph_theme_words(list_love_stories, list_of_romance_words)
agatha_graph = graph_theme_words(list_agatha_christie, list_of_mystery_words)
conan_graph = graph_theme_words(list_arthur_conan, list_of_mystery_words)
mysteries_graph = graph_theme_words(list_mysteries, list_of_mystery_words)

