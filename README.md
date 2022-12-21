# vichShir package
This repository contains common functions that I used in data science projects with Python.



## Key Features
- Utils
  - Download files
- Machine Learning - Preprocessing
  - Normalize the inputs
  - Impute missing data
- Text patterns
  - Name extractor
  - Email
  - Phone
  - Year
- Webscraping
  - Extract the content (text) from websites



## How to use
To clone and install this package, you'll need PIP installed on your computer. From your command line:
```shell
# Update pip
pip install --upgrade pip

# Install the latest master of vichShir
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



## Credits
This software uses the following open source packages:
- Pandas
- Numpy
- Scikit-learn
- Transformers
- Beautifulsoup



## License
Apache 2.0
