from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_metadata
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import re
from nltk.sentiment import SentimentIntensityAnalyzer



# not actually sure if this works lol, but this doesn't return any errors
# intention: create a list of a range of full-length texts from gutenberg
# retrieve and clean each text and then creates a list of the given texts
# list_of_text = []
# for i in range(1, 12):
#     text = strip_headers(load_etext(i)).strip()
#     list_of_text.append(text)
# print(list_of_text)



####################################################################################
# below is the text used for the elasticsearch trial

#retrieve/clean text
text = strip_headers(load_etext(11)).strip()
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')


# not sure if we want to keep this,
# but it basically returns a list of sentiment analysis score for every sentence in the text
# further down is a sentiment analysis for text divided up into 6 sections rather than every sentence

# list_of_sentiment_scores = []
# for sentence in tokenized_text:
#     sid = SentimentIntensityAnalyzer()
#     scores = sid.polarity_scores(sentence)
#     list_of_sentiment_scores.append(scores)
# print(list_of_sentiment_scores)


# splitting the entire text into individual words
text_file_tokenized = (word_tokenize(text))


# text without stop words, split into a list of individual words
tokens_without_sw = [word for word in text_file_tokenized if not word in stopwords.words()]

#############################################################################################
# ELASTIC SEARCH STUFF

from elasticsearch import Elasticsearch
from datetime import datetime


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


doc = {
    'author': str(get_metadata('title', 11)),
    # this still gives me 'frozenset()', but ideally this should return
    # something like frozenset([u'Alice in Wonderland'])

    'text': text,
    'timestamp': datetime.now(),
}

# #indexing a document
res = es.index(index="test-index", id=1, body=doc)
#print(res['result'])
#print(res)


# getting a document
res = es.get(index="test-index", id=1)
print(res['_source'])


############################################################################################################################

# THIS PART ADDRESSES COMMENT FROM SAMAR BELOW:
# Sentiment analysis: As mentioned during the presentation,
# splitting the text into a few parts and analysing each part to
# create a sort of 'sentiment progress as the book progresses'.


# def chunks(lst):
#     """Splits the text evenly into 6 parts"""
#     for i in range(0, len(lst), -(-(len(lst))//6)):
#          return (lst[i:i + (-(-(len(lst))//6))])
#
#
# def sentiment_analysis_split_text(text):
#     """ Returns a list of sentiment scores for
#     divided sections of the given text"""
#     tokenized_text = (sent_tokenize(text))
#     list_of_sentiment_scores = []
#     list_of_text = chunks(tokenized_text)
#     for text in list_of_text:
#         sid = SentimentIntensityAnalyzer()
#         scores = sid.polarity_scores(text)
#         list_of_sentiment_scores.append(scores)
#     print(list_of_sentiment_scores)
#
# sentiment_analysis_split_text(text)



#####################################################


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


def most_common_words(num, num2, num_words):
    """ This method takes in three integers. The first two integers represent the index of the given text
    from the Gutenberg library, and the third integer represents the number of desired common words.
     It outputs the n most common words that are present and also the same in both books"""

    text = data_storage(num)

    # Stopwords
    stopwords = set(line.strip() for line in open('stopwords.txt'))

    # Instantiate a dictionary, and for every word in the file,
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    # this displays all the words (excluding stopwords) in the text and how many times they appear
    wordcount = {}
    list_of_text = text.lower().split()

    for word in list_of_text:
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1



    # Print 10 most common words and the amount they show up
    word_counter = collections.Counter(wordcount)
    print("Most Common " + str(num_words) + " Words in Book # " + str(num))
    for word, count in word_counter.most_common(num_words):
        print(word, ": ", count)

    # Create a data frame of the most common words
    list_most_common = word_counter.most_common(num_words)
    df_text1 = pd.DataFrame(list_most_common, columns=['Word', 'Count'])

    new_list_most_common_text1 = list(map(list, zip(*list_most_common)))

    # fig_text1 = px.bar(df_text1, x="Word", y="Count", title="Text " + str(num) + ": Most Common Words")
    # fig_text1.show()

    # Finding most common words for second text
    text2 = data_storage(num2)
    wordcount_second_text = {}
    list_of_second_text = text2.lower().split()
    for word in list_of_second_text:
        if word not in stopwords:
            if word not in wordcount_second_text:
                wordcount_second_text[word] = 1
            else:
                wordcount_second_text[word] += 1
    word_counter2 = collections.Counter(wordcount_second_text)

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

    # fig_text2 = px.bar(df_text2, x="Word", y="Count", title="Text " + str(num) + ": Most Common Words")
    # fig_text2.show()
    new_list_most_common_text2 = list(map(list, zip(*list_most_common2)))


    # Which most common words from text 1 appear in text 2
    print("\nWhich Most Common Words from Text 1 appear in Text 2")
    for word in list(wordcount_second_text.keys()):
        for word2 in new_list_most_common_text1[0]:
            if word == word2:
                print(word)

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
    barplot3 = sns.barplot(x="Word", y="Count", data=res, hue='text')
    barplot3.set_title("Common words in Books " + str(num) + " and " + str(num2))

    plt.show()

