import nltk
nltk.download('stopwords')
import string
from math import sqrt


def removeSpecCharsFromText(text):
    specChars = string.punctuation + '\n\xa0«»\t—…emptyline' + 'xml' + 'version' + 'encoding' + 'utf' \
                + 'fictionbookhwwwjjaa' + 'љ'
    return "".join([char for char in text if char not in specChars])


def removeDigitsFromText(text):
    return "".join([char for char in text if char not in string.digits])


def removeRusStopwordsFromText(text):
    russianStopwords = nltk.corpus.stopwords.words("russian")
    return [word for word in text if not word in russianStopwords]


def textAnalyze(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        text = text.lower()
        text = removeDigitsFromText(removeSpecCharsFromText(text))
        textTokens = nltk.wordpunct_tokenize(text)
        textTokens = removeRusStopwordsFromText(textTokens)
        text = nltk.Text(textTokens)
        fdist = nltk.probability.FreqDist(text)
    return dict(fdist)


# print('d\n', textAnalyze('detectives/The investigation that is looking for the killer.txt'))
detectivesNames = ['The investigation that is looking for the killer.txt',
                   'Guardian.txt',
                   'The investigation of an American detective.txt',
                   'The cause of my death.txt',
                   'The Boomerang Law.txt']
fictionNames = ['Adventures of the Immortal Highlander Kenny.txt',
                'Children of the Night.txt',
                'New Age.txt',
                'Third Round.txt',
                'Who is stronger.txt']
detectivesData = [textAnalyze('detectives/' + detective) for detective in detectivesNames]
fictionData = [textAnalyze('fiction/' + fiction) for fiction in fictionNames]
testData=textAnalyze('test.txt')
print(testData.keys())
for testKeys in testData.keys():
