'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
import spacy
import gradio as gr


nlp = spacy.load("en_core_web_sm")

def ner(sentence):
    doc = nlp(sentence)
    ents = [(e.text, e.label_) for e in doc.ents]
    return ents


iface = gr.Interface(fn=ner, inputs="text", outputs="text")
iface.launch(debug='True')
