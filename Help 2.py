#!/usr/bin/env python
# coding: utf-8

# In[ ]:


spacy.lang.en.stop_words


# In[120]:


import pandas as pd
import numpy as np
import spacy
import gensim
import pyLDAvis.gensim_models
from spacy.lang.en.stop_words import STOP_WORDS
from spacy import displacy
from spacy.matcher import Matcher
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer


# ![image.png](attachment:image.png) 

# In[4]:


nlp=spacy.blank('en')


# In[12]:


doc1=nlp('''ioneer Building, San Francisco, headquarters of OpenAI

Sam Altman, CEO of OpenAI ChatGPT was fine-tuned on top of GPT-3.5 using supervised learning as well as reinforcement learning.[5] Both approaches used human trainers to improve the model's performance. In the case of supervised learning, the model was provided with conversations in which the trainers played both sides: the user and the AI assistant. In the reinforcement step, human trainers first ranked responses that the model had created in a previous conversation. These rankings were used to create 'reward models' that the model was further fine-tuned on using several iterations of Proximal Policy Optimization (PPO).[6][7] Proximal Policy Optimization algorithms present a cost-effective benefit to trust region policy optimization algorithms; they negate many of the computationally expensive operations with faster performance.[8][9] The models were trained in collaboration with Microsoft on their Azure supercomputing infrastructure.

In addition, OpenAI continues to gather data from ChatGPT users that could be used to further train and fine-tune ChatGPT. Users are allowed to upvote or downvote the responses they receive from ChatGPT; upon upvoting or downvoting, they can also fill out a text field with additional feedback.[10][11][12]

Features and limitations

Cropped screenshot of a conversation with ChatGPT, December 30, 2022 Although the core function of a chatbot is to mimic a human conversationalist, ChatGPT is versatile. For example, it has the ability to write and debug computer programs; to compose music, teleplays, fairy tales, and student essays; to answer test questions (sometimes, depending on the test, at a level above the average human test-taker);[13] to write poetry and song lyrics;[14] to emulate a Linux system; to simulate an entire chat room; to play games like tic-tac-toe; and to simulate an ATM.[15] ChatGPT's training data includes man pages and information about Internet phenomena and programming languages, such as bulletin board systems and the Python programming language.[15]

In comparison to its predecessor, InstructGPT, ChatGPT attempts to reduce harmful and deceitful responses.[16] In one example, whereas InstructGPT accepts the premise of the prompt "Tell me about when Christopher Columbus came to the US in 2015" as being truthful, ChatGPT acknowledges the counterfactual nature of the question and frames its answer as a hypothetical consideration of what might happen if Columbus came to the U.S. in 2015, using information about Columbus' voyages and facts about the modern world – including modern perceptions of Columbus' actions.[6]

Unlike most chatbots, ChatGPT remembers previous prompts given to it in the same conversation; journalists have suggested that this will allow ChatGPT to be used as a personalized therapist.[17] To prevent offensive outputs from being presented to and produced from ChatGPT, queries are filtered through OpenAI's company-wide moderation API,[18][19] and potentially racist or sexist prompts are dismissed.[6][17]

ChatGPT suffers from multiple limitations. OpenAI acknowledged that ChatGPT "sometimes writes plausible-sounding but incorrect or nonsensical answers".[6] This behavior is common to large language models and is called hallucination.[20] The reward model of ChatGPT, designed around human oversight, can be over-optimized and thus hinder performance, otherwise known as Goodhart's law.[21] ChatGPT has limited knowledge of events that occurred after 2021. According to the BBC, as of December 2022 ChatGPT is not allowed to "express political opinions or engage in political activism".[22] Yet, research suggests that ChatGPT exhibits a pro-environmental, left-libertarian orientation when prompted to take a stance on political statements from two established voting advice applications.[23] In training ChatGPT, human reviewers preferred longer answers, irrespective of actual comprehension or factual content.[6] Training data also suffers from algorithmic bias, which may be revealed when ChatGPT responds to prompts including descriptors of people. In one instance, ChatGPT generated a rap indicating that women and scientists of color were inferior to white and male scientists.[24][25]

Service ChatGPT was launched on November 30, 2022, by San Francisco-based OpenAI, the creator of DALL·E 2 and Whisper. The service was launched as initially free to the public, with plans to monetize the service later.[26] By December 4, OpenAI estimated ChatGPT already had over one million users.[10] CNBC wrote on December 15, 2022, that the service "still goes down from time to time".[27] The service works best in English, but is also able to function in some other languages, to varying degrees of success.[14] Unlike some other recent high-profile advances in AI, as of December 2022, there is no sign of an official peer-reviewed technical paper about ChatGPT.[28]

According to OpenAI guest researcher Scott Aaronson, OpenAI is working on a tool to attempt to watermark its text generation systems so as to combat bad actors using their services for academic plagiarism or for spam.[29][30] The New York Times relayed in December 2022 that the next version of GPT, GPT-4, has been "rumored" to be launched sometime in 2023.[17]

Reception and implications Positive reactions ChatGPT was met in December 2022 with generally positive reviews; The New York Times labeled it "the best artificial intelligence chatbot ever released to the general public".[31] Samantha Lock of The Guardian noted that it was able to generate "impressively detailed" and "human-like" text.[32] Technology writer Dan Gillmor used ChatGPT on a student assignment, and found its generated text was on par with what a good student would deliver and opined that "academia has some very serious issues to confront".[33] Alex Kantrowitz of Slate magazine lauded ChatGPT's pushback to questions related to Nazi Germany, including the claim that Adolf Hitler built highways in Germany, which was met with information regarding Nazi Germany's use of forced labor.[34]

In The Atlantic's "Breakthroughs of the Year" for 2022, Derek Thompson included ChatGPT as part of "the generative-AI eruption" that "may change our mind about how we work, how we think, and what human creativity really is".[35]

Kelsey Piper of the Vox website wrote that "ChatGPT is the general public's first hands-on introduction to how powerful modern AI has gotten, and as a result, many of us are [stunned]" and that ChatGPT is "smart enough to be useful despite its flaws".[36] Paul Graham of Y Combinator tweeted that "The striking thing about the reaction to ChatGPT is not just the number of people who are blown away by it, but who they are. These are not people who get excited by every shiny new thing. Clearly, something big is happening."[37] Elon Musk wrote that "ChatGPT is scary good. We are not far from dangerously strong AI".[36] Musk paused OpenAI's access to a Twitter database pending a better understanding of OpenAI's plans, stating that "OpenAI was started as open-source and non-profit. Neither is still true."[38][39] Musk had co-founded OpenAI in 2015, in part to address existential risk from artificial intelligence, but had resigned in 2018.[39]

Google CEO Sundar Pichai upended the work of numerous internal groups in response to the threat of disruption by ChatGPT.[40] In December 2022, Google internally expressed alarm at the unexpected strength of ChatGPT and the newly discovered potential of large language models to disrupt the search engine business, and CEO Sundar Pichai "upended" and reassigned teams within multiple departments to aid in its artificial intelligence products, according to The New York Times.[40] The Information reported on January 3, 2023 that Microsoft Bing was planning to add optional ChatGPT functionality into its public search engine, possibly around March 2023.[41][42]

Stuart Cobbe, a chartered accountant in England & Wales, decided to the test the ChatGPT chatbot by entering questions from a sample exam paper on the ICAEW website and then entering its answers back into the online test. ChatGPT scored 42% which, while below the 55% pass mark, was considered a reasonable attempt.''')


