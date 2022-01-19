# EDA Bram Stoker's Dracula

## tl;dr

**[For the nbviewer](https://nbviewer.org/github/JuliusMaschine/Notebooks/blob/master/NLP/EDA_Dracula.ipynb)**

Using several NLP techniques on the text Dracula by Bram Stoker to investigate it's properties that wouldn't have been otherwise obvious to the reader. It includes the following

## Introduction

One of the best classic books in horror is Bram Stoker's Dracula, where one of the protagonists visits a castle owned by the famed unseen host named Count Dracula. This project will perform basic analysis of the book using NLP techniques on the characters. The source of data will come from Project Gutenberg with the link below.

[Gutenberg Book](https://www.gutenberg.org/ebooks/345)

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
            * ![Proper Noun](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/wordcount_prop.png)

        * Adjectives 
            * ![Adjectives](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/wordcount_adj.png)

        * Preposition
            * ![Preposition](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/wordcountadp.png)

        * Pronoun
            * ![Pronoun](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/wordcount_pron_wo_I.png)

        * Adverbs
            * ![Adverb](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/wordcount_adv.png)

        * Noun
            * ![Noun](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/wordcount_noun.png)

        * Verb
            * ![Verb](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/wordcount_verb.png)


* Common Collocations
    * Certain phrases that the author used through out the book that normally go together gives us an insight to the type of how they talked during that time.

    ![Common Collocations](https://github.com/JuliusMaschine/Notebooks/blob/master/NLP/wordcloud_drac.png)


* Summarisation Techniques
    * Using various techniques in summarisation techniques, shows how the summary of the text might've looked like.

    * The summarisation have used primarily two methods: 
        * The first method weighs the sentences based on the frequency of each word. The sentences are weighted by their frequency of occurrence in the text. The sentences are then sorted in descending order of their weight.
        * Second method takes a sentence and compares it to the other sentences in the text. The sentences are then ranked by the number of words in the sentence that are also in the other sentences. The sentences with the highest rank are then selected as part of the summary.


