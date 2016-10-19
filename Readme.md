Question intent detection 'when','what','who','unknown' type

Dependencies:NLTK,RE,tensorflow,theano,scikit,pandas

Run : python pos.py 
1.This repository consists of codes for question detection in three ways:
1.Rule based grammar
python pos.py 
2.Naive bayes
python nb.py
3.Neural netowrk
a)This code take care of preprocessing,labelling/padding,vocabulary building  of data set
python corpus_handle.py
b)Training the model
python train_model.py
c)Testing the model
python test_model.py
