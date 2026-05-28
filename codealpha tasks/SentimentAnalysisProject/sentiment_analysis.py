import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
df = pd.read_csv("reviews.csv")
print("\nDATASET LOADED SUCCESSFULLY\n")
print(df)
def get_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
df['Sentiment'] = df['Review'].apply(get_sentiment)
print("\nSENTIMENT RESULTS\n")
print(df)
sentiment_counts = df['Sentiment'].value_counts()
print("\nSENTIMENT COUNTS\n")
print(sentiment_counts)
plt.bar(sentiment_counts.index, sentiment_counts.values)
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
df.to_csv("sentiment_results.csv", index=False)
print("\nRESULTS SAVED SUCCESSFULLY!")