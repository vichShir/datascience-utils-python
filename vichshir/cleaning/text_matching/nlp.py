from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification


NAME_EXTRACTOR_MODEL = "xlm-roberta-large-finetuned-conll03-english"


class NameExtractor():

  def __init__(self):
    self.tokenizer = AutoTokenizer.from_pretrained(NAME_EXTRACTOR_MODEL)
    self.model = AutoModelForTokenClassification.from_pretrained(NAME_EXTRACTOR_MODEL)
    self.classifier = pipeline("ner", model=self.model, tokenizer=self.tokenizer, aggregation_strategy='simple')


  def predict(self, corpus):
    return self.classifier(corpus)


  def extract_names(self, corpus):
    prediction = self.predict(corpus)
    persons = [x for x in prediction if x['entity_group'] == 'PER']
    persons = [x['word'] for x in persons]
    return persons