# In[15]:


count=0
for token in doc1:
    count=count+1
print(count)


# In[16]:


doc1[10]


# In[17]:


from spacy.lang.en.stop_words import STOP_WORDS


# In[18]:


nlp=spacy.load('en_core_web_sm')


# In[96]:


t_count=0
for token in doc1:
    t_count=t_count+1
print(' The no of tokens:',t_count)

s_count=0
for token in doc1:
    if token.is_stop == False:
        s_count=s_count+1
print('\n The no of non-stop words:',s_count,'-----token.is_stop')

p_count=0
for token in doc1:
    if token.is_punct == False:
        p_count=p_count+1
print('\n The no of non-punctuations:',p_count,'-----token.is_punct')

lp_count=0
for token in doc1:
    if token.is_left_punct == True:
        lp_count=lp_count+1
print('\n The no of left punctuations:',lp_count, '-----token.is_left_punct')

rp_count=0
for token in doc1:
    if token.is_right_punct == True:
        rp_count=rp_count+1
print('\n The no of right punctuations:',rp_count,'-----token.is_right_punct')


a_count=0
for token in doc1:
    if token.is_alpha == True:
        a_count=a_count+1
print('\n The no of alphabets:',a_count,'-----token.is_alpha')


d_count=0
for token in doc1:
    if token.is_digit == True:
        d_count=d_count+1
print('\n The no of digits:',d_count,'-----token.is_digit')

n_count=0
for token in doc1:
    if token.like_num == True:
        n_count=n_count+1
print('\n The count of like numbers:',n_count,'-----token.like_num')



l_count=0
for token in doc1:
    if token.is_lower == True:
        l_count=l_count+1
print('\n The no of lower case tokens:',l_count,'-----token.is_lower')


u_count=0
for token in doc1:
    if token.is_upper == True:
        u_count=u_count+1
print('\n The no of upper case tokens:',u_count,'-----token.is_upper')


t_count=0
for token in doc1:
    if token.is_title == True:
        t_count=t_count+1
