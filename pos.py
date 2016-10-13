import nltk
from nltk import word_tokenize,pos_tag
import re
#file containing preprocessed questions and sample questions 
file = open('ques2.txt','r')
#Word tokenisation and pos tagging and implementing rule based learning to detect quest
for question in file:
  a=word_tokenize(question.lower())
  b=pos_tag(a)
  f=[]
  print question
  print '@@@@@@@@'
  for i in b:
       f.append(i[1])
  for i in a:
      if 'who' in i:
         print 'who type'
         break
      elif i in ['how','where','which','why']:
         print 'unknown'
         break             
  for u in range(0,len(f)):
            j = len(f) 
            if((f[u] in'WP') and (f[u+1]in'NN')):
               print 'wHen type'
#               print f[u]
#               print f[u+1]
               break
            elif(f[u] in'(WRB)'):
               print'when type' 
               print f[u]
               break
            elif(((f[u] in'WP') and (f[u+1]in'VBZ')) or((f[u] in 'WP')and (f[u+1] in 'NN') and (f[u+2] in 'VBZ'))):
               print 'wHat type'
               break  
            elif(((f[u] in 'VBZ' and (f[u+1] in 'EXT')) or (((f[u] in 'VBZ') and (f[u+1] in 'DT'))and (f[u+1] in 'PRP')))): 
               print 'affirmative'
#               print f[u]
#               print f[u+1] 
               break  
            elif((f[j-4] in 'VB') and (f[j-3] in 'RB') and (f[j-2] in'PRP') or(f[j-3] in 'VB') or(f[j-1] in 'VB')):
               print 'affirmative' 
               break 
            elif():
              print 'unknown'   




     