#most_common_words(345,42324)
#most_common_words(11,12,15)
most_common_words(45,46,15)

#TODO see if the most common words in one text are in the second text

#################################################################################################################################################################
# df1=sentiment_analysis_dataframe(num1)
# df2=sentiment_analysis_dataframe(num2)
# df1['text']=num1
# df2['text']=num2
#
# df = pd.concat([df1, df2]).reset_index(drop=True)
#
# # plot df
# sns.relplot(data=df, x='section', y=y_value, kind='line', hue='text', palette=['orange', 'pink'])
# plt.show()



    # df1=sentiment_analysis_dataframe(num1)
    # df2=sentiment_analysis_dataframe(num2)
    # df1['text']=num1
    # df2['text']=num2
    # res=pd.concat([df1,df2])
    # sns.barplot(x='section', y=y_value, data=res, hue='text')
    # plt.show()


# grouped bar charts for progression of positive sentiment scores in Dracula and Frankenstein
#grouped_graphs(345, 42324, "pos")

################################################################################################

# fig = px.bar(df, x="section", y="neg", color="section",
#              title="Text " + str(num) + ": Negative Sentiment Scores throughout the Book")
# fig1 = px.bar(df, x="section", y="pos", color="section",
#              title="Text " + str(num) + ": Positive Sentiment Scores throughout the Book")

##########################################################################################################
# Which most common words from text 1 appear in text 2
# print("\nWhich Most Common Words from Text 1 appear in Text 2")
# for word in list(word_counter2.keys()):
#     for word2 in new_list_most_common_text1[0]:
#         if word == word2:
#             print(word)

#stopwords = set(line.strip() for line in open('stopwords.txt'))


############################################################################################################

# a = 0
# b = 0
# c = 0
# d = 0
# e = 0
# f = 0
# for a in range(0, length//6):
#     val = "1st"
#     new_list.append(val)
#     a += 1
# for b in range(length//6, ((length//6) * 2)):
#     value = "2nd"
#     new_list.append(value)
#     b += 1
# for c in range(((length//6) * 2), ((length//6) * 3)):
#     value = "3rd"
#     new_list.append(value)
#     c += 1
# for d in range(((length//6) * 3), ((length//6) * 4)):
#     value = "4th"
#     new_list.append(value)
#     d += 1
# for e in range(((length//6) * 4), ((length//6) * 5)):
#     value = "5th"
#     new_list.append(value)
#     e += 1
# for f in range(((length//6) * 5), length):
#     value = "6th"
#     new_list.append(value)
#     f += 1
# df = pd.DataFrame(sentiment_analysis_split_text(num))
# df["section"] = new_list
# return df


#
# def grouped_bar_graphs(books, y_value, section_number):
#     """ this method produces a grouped bar chart displaying the
#     progression of the given sentiment throughout each book
#     This method takes in a list of numbers representing the indexes of the desired books
#      from the Gutenberg library, It also takes in a string representing either
#       'pos', 'neg', 'neutral', or 'compound' sentiment. Additionally, it takes in a number representing the
#        number of sections """
#     list_of_df = []
#     for index in books:
#         df = sentiment_analysis_dataframe(index, section_number)
#         df['text'] = index
#         list_of_df.append(df)
#     res = pd.concat(list_of_df)
#     plt.figure(figsize=(10, 10))
#     barplot = sns.barplot(x='section', y=y_value, data=res, hue='text')
#     barplot.set_title(y_value + " Sentiment throughout the given books: " + str(books) )
#     plt.show()