import nltk
import os

#set Java pth - compulsary!
java_path = "C:\Program Files\Java\jre1.8.0_171"
os.environ['JAVAHOME'] = java_path

#install nltk and stanfordcorenlp packages first before the codes,
# install in settings-->interpreter-->add packages-->search stanfordcorenlp-->install
from stanfordcorenlp import StanfordCoreNLP

#download stanfordcorenlp zip under a directory
#download the Chinese modal under the same directory for processing Chinese texts
nlp = StanfordCoreNLP(r'F:/stanford-corenlp-full-2018-02-27/', lang='zh')

sentence = '清华大学位于北京。'
print (nlp.word_tokenize(sentence)) #中文分詞
print (nlp.pos_tag(sentence)) #中文詞類標注
print (nlp.ner(sentence)) #中文實體鑒別
print (nlp.parse(sentence)) #中文短語結構剖析
print (nlp.dependency_parse(sentence)) #中文依存關係剖析