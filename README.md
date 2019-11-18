This is a python program to determine the [sentiment](https://en.wikipedia.org/wiki/Sentiment_analysis) of arbitrary text files. Please excuse its incredibly poor quality -- I actually don't know how to program in Python (very well, anyway, this is my first thing). It depends on the amazing [TextBlob](https://textblob.readthedocs.io/en/dev/) to do its thing.

[Anaconda](https://www.anaconda.com/distribution/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) highly recommended. I develop in Miniconda.

To set up the environment, run ```conda env create -f environment.yml```.

Usage: get an arbitrary text file and then run `python sentiment.py <filename>`

Todo:

~~Separate out the sentiment number into its own variable.~~

~~Assign arbitrary categories based on sentiment number, like "mildly positive", "very positive", etc.~~

* Possibly move the judged text file into its own directory, like "good" and "bad" or something.

