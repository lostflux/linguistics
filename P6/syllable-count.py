#=========================================================================
# Dartmouth College, CS 72/LING 48, Winter 2024
# Kenneth Lai (Kenneth.Han.Lai@dartmouth.edu)
# Examples for Homework 6.2: Counting syllables of a word in English
#
# This short example uses a package called PyPhen. It uses hunspell
# dictionaries to split the syllables of a word. If you want to use
# it, you'll need to install this package:
#
# From Anaconda:    conda install -c conda-forge pyphen
# From Colab:       !pip install pyphen
#=========================================================================

import pyphen

dic = pyphen.Pyphen(lang='en')

wordToSplit = "sunrise"

sylls = dic.inserted(wordToSplit)
nsylls = sylls.count("-") + 1

print(wordToSplit)
print(sylls)
print(nsylls)
