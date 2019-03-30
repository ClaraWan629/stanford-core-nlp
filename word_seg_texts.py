'''
created on 14 June 2018
by Clara Wan Mingyu
note: this is to read all files in one document and output it in one single file
'''
# START...
'''
import sys
import glob
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

# read the files globally under one directory
path = 'E:\\test_texts\\*.txt'
files = glob.glob(path)

mysents = []
for file in files:
    f = open(file, 'r', encoding='utf-8')
##mytext = f.read() # read the text as a whole; readlines() is for reading the text in lists of lines.
##mysents = nltk.sent_tokenize(mytext)
    mysents += f.readlines()
##outfile_name = f.name.strip('C:\\Users\\Clara\\Desktop\\WSD-new\\Fan\\.txt')
    f.close()

segged_sents = []
for sent in mysents:
    seg_sent = nlp.word_tokenize(sent)
    segged_sents.append(seg_sent)

output = open('E:\\nlp_output\\test_seg.txt', 'w', encoding='utf-8')
for item in segged_sents:
    for x in item:
        output.write('['+str(x)+']' + ' ')
    output.write('\n')
output.close()

print('All the texts have been successsfully segmented and saved to the directory.')
'''

# START...
'''
created on 14 June 2018
by Clara Wan Mingyu
note: this is to read and write files separatedly
'''
import sys
import glob
import nltk
import os

#set Java pth for the use of standfordcorenlp - compulsary!
java_path = "C:\Program Files\Java\jre1.8.0_171"
os.environ['JAVAHOME'] = java_path

#install nltk and stanfordcorenlp packages first before the codes,
# install in settings-->interpreter-->add packages-->search stanfordcorenlp-->install
from stanfordcorenlp import StanfordCoreNLP

#download stanfordcorenlp zip under a directory
#download the Chinese modal under the same directory for processing Chinese texts
nlp = StanfordCoreNLP(r'F:/stanford-corenlp-full-2018-02-27/', lang='zh')

# read the files globally under one directory
path = 'E:\\test_texts\\*.txt'
files = glob.glob(path)

for file in files:
    f = open(file, 'r', encoding='utf-8')
##mytext = f.read() # read the text as a whole; readlines() is for reading the text in lists of lines.
##mysents = nltk.sent_tokenize(mytext)
    mysents = f.readlines()
##outfile_name = f.name.strip('C:\\Users\\Clara\\Desktop\\WSD-new\\Fan\\.txt')
    outfile_name = f.name.strip('E:\\test_texts\\.txt')

    segged_sents = []

    for sent in mysents:
        seg_sent = nlp.word_tokenize(sent)
        segged_sents.append(seg_sent)

    output = open('E:\\nlp_output\\seg_' + outfile_name + '.txt', 'w', encoding='utf-8')
    for item in segged_sents:
        for x in item:
            output.write('[' + str(x) + ']' + ' ')
        output.write('\n')
    output.close()

    f.close()

print('All the texts have been successsfully segmented and saved to the directory.')


