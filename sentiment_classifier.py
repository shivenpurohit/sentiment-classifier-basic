import matplotlib.pyplot as plt

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(word):
    for punctuation in punctuation_chars:
        if(punctuation in word):
            word=word.replace(punctuation,'')
    return word

def get_neg(sentences):
    #split using whitespaces
    sentences_arr = sentences.split()
    count_neg=0
    for word in sentences_arr:
        if(strip_punctuation(word) in negative_words):
            count_neg+=1
    return count_neg

def get_pos(sentences):
    #split using whitespaces
    sentences_arr = sentences.split()
    count_pos=0
    for word in sentences_arr:
        if(strip_punctuation(word) in positive_words):
            count_pos+=1
    return count_pos

f=open("project_twitter_data.csv",'r')
twitter_data= f.read().strip()
f.close()

f=open("resulting_data.csv",'w')
f.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score, Sentiment\n')
tweets = twitter_data.split('\n')

for i in range(len(tweets)):
    if(i==0):
        continue
    data=tweets[i]
    data=data.split(',')
    tweet=data[0].strip()
    retweet_count=data[1].strip()
    reply_count=data[1].strip()
    
    pos_count=get_pos(tweet)
    neg_count=get_neg(tweet)
    net_score=pos_count - neg_count
    if(net_score>0):
        sentiment='Positive'
    elif(net_score==0):
        sentiment='Neutral'
    else:
        sentiment='Negative'
    f.write(retweet_count+','+reply_count+','+str(pos_count)+','+str(neg_count)+','+str(net_score)+','+sentiment+'\n')
f.close()


## plot graph for resulting data (optional)
f=open("resulting_data.csv",'r')
resulting_data= f.read().strip().split('\n')
f.close()

retweets,replies,pos_score,neg_score,net_score,sentiment=[],[],[],[],[],[]
dict_header={'retweets':'Number of Retweets','replies':'Number of Replies','pos_score':'Positive Score','neg_score':'Negative Score','net_score':'Net Score','setiment':'Sentiment'}
dict_sentiment={'Negative':-1,'Positive':1,'Neutral':0}

for i in range(len(resulting_data)):
    if(i==0):
        continue
    data=resulting_data[i]
    data=data.split(',')
    retweets.append(int(data[0].strip()))
    replies.append(int(data[1].strip()))
    pos_score.append(int(data[2].strip()))
    neg_score.append(int(data[3].strip()))
    net_score.append(int(data[4].strip()))
    sentiment.append(dict_sentiment[data[5]])

# plot scatter graph
plt.scatter(net_score, retweets)
plt.xlabel(dict_header['net_score'])
plt.ylabel(dict_header['retweets'])
plt.show()