import requests
from bs4 import BeautifulSoup
from help import stp_word,pos,neg
from nltk.corpus import stopwords
import textstat
from nltk.tokenize import word_tokenize,sent_tokenize
import copy
import pandas as pd

output=[]
data=pd.read_excel('Input.xlsx')

j=0
print("please wait till all completed....")
stop_word=stp_word()#collecting stop words
#getting possitive & negative words data
posi=pos()
negi=neg()
while j<len(data):
    row_maker=[]
    row_maker.append(data.iloc[j][0])
    url=data.iloc[j][1]
    row_maker.append(url)
    headers = {
        
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    try:#sending request for article data
        r=requests.get(url,headers=headers)
        htmlcon=r.content
        soup=BeautifulSoup(htmlcon,'html.parser')
        s=soup.find("article").get_text()
    except:
        output.append(row_maker)
        j+=1
        print(j," no not done")
        continue   
    real_sen=copy.copy(s)
    s=s.lower()
    token=word_tokenize(s)#converting our text to list of words
    real_word=copy.copy(token)
    
    help_list=[]
    for i in token:
        if i in stop_word:
            help_list.append(i)#collecting stop words from token to remove in next step
        elif i.isnumeric():
            help_list.append(i)
        elif i=='”' or i=='“' or i=='’':
            help_list.append(i)    


    for i in help_list:
        token.remove(i)#remove collected stop words from token
 
    poss=[]
    negg=[]
    #collecting possitive and negative words from token
    for i in token:
        if i in posi:
            poss.append(i)
        if i in negi:
            negg.append(i)   
    pos_score=len(poss)#calculating possitive word score
    neg_score=len(negg)#calculating negative word score
    com_word=[]
    syl_count=0
    per_pro_count=0
    no_sen=sent_tokenize(real_sen)
    avg_sen=len(real_word)/len(no_sen)#calculating Average sentence length
    
    row_maker.append(pos_score)
    
    row_maker.append(neg_score)
    
    row_maker.append((pos_score-neg_score)/(pos_score+neg_score+0.000001)) #calculating and storing polarity score in a list
    
    row_maker.append((pos_score+neg_score)/(len(token)+0.000001)) #calculating and storing subjective score in a list
    
    row_maker.append(avg_sen)
    for i in real_word:
        if textstat.syllable_count(i)>2:#collecting complex words
        
            com_word.append(i)
        syl_count+=textstat.syllable_count(i)#counting syllables
        if i in ["i","me","you","he","she","it","him","her","we","us","they","them"]:
            per_pro_count+=1 #counting Personal Pronouns
    per_com= (100*len(com_word))/len(real_word)#calculating persentage of complex word
    fog_index=0.4*(avg_sen+per_com) #calculating fog index
    no_char=textstat.char_count(real_sen,ignore_spaces=True)  #calculating no of character present in text     
    
    row_maker.append(per_com)

    row_maker.append(fog_index)
    
    row_maker.append(avg_sen)
    
    row_maker.append(len(com_word))# storing complex word count
    
    row_maker.append(len(token))# storing cleaned word count
    
    row_maker.append(syl_count/len(real_word)) #calculating and storing Syllable per word
    

    
    row_maker.append(per_pro_count) #storing personal pronouns count
    avg_word_len=no_char/len(real_word)#calculating average word length
    row_maker.append(avg_word_len)
    output.append(row_maker) #adding our Row list to another list to make pandas data frame
    j+=1
    print(j," no done")
out=pd.DataFrame(output,columns=['URL_ID','URL','POSITIVE SCORE','NEGATIVE SCORE','POLARITY SCORE','SUBJECTIVITY SCORE','AVG SENTENCE LENGTH','PERCENTAGE OF COMPLEX WORDS','FOG INDEX','AVG NUMBER OF WORDS PER SENTENCE','COMPLEX WORD COUNT','WORD COUNT','SYLLABLE PER WORD','PERSONAL PRONOUNS','AVG WORD LENGTH'])#creating pandas data frame with our data to covert it into excel
out.to_excel('Output.xlsx')
print("all complted......")
print("your output file is ready")