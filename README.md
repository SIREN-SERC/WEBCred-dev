# Installation
- Set up the environment using [pipenv](https://github.com/pypa/pipenv)
   - Install pipenv [Instructions](https://github.com/pypa/pipenv#installation)
   - `$:pipenv install`
   - Install postgres (google it yourself for your system)
   
- Configure postgres:
   - Create new db
        
        `$: create database __name__`
   - Create password for postgresql
        
        `$: psql postres`
        
        `$: \password`

- Populate the environment variables listed in `env.sample` into `.env` 
with correct values.
        
        Conventionally,
        port=5432

- Make and apply migrations
    
    `$:python manage.py migrations`

- Download Stanford CoreNLP Library
    
    `$: wget http://nlp.stanford.edu/software/stanford-corenlp-full-2018-02-27.zip`
    `$: unzip stanford-corenlp-full-2018-02-27.zip -d stanford-corenlp-full`
    
    Install the JDK [Instructions](http://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html)
    
- Install needed nltk data packages in Python:

    ```
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('stopwords')
    ```

- Start the CoreNLP server

    - `$: cd stanford-corenlp-full-2018-02-27 && java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000 --add-modules java.se.ee`

- Start the webserver

    - `$:cd path_to/WEBCred && python manage.py runserver`
 

Based on the original WEBCred application [here](https://github.com/Shriyanshagro/WEBCred)

![WEBCred](static/screenshot.png)