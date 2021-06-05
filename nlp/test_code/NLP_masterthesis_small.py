# Importing libraries
import pandas as pd
import os
import re
import gensim
from gensim.utils import simple_preprocess
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
import gensim.corpora as corpora
import pyLDAvis.gensim_models
import pickle 
import pyLDAvis
from pprint import pprint
from imp import reload

#set directory
os.chdir('C:/DSIA/Masterarbeit/masterarbeit/nlp')

# Read data
df = pd.read_excel("./transcripts/Interview_1_transcript.xlsx")
df.columns = ["id", "text"]
#df = pd.DataFrame(df)

df.head(6)

#drop index 
df = df.drop(columns=["id"])
df.head()

# Remove punctuation
df['text'] = \
df['text'].map(lambda x: re.sub('[,\.!?:12]', '', x))

# Convert the texts to lowercase
df['text'] = \
df['text'].map(lambda x: x.lower())

# Print out the first rows 
df['text'].head()
df

# Import the wordcloud library
from wordcloud import WordCloud

# Join the different processed text 
long_string = ','.join(list(df['text'].values))

# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')

# Generate a word cloud
wordcloud.generate(long_string)

# Visualize the word cloud
wordcloud.to_image()

# remove stopwords 
stop_words = stopwords.words('german')
stop_words.extend(['schon', 'eng', 'sagt', 'wunderbar', 'gut'])

def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) 
             if word not in stop_words] for doc in texts]
data = df.text.values.tolist()
data_words = list(sent_to_words(data))
# remove stop words
data_words = remove_stopwords(data_words)
print(data_words[:1][0][:30])