print('\n The no of title cases:',t_count,'-----token.is_title')

q_count=0
for token in doc1:
    if token.is_quote == True:
        q_count=q_count+1
print('\n The no of quotes:',q_count,'-----token.is_quote')



URL_count=0
for token in doc1:
    if token.like_url==True :
        URL_count=URLcount+1
print('\n The count of URLs' , URL_count,'------token.like_url')
    
e_count=0 
for token in doc1:
    if token.like_email==True:
        e_count=e_count+1
print('\n The count of Emails', e_count,'-----token.like_email')


print('\n print(token.text,   , token.pos_)')
print('\n  print(token.text,,token.tag_)')

print('\n pos_count=doc1.count_by(spacy.attrs.POS)')

sent_count=0
for sent in doc1.sents:
    sent_count=sent_count+1
print('\nsent count is','--',sent_count,'-----doc1.sent')

print('\n print(token.text,,token.dep_)')

print('\n print(token.text,,token.head)')    

print('\n for chunk in doc1.noun_chunks: print(chunk.text, ,chunk.label_')


# In[33]:


#LIST 

text_2=['Today is Monday','Tomorrow is Tuesday',
       'Yesterday was a holiday']

# Tokens

for sentence in nlp.pipe(text_2):
    print(sentence)
    for token in sentence:
        print(len(token))


# In[35]:


#TUPLE

text_3=('Today is Monday','Tomorrow is Tuesday',
       'Yesterday was Sundaya,a holiday')

for sent in nlp.pipe(text_3):
    print(sent)
    for token in sent:
        print(len(token))


# In[36]:


text_4=[('Today is Monday'),('Tomorrow is Tuesday'),
       ('Yesterday was Sundaya,a holiday')]


sent_count=0
for sent in nlp.pipe(text_4):
    sent_count=sent_count+1
    print(sent_count,'=>',sent)
    for token in sent:
        print(token)


# In[37]:


text_df=pd.DataFrame(text_2,columns=['Sentence'])
text_df


# In[39]:


# nlp.pipe(text_df['Sentence'])#

for sent in nlp.pipe(text_df['Sentence']):
    print(sent)
    for token in sent:
        print(token)


# In[85]:


## Separating doc into sentences
X=[]
for sent in doc1.sents:
    print(sent)
    X.append(sent.text)
    


# In[81]:


X


# In[84]:





# In[44]:


sent_count=0
for sent in doc1.sents:
    sent_count=sent_count+1
print(sent_count)


# In[48]:


#tagger

for token in doc1:
    print(token.text,'==>',token.tag_)
    
spacy.explain('NNS')


# In[50]:


##POS
for token in doc1:
    print(token.text,'==>',token.pos_)


# In[52]:


pos_count=doc1.count_by(spacy.attrs.POS)
pos_count


# In[56]:


from spacy import displacy
displacy.render(doc1,style='dep')


# In[58]:


options={'compact':'True','color':'blue'}


displacy.render(doc1,style='dep',options=options)


# In[86]:


doc2=pd.DataFrame(X, columns=['X'])
doc2


# In[78]:


X


# In[87]:


token=[]
for sent in nlp.pipe(doc2['Sentence']):
    if sent.has_annotation('DEP'):
        token.append([word.text for word in sent] )
token


# In[88]:


#Converting into dataframe

token=[]
pos=[]
for sent in nlp.pipe(doc2['X']):
    if sent.has_annotation('DEP'):
        token.append([word.text for word in sent] )
        pos.append([word.pos_ for word in sent])
print(token)
print(pos)


# In[90]:


# Updating text_df

doc2['Token']=token
doc2['POS']=pos


# In[91]:


doc2


# In[97]:


## Noun chunks

for chunk in doc1.noun_chunks:
    print(chunk.text, '==>',chunk.label_)


# In[107]:


ent_list2=[]
for ent in doc1.ents:
    print(ent.text,'==>',ent.label_)
    ent_list2.append(ent.label_)
    


# In[108]:


ent_list2


# In[100]:


ent_list=[(ent.text,ent.label_) for ent in doc1.ents]


# In[101]:


ent_list


# In[111]:


ent_list1=[]
for ent in doc1.ents:
    ent_list1.append(ent.label_)
print(ent_list1)


# In[112]:


from collections import Counter
Counter(ent_list1)


# In[114]:


most_ent=[]
for ent in doc1.ents:
    most_ent.append(ent.text)
print(most_ent)


# In[115]:


# Most common

Counter(most_ent).most_common()


# In[116]:


Counter(most_ent).most_common(10)


# In[118]:


print(len(doc1.ents))


# In[129]:


##MAtching

matcher_2=Matcher(nlp.vocab)
pattern_2=[{'text':'OpenAI'}]
matcher_2.add('Pattern2',[pattern_2])
match_2=matcher_2(doc1)


