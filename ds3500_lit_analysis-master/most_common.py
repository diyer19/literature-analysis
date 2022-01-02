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


def most_common_one_book(num):
    """
    params: number representing the index of the desired book from the Gutenberg library
    returns: a dictionary the count of every word in the book excluding stopwords"""
    text = data_storage(num)
    wordcount = {}

    # Stopwords
    stop_words = list(STOPWORDS)
    stop_words.append('said')
    stop_words.append('will')
    stop_words.append('us')
    stop_words.append('one')
    stop_words.append('got')
    stop_words = set(stop_words)

    list_of_text = text.lower().split()
    for word in list_of_text:
        if word not in stop_words:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    word_counter = collections.Counter(wordcount)
    return word_counter


def most_common_words(num, num2, num_words):
    """
    params: This method takes in three integers. The first two integers represent the index of the given text
    from the Gutenberg library, and the third integer represents the number of desired common words.
    returns: the n most common words that are present and also the same in both books"""

    word_counter = most_common_one_book(num)

    # Create a data frame of the most common words
    list_most_common = word_counter.most_common(num_words)
    df_text1 = pd.DataFrame(list_most_common, columns=['Word', 'Count'])

    new_list_most_common_text1 = list(map(list, zip(*list_most_common)))

    # Finding most common words for second text
    word_counter2 = most_common_one_book(num2)

    list_most_common2 = word_counter2.most_common(num_words)
    df_text2 = pd.DataFrame(list_most_common2, columns=['Word', 'Count'])

    df_text1['text'] = num
    df_text2['text'] = num2
    res = pd.concat([df_text1, df_text2])
    plt.figure(figsize=(10, 10))
    barplot2 = sns.barplot(x="Word",y="Count", data=res, hue='text')
    barplot2.set_title("Most Common words in Books " + str(num) + " and " + str(num2) + " respectively")
    plt.xticks(rotation=70)
    plt.show()

    # Are there any of the same most common words in these two books?
    print("\nAre there any of the same most common words in these two books?")
    list_of_common_words1 = []
    list_of_common_words2 = []

    for word, amount in list_most_common:
        for word2, amount2 in list_most_common2:
            if word == word2:
                tuple1 = (word, amount)
                tuple2 = (word2, amount2)
                list_of_common_words1.append(tuple1)
                list_of_common_words2.append(tuple2)


    df1 = pd.DataFrame(list_of_common_words1, columns=['Word','Count'])
    df2 = pd.DataFrame(list_of_common_words2, columns=['Word', 'Count'])

    df1['text'] = num
    df2['text'] = num2
    res = pd.concat([df1, df2])
    try:
        barplot3 = sns.barplot(x="Word", y="Count", data=res, hue='text')
        barplot3.set_title("Common words in Books " + str(num) + " and " + str(num2))
    except ValueError as v:
        print("No Common Words Present Between The Two Books")

    plt.show()



# Find the most common words between Anne of Green Gables and Emma
# Love Stories
love_stories_1 = most_common_words(45, 158, 10)



# Find the most common words between Pride and Prejudice and Emma
# Love Stories // by Jane Austen
love_stories_2 = most_common_words(1342, 158, 10)


# Find the most common words between A Christmas Carol and Twas the Night Before Christmas
# Christmas
christmas = most_common_words(17135, 46, 10)


# Find the most common words between Frankenstein and Dracula
# Horror Tales
horror_tales_1 = most_common_words(84, 345, 10)


# Find the most common words between Great Gatsby and Scarlet Letter
# Married Women
married_women = most_common_words(64317,25344,10)



# Find the most common words between The Strange Case of Dr. Jekyll and Mr. Hyde and The Phantom of the Opera
# Horror Tales
horror_tales_2 = most_common_words(43, 175,15)


