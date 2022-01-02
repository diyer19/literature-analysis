LITERATURE ANALYSIS PROJECT 

Running the Code:

**Sentiment Analysis (sentiment_analysis.py)**
To run the code and output a visualization for this component, you have to run the following method:

_grouped_line_graphs(list_of_book_indexes, sentiment_desired, number_of_sections)_

For the above method you have to input a list of integers representing 
the indexes of the desired books in the Gutenberg library, 
the sentiment desired (either "pos", "neg", "neu", or "compound"), 
and the desired number of sections that the analysis should be divided into



**Thematic Words Present (theme_words.py)**
To run the code and output a visualization for this component, you have to run the following method:

_graph_theme_words(list_of_book_indexes, list_of_thematic_words)_

For the above method you have to input a list of integers representing 
the indexes of the desired books in the Gutenberg library and a list of thematic or genre specific words.



**Finding Most Common Words (most_common.py)**
To run the code and output a visualization for this component, you have to run the following method:

_most_common_words(index1, index2, num_words)_

For the above method you have to input three integers. 
The first two integers represent the index of the given text
from the Gutenberg library, and the third integer represents the number of desired common words.
It outputs the n most common words that are present and also the same in both books



**word_clouds.py**
As long as the necessary packages & libraries are installed, this file should run and output one word cloud.
(The grapher method is executed in line 35, where it takes a book's index as a parameter input)



**zipf.py**
As long as the necessary packages & libraries are installed (and the text_storage.py file is saved in the same folder),
this file should run. This file is run as a primer for test_zipfs_law.py, and should not output anything.



**test_zipfs_law.py**
This file simply runs the generator method from zipf.py that generates a zipf table. It then prints this table
out in the shell and outputs a zipfian curve on a two-dimensional graph.



**heaps.py**
This file consists of two methods, heaps_analyzer and heaps_grapher, which conduct a heaps law analysis of a given
body of text and chart the findings in a heapsian curve on a two-dimensional graph, respectively. As long as the necessary
packages are installed (and the text_storage.py file is saved in the same folder) this file should be able to run in its current configuration.