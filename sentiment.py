import sys
from textblob import TextBlob
print("The file you selected is:", sys.argv[1])
text_file = open(sys.argv[1],"r")
output = text_file.read()
text_sentiment = TextBlob(output)
print(text_sentiment.sentiment)
