'''Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.
Example:

Assume that words.txt has the following content:

the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1'''






# My logic 

from operator import itemgetter

with open("words.txt", "r") as f:
    words = f.read().split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

sorted_freq = sorted(freq.items(), key=itemgetter(1), reverse=True)

for word, count in sorted_freq:
    print(word, count)







# ChatGPT coded 

# tr -s ' ' '\n' < words.txt |
# grep -v '^$' |
# sort |
# uniq -c |
# sort -nr |
# awk '{print $2, $1}'