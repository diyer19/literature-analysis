from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import re
from text_storage import data_storage

# slight modifications to pre-populated set of stopwords
stop_words = list(STOPWORDS)
stop_words.append('said')
stop_words.append('will')
stop_words.append('us')
stop_words.append('one')
stop_words = set(stop_words)

def plot_cloud(num):
    """
    Plots wordcloud of given text dataset extracted from ElasticSearch database
    params: 'num': index of a specific piece of text in the ElasticSearch database
    returns: wordcloud
    """
    wordcloud = WordCloud(width= 3000, height = 2000, random_state=1,
                      background_color='salmon', colormap='Pastel1',
                      collocations=False, stopwords = stop_words).generate(data_storage(num))
    # Set figure size
    plt.figure(figsize=(8, 8))
    
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
 
    return


plot_cloud(7)