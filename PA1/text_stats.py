import json
import string
from collections import Counter
from tabulate import tabulate
from nltk.corpus import stopwords
from matplotlib import pyplot as plt
import numpy as np
stopwords = set(stopwords.words('english'))


data = json.loads(open("/Users/javani/PycharmProjects/PA1/PA1/ksu_1000.json").read())
total_tokens = 0
emails_counter = Counter()
word_frequencies = Counter()
word_frequencies_without_stopwords = Counter()
webpages_with_emails = 0
total_wordcount = 0
for record in data:
    total_tokens += len(record["body"])
    total_wordcount += len(record["body"])
    if record["emails"]:
        webpages_with_emails = webpages_with_emails + 1
    emails_counter.update(record["emails"])
    word_frequencies.update(record["body"])

print(f"Average Document Length: {round(total_tokens / len(data), 2)}")
print(f"Top 10 most frequent email addresses:")
print(*emails_counter.most_common(10), sep="\n")
print(f"Percentage of webpages that contain an email address: {round(webpages_with_emails / len(data), 2)}%")
print(f"Top 30 most common words")
most_common = [(idx + 1, x[0], x[1], round(x[1]/total_wordcount,5)) for idx, x in enumerate(word_frequencies.most_common(30))]

print(word_frequencies.most_common(6))
print(type(word_frequencies.most_common(6)))
arr = np.array([(rank, count[1]) for rank, count in enumerate(word_frequencies.most_common(1000))]) #np.array(list(word_frequencies.most_common(1000)))
print(arr)
x, y = arr[:,0], arr[:,1]
print(tabulate(most_common, headers=["Rank", "Term", "Frequency", "Percentage"]))
fig = plt.figure()
plt.plot(x,y)   # plt.loglog for a log-log plot
plt.xlabel('rank')
plt.ylabel('frequency')
fig.savefig('word_distribution.png')
plt.loglog(x,y)   # plt.loglog for a log-log plot
plt.xlabel('rank')
plt.ylabel('frequency')
fig.savefig('word_distribution_log.png')


for stopword in stopwords:
    del word_frequencies[stopword]

for punctuation in string.punctuation:
    del word_frequencies[punctuation]

print(f"Top 30 most common words (after removing stopwords/punctuation)")
most_common = [(idx + 1, x[0], x[1], round(x[1]/total_wordcount,5)) for idx, x in enumerate(word_frequencies.most_common(30))]
arr = np.array([(rank, count[1]) for rank, count in enumerate(word_frequencies.most_common(1000))])
x, y = arr[:,0], arr[:,1]
print(tabulate(most_common, headers=["Rank", "Term", "Frequency", "Percentage"]))
fig = plt.figure()
plt.plot(x,y)   # plt.loglog for a log-log plot
plt.xlabel('rank')
plt.ylabel('frequency')
fig.savefig('word_distribution_without_stopwords.png')
plt.loglog(x,y)   # plt.loglog for a log-log plot
plt.xlabel('rank')
plt.ylabel('frequency')
fig.savefig('word_distribution_without_stopwords_log.png')