import re
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
def tokenize_text(text):
    """
    Split text into individual words/tokens.
    """

    # Convert to lowercase
    text = str(text).lower()

    # Remove punctuation and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize text
    tokens = word_tokenize(text)

    return tokens


# -----------------------------------
# 2. Stop-word Removal Function
# -----------------------------------

def remove_stopwords(tokens):
    """
    Remove common English stopwords.
    """

    cleaned_tokens = [
        token for token in tokens
        if token not in stop_words
    ]

    return cleaned_tokens


# -----------------------------------
# 3. Lemmatization Function
# -----------------------------------

def lemmatize_tokens(tokens):
    """
    Convert words into their base/root form.
    """

    lemmatized_tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
    ]

    return lemmatized_tokens