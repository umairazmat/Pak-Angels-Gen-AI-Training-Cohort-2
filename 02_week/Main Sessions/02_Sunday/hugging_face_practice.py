# Model Link : https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline(
    "text-classification",
    model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis",
)


# Predict the sentiment of a sentence

from transformers import pipeline

# Load a pre-trained model for sentiment analysis
classifier = pipeline("sentiment-analysis")

# Test on a sample text
result = classifier("Hugging Face is amazing!")

print(result)


# Predict the sentiment of a sentence
from transformers import pipeline

# Load a pre-trained model for sentiment analysis
classifier = pipeline("sentiment-analysis")

# Test on a sample text
# result = classifier("Hugging Face is amazing!")
# result = classifier("Hugging Face made me frustrated!")
# result = classifier("Hugging Face is OK")
result = classifier("Pakistan is the crazy")
print(result)


# Predict the sentiment of a sentence
from transformers import pipeline

# Load a pre-trained model for sentiment analysis
classifier = pipeline("sentiment-analysis")

# Test on a sample text
result = classifier("Hugging Face is Bad!")

print(result)
