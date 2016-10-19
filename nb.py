import numpy
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
#Insample data 
what=pd.read_csv('/home/kirti/Downloads/question-classifier-cnn-tensorflow-master/corpus/qa_data.what',sep='\t',names=["question"])
what['Label']='What'
when=pd.read_csv('/home/kirti/Downloads/question-classifier-cnn-tensorflow-master/corpus/qa_data.when',sep='\t',names=["question"])
when['Label']='When'
who= pd.read_csv('/home/kirti/Downloads/question-classifier-cnn-tensorflow-master/corpus/qa_data.who',sep='\t',names=["question"])
who['Label']='Who'
affirmative=pd.read_csv('/home/kirti/Downloads/question-classifier-cnn-tensorflow-master/corpus/qa_data.affirmative',sep='\t',names=["question"])
affirmative['Label']='Who'
other = pd.read_csv('/home/kirti/Downloads/question-classifier-cnn-tensorflow-master/corpus/qa_data.other',sep='\t',names=["question"])
other['Label']='Other'
insample = pd.concat([what,when,who,affirmative,other],axis=0)
count_vectorizer = CountVectorizer()
#creating features from insample messages
counts = count_vectorizer.fit_transform(insample['question'].values)
#Taking final category as targets
targets = insample['Label'].values
classifier = MultinomialNB()
classifier.fit(counts, targets)
#Outsample data prediction and accuracy detection
outsample=pd.read_csv('/home/kirti/Downloads/question-classifier-cnn-tensorflow-master/corpus/forcasestudy_outsample.csv',sep='\t',names=['question'])
example_counts_outsample = count_vectorizer.transform(outsample['question'])
predictions_outsample = classifier.predict(example_counts_outsample)
print predictions_outsample
#print(metrics.accuracy_score(predictions_outsample,outsample['Final']))
#Outsample data prediction and accuracy detection
#example_counts_insample = count_vectorizer.transform(insample['message'])
#predictions_insample = classifier.predict(example_counts_insample)
#print(metrics.accuracy_score(predictions_insample,insample['Final Category']))
