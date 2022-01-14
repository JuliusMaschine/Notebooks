# EDA Bram Stoker's Dracula

## tl;dr

**![For the nbviewer](https://nbviewer.org/github/JuliusMaschine/Notebooks/blob/master/NLP/EDA_Dracula.ipynb)**

Using several NLP techniques on the text Dracula by Bram Stoker to investigate it's properties that wouldn't have been otherwise obvious to the reader. It includes the following

## Introduction

One of the best classic books in horror is Bram Stoker's Dracula, where one of the protagonists visits a castle owned by the famed unseen host named Count Dracula. This project will perform basic analysis of the book using NLP techniques on the characters. The source of data will come from Project Gutenberg with the link below.

## Brief Overview

* Character Occurence 
    * Using spaCy's person entity detecting capabilities we can count the character occurence in text

    * Using Person Entity
        * ![Character Occurence Graphs Using Person Entity](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/character_occurence_prsn_ent.png)

    * Using Proper Noun Method From spaCy
        * ![Character Occurence Graphs Using Proper Noun](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/character_occurence_prpr_noun.png)

    * Direct Comparison of Graphs
        * ![Character Occurence Graphs Using Person Entity](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/character_occurence_comb_graph.png)

* Character Information
    * we count the adjectives following around or after a noun, person entity to determine the most common adjective associated with that person/entity

        * Dracula 
            * 'fearful' 'great' 'very' 'bind'
        * Jonathan 
            * 'live', 'unnatural', 'horrible', 'awful', 'other', 'same', 'usual', 'ill', 'previous', 'excellent', 'old', 'rich', 'good', 'poor', 'dear', 'whole', 'fearful', 'long', 'human', 'mortal', 'own', 'well', 'interesting', 'wonderful', 'pierce', 'die', 'quick', 'poor', 'alone', 'round'
        * Lucy 
            * 'dear', 'poor', 'sad', 'dead', 'unequalled', 'false', 'true', 'sweet', 'late'
        * Van Helsing
            * 'sweet', 'gentle', 'remorseless', 'dear', 'instant', 'kind', 'great', 'little', 'black', 'usual', 'different', 'good', 'old', 'pierce', 'die', 'agonised', 'same', 'careful', 'old'
        * Mina 
            * 'dear', 'wonderful', 'sweet', 'poor', 'die', 'young', 'awake', 'wonderful', 'pierce', 'die', 'quick', 'poor', 'alone', 'round', 'flicker', 'own', 'drive', 'white', 'holy', 'dear'
        * Morris
            * 'instinctive', 'certain', 'other'], 'Seward': ['proper', 'remorseless', 'lunatic', 'strong', 'good', 'poor', 'dear', 'ard', 'distant', 'dear', 'proper', 'remorseless', 'lunatic', 'strong', 'good', 'poor', 'dear', 'ard', 'distant'
        * Renfield 
            * 'bloody', 'stubble', 'close', 'poor'
        * Arthur
            * 'pine', 'roaring', 'great', 'merciful', 'real', 'taketh', 'human', 'dear', 'good'

* Word Count Per Word Type
    * How often words are used showing us the uniqueness of the author

    * Top 5 Words
        * Proper Noun
            * Van Helsing: 317
            * Lucy: 298 
            * Mina: 229 
            * Jonathan: 200 
            * Count: 191
        * Adjectives 
            * good: 266 
            * great: 195 
            * poor: 190 
            * old: 187 
            * dear: 168
        * Preposition
            * away: 185 
            * far: 112 
            * long: 72 
            * soon: 69 
            * later 69
        * Pronoun
            * I: 6304 
            * yer: 9 
            * everybody: 4
            * anybody: 3 
            * em: 2
        * Adverbs
            * away: 185
            * far: 112
            * long: 72
            * soon: 69
            * later: 69
        * Noun
            * time: 442
            * man: 402
            * night: 329
            * hand: 311
            * day 274
        * Verb
            * come: 781 
            * know: 591 
            * look: 410 
            * tell: 377 
            * think: 354

* Common Collocations
    * Certain phrases that the author used through out the book that normally go together gives us an insight to the type of how they talked during that time.

* Summarisation Techniques
    * Using various techniques in summarisation techniques, shows how the summary of the text might've looked like.

    * The summarisation have used primarily two methods: 
        * The first method weighs the sentences based on the frequency of each word. The sentences are weighted by their frequency of occurrence in the text. The sentences are then sorted in descending order of their weight.
        * Second method takes a sentence and compares it to the other sentences in the text. The sentences are then ranked by the number of words in the sentence that are also in the other sentences. The sentences with the highest rank are then selected as part of the summary.


