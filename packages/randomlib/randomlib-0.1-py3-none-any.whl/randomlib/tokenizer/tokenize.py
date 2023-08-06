class Tokenize:
    def __init__(self, code):
        print("Tokenize instance initialized..")
        self.lang = code

    def sentence_tokenize_mr(self, txt):
        punc_for_sentence_end = '''.!?'''
        sentences = []
        string = ""
        for i in txt:
            if i not in punc_for_sentence_end:
                string += i
            else:
                string += i
                sentences.append(string)
                string = ""
        print(sentences)
        
    def sentence_tokenize(self,txt):
        if (self.lang == 'mr'):
            self.sentence_tokenize_mr(txt)

    def word_tokenize_mr(self, txt,punctuation):
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        if punctuation:
            str=""
            tokens=[]
            for ele in txt:
                if ele in punc:
                    if str:
                        tokens.append(str)
                        str=""
                    tokens.append(ele)
                    # txt = txt.replace(ele, "")
                elif ele == " ":
                    if str: #to ensure that 
                        tokens.append(str)
                        str=""
                else:
                    str+= ele
            if str: #for the last word in a text that might not be ending with a punctuation mark
                tokens.append(str)
                str=""
            # print(tokens)
            return tokens
        else:
            for ele in txt:
                if ele in punc:
                    txt = txt.replace(ele, " ") # replace by " "
            x = txt.split()
            # print(x)
            return x
        
    def word_tokenize(self,line,punctuation=True):
        #punctuation :False ->doesnot retain punctuations
        #punctuation :True ->creates a new token for punctuation mark
        if (self.lang == 'mr'):
            result =self.word_tokenize_mr(line,punctuation)
            return result