# In[130]:


for match_id,start,end in match_2:
    span=doc1[start:end]
    print(span)


# In[132]:


matcher_3=Matcher(nlp.vocab)
pattern_3=[{'LEMMA':'OpenAi'},
          {'LEMMA':' '}]


matcher_3.add('Pattern3',[pattern_3])
match_3=matcher_3(doc1)


# In[138]:


for match_id,start,end in match_3:
    span=doc1[start:end]
    print(span)


# In[135]:


matcher_4=Matcher(nlp.vocab)
pattern_4=[{'IS_ALPHA': True},
           {'IS_DIGIT':True}]

matcher_4.add('Pattern4',[pattern_4])
match_4=matcher_4(doc1)


# In[137]:


for match_id,start,end in match_4:
    span=doc1[start:end]
    print(span)


# In[141]:


'''
pattern_3=[{'LEMMA':'language'}]
pattern_4=[{'IS_ALPHA': True},
           {'IS_DIGIT':True}]

pattern_5=[{'LEMMA':
            {'IN':['launch','discover','find',
        'invent','create','develop','innovate',
        'form','initiate']}}]
pattern_6=[{'LENGTH':{'>=':15}}]

pattern_7=[{'LENGTH':{'==':2}}]

pattern_10=[{"ENT_TYPE":'PERSON'}]
'''


# In[143]:


#bag of word

words_list=[]
for text in texts:
    doc=nlp(text)
    text_words=[]
    for token in doc:
        if token.is_stop==False and token.is_punct==False and token.like_num==False and token.text!='\n':
            text_words.append(token.lemma_)
    words_list.append(text_words)


# In[ ]:


print(len(words_list[1]))


# In[ ]:


corpus=[]
from gensim.corpora import Dictionary


# In[ ]:


dict=Dictionary(words_list)
type(dict)


# In[ ]:


for word in words_list:
    corpus.append(dict.doc2bow(word))

print(corpus)


# In[ ]:


#LDA

lda=gensim.models.ldamodel.LdaModel(corpus=corpus,
                                   num_topics=5,
                                   id2word=dict)

type(lda)

lda.print_topics()

lda.print_topics()[:2]


# This section serves as a short reminder on what we are trying to do. CareerVillage, in its essence, is like Stackoverflow or Quora but for career questions. Users can post questions about any careers like computer science, pharmacology, aerospace engineering etc, and volunteer professionals try their best to answer the questions.
# 
# When a new question comes in, CareerVillage recommends that question to a specific professional who is suitable to answer that question. In order to maximize the chance that a user’s questions get answered, CareerVillage needs to send the right question to the most apt professional. This is where our job comes in! We have to design a recommendation system that takes in a newly posted question, and outputs the professionals who are most suitable to answer that question.

# In[144]:


lda.get_term_topics('game')

lda.get_term_topics('politics')

lda.get_term_topics('famous')


# In[ ]:


#VIzualisation

pyLDAvis.enable_notebook()


plot=pyLDAvis.gensim_models.prepare(lda,
                                    corpus=corpus,
                                   dictionary=lda.id2word)

plot


# In[ ]:


#Sentiment analysis


# In[ ]:


blob1=TextBlob(text1)

# We want to have the sentiment

blob1.sentiment


# In[ ]:


#TFIDF vectors

from sklearn.feature_extraction.text import TfidfVectorizer


# In[ ]:


tf=TfidfVectorizer()

features=tf.fit_transform(data)

print(features)


# In[ ]:


#Clustering

#elbow
SSD=[]
for k in range(1,10):
    kmeans=KMeans(n_clusters=k, random_state=10)
    kmeans.fit(features)
    SSD.append(kmeans.inertia_)
plt.plot(range(1,10),SSD);


## Applying silhouette_score
from sklearn.metrics import silhouette_score
SS=[]
for k in range(2,11):
    kmeans=KMeans(n_clusters=k, random_state=10)
    kmeans.fit(features)
    SS.append(silhouette_score(features,kmeans.predict(features)))
    
plt.plot(range(2,11),SS);


# In[ ]:


kmeans=KMeans(n_clusters=5,random_state=10)
kmeans.fit(features)


kmeans.labels_


# In[ ]:


bbc['Cluster']=kmeans.labels_

#dimension reduction using TNSE

from sklearn.manifold import TSNE

tsne=TSNE(n_components=2,perplexity=30,random_state=10)

features_tsne=tsne.fit_transform(features)

features_tsne

features_tsne.shape

#vizualization

plt.figure(figsize=(10,8))
plt.scatter(features_tsne[:,0],features_tsne[:,1]);

plt.figure(figsize=(10,8))
plt.scatter(features_tsne[:,0],features_tsne[:,1],c=bbc['Cluster']);

