
coref_text = "Thai food was great and not expensive. we loved it. We visited many beach resorts in Thailand, they are so beautiful.We recommened them."

from py3 import coref, lemma_en

def leco(coref_text):
    text = coref(coref_text)
    return lemma_en(text)

