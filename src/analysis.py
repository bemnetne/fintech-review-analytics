# -----------------------------------
# Import Libraries
# -----------------------------------

import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer


# -----------------------------------
# Download NLTK Resources
# -----------------------------------

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# -----------------------------------
# Initialize NLP Tools
# -----------------------------------

# English stopwords
stop_words = set(stopwords.words('english'))

# Lemmatizer
lemmatizer = WordNetLemmatizer()


# -----------------------------------
# Load Dataset
# -----------------------------------

df = pd.read_csv("bank_reviews_sentiment.csv")


# -----------------------------------
# 1. Tokenization Function
# -----------------------------------

def tokenize_text(text):
    """
    Split text into individual words/tokens.
    """

    # Convert text to lowercase
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


# -----------------------------------
# 4. Complete Preprocessing Pipeline
# -----------------------------------

def preprocess_text(text, apply_lemmatization=True):
    """
    Full preprocessing pipeline:
    1. Tokenization
    2. Stop-word removal
    3. Optional lemmatization
    """

    # Step 1: Tokenization
    tokens = tokenize_text(text)

    # Step 2: Stop-word removal
    cleaned_tokens = remove_stopwords(tokens)

    # Step 3: Optional lemmatization
    if apply_lemmatization:
        cleaned_tokens = lemmatize_tokens(cleaned_tokens)

    # Convert tokens back to sentence
    processed_text = " ".join(cleaned_tokens)

    return processed_text


# Apply Text Preprocessing


df["processed_review"] = df["review"].apply(
    preprocess_text
)



# TF-IDF Keyword Extraction


vectorizer = TfidfVectorizer(
    max_features=100,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(
    df["processed_review"]
)

keywords = vectorizer.get_feature_names_out()

scores = X.mean(axis=0).A1

tfidf_df = pd.DataFrame({
    "keyword": keywords,
    "score": scores
})

tfidf_df = tfidf_df.sort_values(
    by="score",
    ascending=False
)

print("\nTop TF-IDF Keywords:")
print(tfidf_df.head(20))


# Theme Identification 


def identify_theme(text):
    """
    Assign business-related themes
    using keyword matching.
    """

    text = text.lower()

    # Account Access Issues
    if any(word in text for word in [
        "login", "password", "otp",
        "account", "secured"
    ]):
        return "Account Access & Security"

    # Transaction Performance
    elif any(word in text for word in [
        "transaction", "transfer",
        "payment", "money", "balance"
    ]):
        return "Transaction Performance"

    # Technical Issues
    elif any(word in text for word in [
        "slow", "error", "problem",
        "crash", "working", "open"
    ]):
        return "Technical Issues"

    # UI & User Experience
    elif any(word in text for word in [
        "easy", "good", "nice",
        "amazing", "best"
    ]):
        return "UI & User Experience"

    # Feature Requests
    elif any(word in text for word in [
        "update", "feature",
        "improve", "option"
    ]):
        return "Feature Requests"

    else:
        return "Other"


# Apply Theme Identification


df["identified_theme"] = df[
    "processed_review"
].apply(identify_theme)



# Save Results as CSV


final_df = df[
    [
        "review_id",
        "review",
        "sentiment",
        "confidence_score",
        "identified_theme"
    ]
]

# Rename columns according to requirements
final_df = final_df.rename(columns={
    "review": "review_text",
    "sentiment": "sentiment_label",
    "confidence_score": "sentiment_score"
})

# Save final dataset
final_df.to_csv(
    "bank_reviews_analysis.csv",
    index=False
)