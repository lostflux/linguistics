#!/usr/bin/env python3

#=======================================================================
# Dartmouth College, LING48/CS72, Winter 2024
# Kenneth Lai (kenneth.han.lai@dartmouth.edu)
# Examples for Homework 2.2: N-gram probabilities and n-gram text generation
#
# You must study the links below and attempt to modify
# the program according to the homework instructions.
#
# Documentation of the NLTK.LM package
# https://www.nltk.org/api/nltk.lm.html
#
# How to extract n-gram probabilities 
# https://stackoverflow.com/questions/54962539/how-to-get-the-probability-of-bigrams-in-a-text-of-sentences
#
# Calculating perplexity with NLTK
# https://stackoverflow.com/questions/54941966/how-can-i-calculate-perplexity-using-nltk
#=======================================================================

"""
CS-72: Accelerated Computational Linguistics
Student: Amittai Siavava
Assignment 2: N-gram probabilities and n-gram text generation

This script calculates the perplexity of a given sentence using a bigram model trained on a corpus of Swahili text.
"""
import os
import requests
import io 
import random
from nltk.lm.preprocessing import pad_both_ends, padded_everygram_pipeline
from nltk.lm import MLE, NgramCounter, Vocabulary
from nltk.util import ngrams
from collections import Counter
from nltk import word_tokenize, sent_tokenize, bigrams, trigrams

# Open file
file = io.open('corpora-hw2/swahili - sw-daima.txt', encoding='utf8')
text = file.read()
			  
# Preprocess the tokenized text for language modeling
# https://stackoverflow.com/questions/54959340/nltk-language-modeling-confusion
n = 2
paddedLine = [list(pad_both_ends(word_tokenize(text.lower()), n))]
train, vocab = padded_everygram_pipeline(n, paddedLine)

# Train an n-gram maximum likelihood estimation model
model = MLE(n) 
model.fit(train, vocab)

print("")

# NLTK will calculate the perplexity of these sentences
test_sentences = [
    "aidha alisema kuwa iwapo serikali"           # appears in corpus
  , "waache kutusifia ili wawaone watanzania"      # appears in generated text
  , "watoto walienda chumbani kunywa sharubati"      # has words not in corpus (sharubati = juice)
  ]

# NOTE: translations
# 1. "aidha alisema kuwa iwapo serikali" = "he also said that if the government" (in corpus)
# 2. "waache kutusifia ili wawaone watanzania" = "stop praising us so that they can see us tanzanians"
# 3. "watoto walienda chumbani kunywa sharubati" = "the children went into the house to drink juice"

tokenized_text = [list(map(str.lower, word_tokenize(sent))) for sent in test_sentences]

# Probability of bigrams
test_data = [bigrams(t,  pad_right=False, pad_left=False) for t in tokenized_text]
for test in test_data:
  print ("MLE Estimates:", [((ngram[-1], ngram[:-1]),model.score(ngram[-1], ngram[:-1])) for ngram in test])

print("")
	
# Perplexity of bigrams
test_data = [bigrams(t,  pad_right=False, pad_left=False) for t in tokenized_text]
for i, test in enumerate(test_data):
  print("PP({0}):{1}".format(test_sentences[i], model.perplexity(test)))
  
print("")
