#  Utilize spacy for name extraction
#  strModified = "2025.12.06"

#
#  ---------- Python Setup ----------
#
#  pip3 install -U pip setuptools wheel
#  pip3 install spacy

#  Download the libraries needed
#  python3 -m spacy download en_core_web_sm
#  python3 -m spacy download en_core_web_lg

#
#  ---------- Names ----------
#
import spacy

strText = "Hello Daniel Morvay!  How are thing today?  My name is Redbeard, your faithful AI.  How may I help today?  Today is 2025.12.05, and tomorrow is December 06, 2025.  Next week will have Monday and Thursday."

objNLP = spacy.load("en_core_web_lg")
objBreakdown = objNLP(strText).to_json()

#  Extract people
objPeople =  [ee for ee in objBreakdown['ents'] if ee['label'] == 'PERSON']

#  Print names
for pps in objPeople:
    print(strText[pps['start']:pps['end']])

#
#  ---------- Dates ----------
#
import spacy

strText = "Hello Daniel Morvay!  How are thing today?  My name is Redbeard, your faithful AI.  How may I help today?  Today is 2025.12.05, and tomorrow is December 06, 2025.  Next week will have Monday and Thursday."

objNLP = spacy.load("en_core_web_lg")
objBreakdown = objNLP(strText).to_json()

#  Extract Dates
objDates =  [ee for ee in objBreakdown['ents'] if ee['label'] == 'DATE']

#  Print dates
for pps in objDates:
    print(strText[pps['start']:pps['end']])


#
#  ---------- More General Extraction ----------
#
import spacy

strText = "Hello Daniel Morvay!  How are thing today?  My name is Redbeard, your faithful AI.  How may I help today?  Today is 2025.12.05, and tomorrow is December 06, 2025.  Next week will have Monday and Thursday."

objNLP = spacy.load("en_core_web_lg")
objBreakdown = objNLP(strText).to_json()

#  Extract All
objAll =  [ee for ee in objBreakdown['ents']]

#  Print All
for pps in objAll:
    print(strText[pps['start']:pps['end']])
