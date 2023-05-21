#!/usr/bin/env python
# coding: utf-8

# In[33]:

import pandas as pd
import numpy as np
import spacy
import re
import string
import nltk
import url_normalize
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from google.cloud import storage

# Download required resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# Define the text cleaning function
def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]

    # Remove numerical values
    tokens = [token for token in tokens if not token.isnumeric()]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Join tokens back into a single string
    cleaned_text = " ".join(tokens)

    return cleaned_text


# In[44]:


def extract_features(sentence):
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence.lower())

    # Remove common stopwords
    stop_words = set(nltk.corpus.stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]

    # Initialize the list of article features
    article_features = []

    # Iterate over the tokens and extract relevant features
    for i in range(len(tokens)):
        if tokens[i] == "men" or tokens[i] == "woman" or tokens[i] == "unisex":
            # Include gender-specific terms
            article_features.append(tokens[i])
        elif tokens[i] != "in":
            # Exclude the word "in"
            article_features.append(tokens[i])

            # Check if the current token is followed by "in"
            if i < len(tokens) - 1 and tokens[i + 1] == "in":
                # Include the brand name
                article_features.append(tokens[i + 2])

    # Join the extracted features into a single string
    extracted_features = " ".join(article_features)

    return extracted_features


# In[57]:


def find_similar_sentences(query_text, top_k, df):
    # Normalize the 'Url' column
    df['NormalizedUrl'] = df['Url'].apply(url_normalize.url_normalize)

    # Drop duplicates based on the normalized 'Url' column
    df = df.drop_duplicates(subset=['NormalizedUrl'])

    # Remove the temporary 'NormalizedUrl' column
    df = df.drop(columns=['NormalizedUrl'])

    df.reset_index(drop=True, inplace=True)

    # Apply the text cleaning function to the 'Text' column
    df["CleanedText"] = df["Name"].apply(clean_text)

    # Create a CountVectorizer instance
    vectorizer = CountVectorizer()

    # Fit the vectorizer on the cleaned text data
    vectorizer.fit(df["CleanedText"])

    # Transform the query text into a bag-of-words vector
    query_vector = vectorizer.transform([query_text])

    # Transform the entire dataset into bag-of-words vectors
    sentence_vectors = vectorizer.transform(df["CleanedText"])

    # Compute similarity scores between the query and all sentences
    similarity_scores = cosine_similarity(query_vector, sentence_vectors)

    # Get the indices of the top-k most similar sentences
    indices = similarity_scores[0].argsort()[::-1][:top_k]

    # Get the similar sentences and convert it to list
    similar_sentences_urls = df.loc[indices, "Url"].tolist()

    # Serialize the list to JSON
    results_json = json.dumps(similar_sentences_urls)

    return results_json


def google_cloud_function(request):
    # initialize storage client
    client = storage.Client.from_service_account_json('./key.json')    
    df = pd.read_csv('gs://clothing--similarity-bucket/data.csv', encoding='utf-8')
    request_json = request.get_json()
    if not request_json or 'query' not in request_json:
        return 'Error: Missing query parameter in the request.', 400

    query = request_json['query']
    topN = int(request_json.get('topN', 10))
    updatedQuery = extract_features(clean_text(query)) # Clean and extract features from the query
    similar_results = find_similar_sentences(query, topN, df) # Calculate the results 
    return similar_results


