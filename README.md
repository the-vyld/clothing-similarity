# Clothing Similarity BoW Model

This is a model which excepts a string having some description of a clothing article by a user, for ex: `I want an adidas red t-shirt` and returns topN similar results to the article using `feature extraction`, `vector-space embeddings` and `cosine_similarity`. I have extracted the data using web-scraping from a website `asos.com` as they had a huge list and variety of products. The model is deployed on `google-cloud-functions` and accepts a `JSON` in this format:

`{
    "query": "...",
    "topN": "..."
 }`
 
 here query parameter is mandatory and topN is optional (set to 10 by default).

1. `scrapper.py` scrapes ajax request data from clothing websites using `requests` library and stores it in a pandas dataframe `data.csv`
2. the textual data is cleaned and shuffled and the text descriptions are tokenized using `nltk` library
3. `extract_features` function extracts useful features from a sentence which is used to pre-process the input query string for better model performance
4. used a `vector-spaced` bag of words model with cosine_similarity to compare similarity between the input and existing data and then output the results
5. model compares the whole dataset and returns topN (query param, default = 10) similar results

# Deployment instructions

1. upload the `main.py` file and `requirements.txt` file in google-cloud-functions
2. add the dataset in a cloud-storage-container which should be in the same project as the function
3. make sure necessary permissions are provided to the service of the cloud function to access the container and the database within
4. in the entry-point function for google cloud, include the storage client with a path to your function's service's api key for authorization
5. also add the api key (`key.json`) in the zip file at same level containing main and requirements
