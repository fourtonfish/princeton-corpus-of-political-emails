import os
import pandas as pd
# import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from pprint import pprint
from rich import print as r_print
from us_state_abbrev import * 

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

index = 0
total = len(df.groupby("state"))

for i, x in df.groupby("state"):
    index += 1
    state_lower = i.lower()
    print(f"creating word cloud image for {state_lower}... ({index}/{total})")
    wordcloud = WordCloud(
        width = 500,
        height = 500,
        background_color = 'black',
        # max_words = 25,
        min_word_length = 3,
        stopwords = [
            "Alex",
            "and",
            "body_text",
            "for",
            "REDACTED",
            "sta",
            "the",
            "this",
            "Unsubscribe",
            "URL",
            "view"
        ],
        colormap = "Greys"
    ).generate(str(x["body_text"]))
    
    fig = plt.figure(
        figsize = (40, 30),
        facecolor = 'k',
        edgecolor = 'k'
    )
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    # plt.show()
    wordcloud.to_file(f"images/{us_state_abbrev[i].lower()}.png")
    with open(f"text/{us_state_abbrev[i].lower()}.txt", "w") as outfile:
        outfile.write(", ".join(wordcloud.words_.keys()))
