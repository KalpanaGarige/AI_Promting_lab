# Prompt:
# Write a Python script that cleans social media data:
# - clean text (remove stopwords, punctuation, HTML)
# - handle missing values for likes/shares
# - convert timestamp to datetime and extract hour, weekday
# - detect duplicate/spam posts and remove them.

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

# Download stopwords
nltk.download('stopwords')

# Load your file
df = pd.read_csv("social_media.csv")

# ---------- 1. Clean Text Column ----------
def clean_text(text):
    if pd.isna(text):
        return ""
    
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()
    
    # Remove special characters and punctuation
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    
    # Lowercase
    text = text.lower()

    # Remove stopwords
    stops = set(stopwords.words("english"))
    text = " ".join(word for word in text.split() if word not in stops)

    return text

df["clean_post"] = df["post_text"].apply(clean_text)

# ---------- 2. Handle Missing Values ----------
df["likes"] = df["likes"].fillna(0)
df["shares"] = df["shares"].fillna(0)

# ---------- 3. Convert timestamp ----------
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Extract new features
df["hour"] = df["timestamp"].dt.hour
df["weekday"] = df["timestamp"].dt.day_name()

# ---------- 4. Remove Duplicates / Spam ----------
df = df.drop_duplicates(subset=["clean_post"])

# ---------- Final Cleaned Output ----------
print("\nCleaned Data:")
print(df.head())

# Save cleaned file
df.to_csv("cleaned_social_media.csv", index=False)
print("\nCleaned file saved as cleaned_social_media.csv")
