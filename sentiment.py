import sys
from textblob import TextBlob

# turning the judge into a function
def judge(score):
    "This function takes the sentiment score and applies a judgment to it"
    print(score)
    return


print("The file you selected is:", sys.argv[1])
text_file = open(sys.argv[1],"r")
output = text_file.read()
text_sentiment = TextBlob(output)
score = text_sentiment.sentiment.polarity
print(text_sentiment.sentiment)
# If/else tree for judging sentiment
if score > 0.01 and score < 0.3:
    print("I declare this.... somewhat positive!") 
elif score > 0.3:
    print("I declare this.... very positive!")
elif score < -0.01 and score > -0.3:
    print("I declare this.... somewhat negative!")
elif score < -0.3:
    print("I declare this.... very negative!")
elif score == 0:
    print("I declare this.... true neutral!")
else:
    print("wtf!!!!??")

