from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from termcolor import colored

print(colored("\n🔹 NLP Practical: Sentiment Analysis 🔹\n", "cyan", attrs=["bold"]))

# Take input from user
text = input("Enter a sentence for Sentiment Analysis: ")

# Analyze using TextBlob
blob = TextBlob(text)
polarity = blob.sentiment.polarity  # -1 (negative) to +1 (positive)

# Show result
print("\nResult of Sentiment Analysis:")
if polarity > 0:
    print(colored("✅ Positive 😀", "green", attrs=["bold"]))
elif polarity < 0:
    print(colored("❌ Negative 😡", "red", attrs=["bold"]))
else:
    print(colored("😐 Neutral", "blue", attrs=["bold"]))

print(colored("\n🔹 Generating WordCloud from sample text... 🔹\n", "cyan"))

sample_reviews = text

# Generate WordCloud
wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="viridis").generate(sample_reviews)

# Show WordCloud
plt.figure(figsize=(8,4))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("WordCloud of Text", fontsize=14, color="darkblue")
plt.show()