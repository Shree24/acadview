# QUESTION 1

import re
emails="zuck26@facebook.com"  "page33@google.com"  "jeff42@amazon.com"
pattern= r'(\w+)@([A-Z0-9]+)\.([A-Z]{1,3})'
a=re.findall(pattern, emails, flags=re.IGNORECASE)
print(a)

# END

# QUESTION 2
import re
text ="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
t=re.findall(r'\bB\w+', text,flags=re.IGNORECASE)
print(t)                                               # print words starting with B or cb

# END

# QUESTION 3

sentence = "A, very very; irregular_sentence"
import re
z=" ".join(re.split('[;,\s_]+', sentence))
print(z)

# END

# OPTIONAL QUESTION

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
import re
def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)                             # remove URLs
    tweet = re.sub('RT|cc', '', tweet)                                  # remove RT and cc
    tweet = re.sub('#\S+', '', tweet)                                   # remove hashtags
    tweet = re.sub('@\S+', '', tweet)                                   # remove mentions
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)  # remove punctuations
    tweet = re.sub('\s+', ' ', tweet)                                                     # remove extra whitespace
    return tweet

print(clean_tweet(tweet))