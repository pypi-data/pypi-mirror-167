# random-word-generator
A small Python librairy to generate random credible words based on a  list of words by esimating the probability of the next character from the frequency of the previous ones

```
from markov_word_generator import MarkovWordGenerator

generator = MarkovWordGenerator(markov_length=3, dictionary_filename='dictionaries/EN-words.dic', ignore_accents=True)

for i in range(0, 10):
    print(generator.generate_word())
```

```
blungalinther
super
solder
degreetricked
mittlessly
out
hearf
fracertory
gyny
locious
```

```
from markov_word_generator import MarkovWordGenerator

generator = MarkovWordGenerator(markov_length=4, dictionary_filename='dictionaries/EN-words.dic', ignore_accents=True)

for i in range(0, 10):
    print(generator.generate_word())
```

```
authering
negligented
manoeistical
bleat
lover
confusions
dest
hand
display
entwinkle
```
