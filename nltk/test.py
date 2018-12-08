from nltk.tokenize import sent_tokenize,word_tokenize

#https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/

import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':'s-access-detail-page'}):
            tet = link.get('title')
            words=word_tokenize(tet)
            #print(tet)
            freq={}
            for w in words:
                if w in freq:
                    freq[w]=freq[w]+1
                else:
                    freq[w]=1
            print(freq)
web(1,'https://www.amazon.es/ADDTOP-Cargador-Impermeable-Li-Pol%C3%ADmero-Smartphone/dp/B077TP3QRR?pd_rd_wg=afG9P&pd_rd_r=867f5b4c-8314-4c12-9d82-b6bb5839117e&pd_rd_w=ToSnj&ref_=pd_gw_simh&pf_rd_r=AGHEC7Q1588Q5NPZ24A2&pf_rd_p=3a9a4293-41a1-5c27-8386-b1269283e406')