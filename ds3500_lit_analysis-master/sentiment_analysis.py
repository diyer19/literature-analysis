from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_metadata
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import re
from nltk.sentiment import SentimentIntensityAnalyzer
from text_storage import data_storage
import pandas as pd
import plotly.express as px
import textwrap
import seaborn as sns
import matplotlib.pyplot as plt



def sentiment_analysis_split_text(num, section_number):
    """
    params: index number of the desired book from the Gutenberg library and
    number of sections desired for the analysis
    returns: a list of sentiment scores for
    divided sections of the given text"""
    text = data_storage(num)
    list_of_sentiment_scores = []
    list_of_text = textwrap.wrap(text, len(text)//section_number)
    for item in list_of_text:
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(item)
        list_of_sentiment_scores.append(scores)
    return list_of_sentiment_scores



def sentiment_analysis_dataframe(num, section_number):
    """ params: index number of the desired book from the Gutenberg library
    and the number of sections desired for the analysis
    returns: a dataframe consisting of the sentiment
    analysis scores separated out into the given number of sections"""
    length = len(sentiment_analysis_split_text(num, section_number))
    section_length = length//section_number
    new_list = []
    i = 0
    for i in range(0,section_number + 1):
        for j in range((i*section_length), min((i+1)*section_length, length)):
            if j >= (section_length * section_number):
                new_list.append(str(i))
            else:
                new_list.append(str(i + 1))

    df = pd.DataFrame(sentiment_analysis_split_text(num,section_number))
    df["section"] = new_list
    return df


def grouped_line_graphs(books, y_value, section_number):
    """
    params: a list of numbers representing the indexes of the desired books
     from the Gutenberg library, a string representing either
      'pos', 'neg', 'neutral', or 'compound' sentiment, and a number representing the
       number of sections
    returns: a grouped line chart displaying the
    progression of the given sentiment throughout each book"""
    list_of_df =[]
    for index in books:
        df = sentiment_analysis_dataframe(index, section_number)
        df['text'] = index
        list_of_df.append(df)
    res = pd.concat(list_of_df).reset_index(drop=True)

    plt.figure(figsize=(60, 50))
    lineplot = sns.relplot(data=res, x='section', y=y_value, kind='line', hue='text', palette=("deep"))
    lineplot.fig.suptitle(y_value + " Sentiment throughout the given books: " + str(books))
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
# Crime and Punishment, Shadow in the House, The Hound of the Baskervilles,
# A Study in Scarlet, and The Sign of the Four
list_mysteries = [58866, 1155, 2554, 2852]

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



# Example Graphs
# pos_horror = grouped_line_graphs(list_horror_tales, "pos", 30)
# neg_horror = grouped_line_graphs(list_horror_tales, "neg", 30)
# pos_romance = grouped_line_graphs(list_love_stories, "pos", 35)
# pos_christmas = grouped_line_graphs(christmas, "pos", 30)
# neg_romance = grouped_line_graphs(list_love_stories, "neg", 35)
# neg_agatha = grouped_line_graphs(list_agatha_christie, "neg", 30)
# neg_conan = grouped_line_graphs(list_arthur_conan, "neg", 30)
# pos_jane = grouped_line_graphs(list_jane_austen, "pos", 30)
# pos_mystery = grouped_line_graphs(list_mysteries, "pos", 30)
# neg_mystery = grouped_line_graphs(list_mysteries, "neg", 30)