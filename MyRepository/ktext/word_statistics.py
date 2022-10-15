from PyPDF2 import PdfReader
from docx import Document
import matplotlib.pyplot as plt

import collections
import csv

from sympy import Not 


class Ktext:
    s1=["dor", "tor", "sor", "eiro", "ista", "nte", "rio"]  # Agente causador
    s2=["dade", "ência", "ez", "eza", "ice", "ície", "ismo", "or", "ude", "ume", "ura"] # Qualidade
    s3=["ado", "ato", "aria", "douro", "tório", "tério"] # Local
    s4=["ia", "ismo", "ica", "tica"] # Doutrina
    s5=["al", "agem", "ada", "ama", "ame", "ário", "aria", "edo", "eiro", "eira", "ena"] # Coletivo
    s6=["az", "ento","lento", "into", "enho", "onho", "oso", "udo"] # Intensidade
    s7 = ["eo","aco", "iaco", "aco", "aico", "ano", "ão", "enho", "eno", "ense", "ês", "eu", "ino", "ista"] # Possui a natureza de...
    s8= ["ável", "ível", "óvel", "úvel", "iço", "ivo"] # possibilidade
    s9 = ["ada", "agem", "ança", "aria", "eria", "ata", "ção", "ura", "ela", "ença", "ência", "mento", "or"] # Ação
    s10 = ["ear", "ejar"] # Ação que se repete
    s11 = ["icar", "itar", "iscar"] # Ação diminutiva que se repete
    s12= ["ecer","escer"] # Tornar-se
    s13 = ["ão", "aço", "alhão", "aréu", "arra", "arrão", "eirão",  "uça"] # Aumentativos
    s14 = ["inho", "zinho", "acho", "icho",  "eco", "ela", "ote", "isco"] # Diminuitivo
    s15 = ["s", "ns", "es", "is", "eis", "ões", "ães", ]
    s16 = ["a", "o"] # Gênero

    def __init__(self, pdf_path) -> None:
        '''
        Return:
        n_pages:            Número de páginas do documento.
        suffixes:           Lista de todos sufixos que encontrei na internet.
        words:              Lista de todas palavras do texto, sem as principais pontuações.
        dic_words:          Dicionário contendo a contagem das palavras.

        '''
        self.path = pdf_path
        self._document = PdfReader(self.path)
        self.n_pages = self._document.numPages
        self.suffixes=self.__all_suffix()
        self.words = self.__extractor()
        self.dic_words = collections.Counter(self.words)


    def suffix_remove(self, word_list):
        '''
        not implemented...
        TODO: Fazer um jeito mais inteligente comparando os sufixos e avaliando o primitivo das palavras.
        
        '''
        candidate=[]
        primitivo={}
        for word in word_list:
            for suffix in self.suffixes:
                s=len(suffix)
                if word[-s]+suffix in word_list:
                    candidate.append(word)
                    if Not(word[-s] in primitivo):
                        primitivo[word[-s]]=word
                    else:
                        primitivo[word[-s]]='/'+word


    def __all_suffix(self) -> list:
        '''Retorna uma lista contendo todos sufixos'''
        suffix=[]
        count=1
        while True:
            try:
                suffix+=getattr(self,f's{count}')
                count+=1
            except AttributeError:
                break
        return suffix


    def __extractor_visitor_body(self, text, cm, tm, fontDict, fontSize):
        '''Uma função que funciona como filtro, ela funciona como mágica, mas funciona (PyPDF2).'''
        y = tm[5]
        if y > 50 and y < 680 and fontSize>11.5:
            self.parts.append(text)

    def __extractor(self) -> str:
        '''
        Fornece uma lista contendo todas as palavras e retira alguns caracteres especiais, talvez seja interessante fazer com regex.
        '''
        self.parts=[] # Usado em __extractor_visitor_body
        full_text=[] 
        
        for n_page in range (0,self.n_pages):
            page = self._document.pages[n_page]
            page.extract_text(visitor_text=self.__extractor_visitor_body)

            text = "".join(self.parts) # Recebe o resultado da página atual
            full_text.append(text)

        # Basic Treatment
        full_text=''.join(full_text)
        full_text=full_text.lower()
        full_text=full_text.replace('\n','')
        full_text=full_text.replace('.','')
        full_text=full_text.replace(',','')
        full_text=full_text.replace('-','')
        full_text=full_text.replace(':','')
        full_text=full_text.replace(';','')
        full_text=full_text.split(' ')
        return full_text
        


if __name__ == '__main__':
    # Definições
    file=r"E:\Estudos\Cursos\Normas Químicas\RDC 658 - Boas Práticas de Fabricação de Medicamentos\RDC 658 - Boas Práticas de Fabricação (3º).pdf"

    # Join the variable words (I used this before implement Class)
    # suffix = ['s']
    # fun=lambda x: x[:-1]+'/'+x if len(x)>2 and x[-1]=='s' and (x[:-1] in full_text) else x
    # full_text=list(map(fun,full_text))
    # del suffix, fun

    text=Ktext(file)

    words=text.words
    dic_words=text.dic_words


    # Save how csv
    with open('words_count.csv', 'w', encoding="utf-8") as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in dic_words.items():
            writer.writerow([key, value])

    # Save how txt
    with open('text.txt', 'w', encoding="utf-8") as disk:
        disk.write(text)