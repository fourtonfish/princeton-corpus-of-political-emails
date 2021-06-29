import os
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from pprint import pprint
from rich import print as r_print

r_print("Exploring the [bold]Princeton Corpus of Political Emails[/bold] dataset")
print("Loading...")

df = pd.read_csv("corpus_v1.0.csv", dtype={
    "from_name": "string",
    "from_address": "string",
    "subject": "string",
    "body_text": "string",
    "name": "string",
    "office_sought": "string",
    "party_affiliation": "string",
    "office_level": "string",
    "district_type": "string",
    "final_website": "string",
    "crawl_date": "string",
    "source": "string",
    "state": "string",
    "type": "string",
    "subtype": "string",
    "date": "string",
    "hour": "string",
    "day": "string",
    "uid_email": "string",
    "uid_inbox": "string",
    "incumbent": "string"
})

pd.set_option("display.max.columns", None)
pd.set_option('display.max_rows', None)

print("Columns:")
pprint(list(df))

# print(df)

print("Preview:")
print(df.head(10))

column = "body_text"
values = pd.unique(df[column])
count = len(values)

print(f"found {count:,} values in the {column} column")

index = 0
total = len(df.groupby("state"))

for i, x in df.groupby("state"):
    index += 1
    state_lower = i.lower()
    p = os.path.join(os.getcwd(), f"emails-by-state/{state_lower}.csv")
    x["body_text"].to_csv(p, index=False)
