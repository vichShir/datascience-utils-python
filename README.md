# vichShir package
Utils package with commonly functions used for data science projects with Python



## How to use

```shell
pip install --upgrade pip
pip install git+https://github.com/vichShir/datascience-utils-python.git
```



## Examples

### NER - Name Extractor

```python
from vichshir.cleaning.text_matching.nlp import NameExtractor

txt_person = '''
Existem muitos sistemas de ERP. Thiago Fulano da Silva é CTO e desenvolvedor de um poderoso sistema de ERP, também coordena uma equipe, João Sicrano da Costa e Pedro Beltrano.
'''

extractor = NameExtractor()
persons = extractor.extract_names(txt_person)
persons
```
