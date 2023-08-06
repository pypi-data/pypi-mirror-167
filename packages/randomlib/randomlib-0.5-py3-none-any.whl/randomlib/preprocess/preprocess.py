import re
from randomlib.tokenizer import Tokenize

class Preprocess:
    stopwords =[]
    def __init__(self):
        # print("Preprocess instance initialized..")
        if not Preprocess.stopwords:
            #Array is empty
            f1 = open('Marathi_stopwords.txt', 'r',encoding="utf8")
            Lines = f1.readlines()
            #Strips the newline character
            for line in Lines:
                Preprocess.stopwords.append(line.strip())
            # print(Preprocess.stopwords)
            # print(len(Preprocess.stopwords))
    
    #Remove URLs from a sample string
    def remove_url(self , text):
        return re.sub(r"http\S+", "", text)


   #obj = Tokenize('mr')
   #txt = "Add marathi text here"
   #tokenslist = obj.word_tokenize_mr(txt) 
    def remove_stopwords(self , text):
        newlist = [] # edit this line. Load the text data here
        t = Tokenize.Tokenize('mr')
        textlist = t.word_tokenize(text , False)
        for word in textlist:
            if word not in Preprocess.stopwords:
                newlist.append(word)
            # else:
            #     print(word)
        return newlist
    

        '''
        Remove  non Dev text
        option to remove:
        i.English
        ii.Emojis
        iii.English digits?:retain them
        '''
    

