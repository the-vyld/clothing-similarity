# Clothing Similarity BoW Model

1. `scrapper.py` scrapes ajax request data from clothing websites using `requests` library and stores it in a pandas dataframe and stores it as `data.csv`
2. the textual data is cleaned and shuffled and the text descriptions are tokenized using `nltk` library
3. `extract_features` function extracts useful features from a sentence which is used to pre-process the input query string for better model performance
4. used a `vector-spaced` bag of words model with cosine_similarity to compare similarity between the input and existing data and then output the results
5. model compares the whole dataset and returns topN (query param, default = 10) similar results

# Deployement instructions

1. upload the `main.py` file and `requirements.txt` file in google-cloud-functions
2. add the dataset in a cloud-storage-container which should be in the same project as the function
3. make sure necessary permissions are provided to the service of the cloud function to access the container and the database within
4. in the entry-point function for google cloud, include the storage client with a path to your function's service's api key for authorization
5. also add the api key (`key.json`) in the zip file at same level containing main and requirements
