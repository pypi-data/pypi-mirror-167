#import coreferee, spacy
#nlp = spacy.load('en_core_web_lg')
#nlp.add_pipe('coreferee')

#python3 -m pip install coreferee
#python3 -m coreferee install en
#python -m spacy download en_core_web_lg

import spacy 


from spacy import displacy
nlp = spacy.load('en_core_web_lg')
nlp.add_pipe('coreferee')

#coref_text = "Thai food was great and not expensive. we loved it. We visited many beach resorts in Thailand, they are so beautiful.We recommened them."
#core_text = "Although he was very busy with his work, Peter had had enough of it. He and his wife decided they needed a holiday. They travelled to Spain because they loved the country very much."
def coref(core_text):
  doc = nlp(core_text)
  #doc._.coref_chains.print()
  refs = doc._.coref_chains

  keyNs = []
  key_list =[]
  for ref in refs:
    keyN = ref[ref.most_specific_mention_index]
    if len(keyN)==1:
        key_l = [a[0] for a in list(ref)]
        keyNs.append(keyN[0])
        key_list.append(key_l)

  words_index = {}
  for i, token in enumerate(doc):
    for keyN, keyL in zip(keyNs, key_list):
      if i in keyL and token.tag_ =="PRP":
        #print(token.text)
        word = doc[keyN].text
        words_index.update({i:word})
  words2 = []
  for i, token in enumerate(doc):
    if i in list(words_index):
      word = words_index[i]
    else:
      word = token.text
    words2.append(word)
  coref_text = " ".join(words2)
  return coref_text


# lemmatize the words
def lemma_en(text):
    #python -m spacy download en_core_web_sm 
    # Create a Doc object
    #text = "asked I am gone you went to supermarkets to you are bought buy drinks visited and traveled by flying"
    doc = nlp(text)
    
    #lemmatized_text = " ".join([token.text for token in doc if token.text in ['him','her','them'] else token.lemma_])
    words = []
    for token in doc :
      if token.text in ['him','her','them']: # for coreference, otherwise it will be changed to he, she, they
          word = token.text
      else:
        word = token.lemma_
      words.append(word)
       
    lemmatized_text = " ".join(words)

    #print(lemmatized_text)
    return lemmatized_text
textt = "went went he asked reviews tasted worth wente already times since totally falling love you are bought buy drinks visited and traveled by went"
textt = "really? it satisfied me, surprised It isn't many traveled to Thailand once a year at least, I liked the hotel"
lemma_en(textt)