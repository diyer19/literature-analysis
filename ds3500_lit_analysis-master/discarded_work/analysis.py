"""
@author: Brennan Ayres
@file: analysis.py: A text reader designed to quantitatively score text sophistication.
"""

import textstat
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import gutenberg
import pandas as pd
import plotly.express as px
from text_storage import data_storage

# Read in a manually downloaded text file, in this case Moby Dick
# with open('moby_dick.txt', 'r') as file:
#     data = file.read().replace('\n', '')
#     file.close()

# Uses the Flesch Reading Ease score from the textstat library to score a text from 1-100 based on its
# readability at various age levels. (100 being simplest to read, 1 being most challenging)
def flesch_reading_score(books):
    scores = []
    for index in books:
        score = textstat.flesch_reading_ease(data_storage(index))
        scores.append(score)
    data = list(zip(books, scores))
    df = pd.DataFrame(data, columns = ['Book Index', 'Flesch Reading Score'])
    fig = px.bar(df, x="Book Index", y="Flesch Reading Score",
                 title="Flesch Reading Scores for the Given Books")
    fig.show()


#print('The Flesch reading score is:', flesch_reading_score)

# Uses the Flesch Kincaid score from the textstat library to evaluate a text's readability based on grade level
def flesch_kincaid_score(books):
    scores = []
    for index in books:
        score = textstat.flesch_kincaid_grade(data_storage(index))
        scores.append(score)
    data = list(zip(books, scores))
    df = pd.DataFrame(data, columns = ['Book Index', 'Flesch Kincaid Score'])
    fig = px.bar(df, x="Book Index", y="Flesch Kincaid Score",
                 title="Flesch Kincaid Scores for the Given Books")
    fig.show()

# Uses the Gunning Fog formula from the textstat library to score a text's readability based on grade level
def gunning_score(books):
    scores = []
    for index in books:
        score = textstat.gunning_fog(data_storage(index))
        scores.append(score)
    data = list(zip(books, scores))
    df = pd.DataFrame(data, columns = ['Book Index', 'Gunning Score'])
    fig = px.bar(df, x="Book Index", y="Gunning Score",
                 title="Gunning Scores for the Given Books")
    fig.show()

# Uses the SMOG index from the textstat library to score a text's readability based on grade level

def smog_score(books):
    scores = []
    for index in books:
        score = textstat.smog_index(data_storage(index))
        scores.append(score)
    data = list(zip(books, scores))
    df = pd.DataFrame(data, columns = ['Book Index', 'Smog Score'])
    fig = px.bar(df, x="Book Index", y="Smog Score",
                 title="Smog Scores for the Given Books")
    fig.show()

books = [11,12,14]
#flesch_reading_score(books)
smog_score(books)
# gunning_score(books)
# flesch_kincaid_score(books)







# Averages the three grade-level scoring methods to strengthen the interpretation of the text's readability
#balance = int((flesch_kincaid_score + gunning_score + smog_score) // 3)

#print('\nIn other words, the average grade level to properly comprehend this book is:', balance, '\n')

# NOTE: textstat.text_standard function fails with 'dirty' text (that hasn't been stripped of non-alphanumeric chars
#consensus = textstat.text_standard(data, float_output=False)


# def sentiment_analyzer(text):
#     """indicates the overall sentiment of the body of text by displaying percentages of negative, neutral, and positive tone.
#     Also provides a compound score to show the majority of the tone """
#     sid = SentimentIntensityAnalyzer()
#     scores = sid.polarity_scores(text)
#     print(scores)


###########################################################################################################

# getting info from text using gutenberg nlkt.corpus gutenberg library
# Unsure about use

# from nltk.corpus import gutenberg
# # NLTK includes a small selection of texts from the Project Gutenberg
# # site, which contains some 25,000 free electronic books,
#
# def text_analysis():
#     """This displays four statistics for each text:
#     number of words in the text
#     average word length,
#     average sentence length,
#     and the number of times each vocabulary item
#     appears in the text on average."""
#     for fileid in gutenberg.fileids():
#         num_chars = len(gutenberg.raw(fileid))
#         num_words = len(gutenberg.words(fileid))
#         num_sents = len(gutenberg.sents(fileid))
#         num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
#         print(fileid, "Number of words: ", num_words, "Average word length: ", round(num_chars/num_words),
#               "Average sentence length ", round(num_words/num_sents), "Lexical diversity score", round(num_words/num_vocab))
#
#
# def main():
#     sentiment_analyzer(data[:5000])
# # TODO evolution of sentiment throughout body of text
# # TODO plot sentiment by sentence to establish signature
# # TODO Character network
# # Sample sentiment at various parts of text
#
#
#
# if __name__ == '__main__':
#     main()