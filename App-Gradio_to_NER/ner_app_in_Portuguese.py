'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
import spacy
import gradio as gr

# LOC, MISC, ORG e PER
nlp = spacy.load("pt_core_news_lg")

def ner(sentence):
    doc = nlp(sentence)
    ents = [(e.text, e.label_) for e in doc.ents]
    return ents


iface = gr.Interface(fn=ner, inputs="text", outputs="text")
iface.launch(debug='True')
