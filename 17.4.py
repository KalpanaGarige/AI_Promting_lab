#Clean a movie reviews dataset with the following steps:
# Standardize text (lowercase, remove HTML tags, remove punctuation).
# Tokenize and encode reviews using TF-IDF.
# Handle missing ratings (fill with median).
# Normalize ratings from 0–10 scale to 0–1 scale.
# Detect duplicates and remove them.
# Produce a before vs after summary report.

import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler

# 1. Load Dataset
df = pd.read_csv("movie_reviews-1.csv")   # your file
print("----- BEFORE CLEANING -----")
print(df.head())

# 2. Remove HTML tags
def clean_html(text):
    return BeautifulSoup(text, "html.parser").get_text()

df["review_text"] = df["review_text"].astype(str).apply(clean_html)

# 3. Lowercase + remove punctuation

def clean_text(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9\s]", "", t)
    return t

df["review_text"] = df["review_text"].apply(clean_text)

# 4. Handle missing ratings (fill with median)
median_rating = df["rating"].median()
df["rating"] = df["rating"].fillna(median_rating)

# 5. Normalize ratings (0-10 → 0-1)

scaler = MinMaxScaler()
df["rating_normalized"] = scaler.fit_transform(df[["rating"]])

# 6. Remove duplicate reviews
df = df.drop_duplicates(subset=["review_text"])

# 7. TF-IDF Encoding
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df["review_text"])

# Convert TF-IDF to a DataFrame (optional)
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=tfidf.get_feature_names_out()
)
# 8. Summary After Cleaning
print("\n----- AFTER CLEANING -----")
print(df.head())

print("\nTF-IDF Shape:", tfidf_df.shape)

# Save cleaned data
df.to_csv("cleaned_movie_reviews.csv", index=False)
tfidf_df.to_csv("movie_reviews_tfidf.csv", index=False)

print("\n✔ Cleaning complete!")
print("✔ cleaned_movie_reviews.csv created")
print("✔ movie_reviews_tfidf.csv created")
