#!/usr/bin/env python

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
#=======================================================================

"""
CS-72: Accelerated Computational Linguistics
Student: Amittai Siavava
Assignment 2: N-gram probabilities and n-gram text generation

This script generates a 100-word sequence using a 1,2,3, and 4-gram model trained on a corpus of Swahili text.
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

#? (a) Use Swahili corpus
file = open('corpora-hw2/swahili - sw-daima.txt', encoding='utf8')
text = file.read()

def train_and_generate(n, tokenized_text):

    paddedLine = [list(pad_both_ends(tokenized_text, n))]
    train, vocab = padded_everygram_pipeline(n, paddedLine)

    # Train an n-gram maximum likelihood estimation model
    model = MLE(n) 
    model.fit(train, vocab)
    
    word_list = model.generate(100, random_seed=999) # reproducibile
    result = ' '.join(word_list)
    print(f"\n\nGENERATED 100-WORD SEQUENCE USING {n}-GRAMS\n=========================================")
    print(f"{result}")
    print("=========================================\n\n")

    return model
  
# Preprocess the tokenized text for language modeling
# https://stackoverflow.com/questions/54959340/nltk-language-modeling-confusion
tokenized_text = word_tokenize(text.lower())

#? (b) generate a 100 word sequence

##? using unigram model
train_and_generate(1, tokenized_text)

##? using bigram model
train_and_generate(2, tokenized_text)

##? using trigram model
train_and_generate(3, tokenized_text)

##? using four-gram model
# NOTE: save model for reuse below

model = train_and_generate(4, tokenized_text)

#? (c) Get probability and counts of a unigram, bigram, and trigram

##? unigram = "alisema" --> "he/she said"
uni_counts = model.counts['alisema']
uni_prob = model.score('alisema')

# get total word count from the model


print("UNIGRAM COUNTS AND PROBABILITIES\n=========================================")
print(f"counts('alisema'): \t\t {uni_counts}")
print(f"P('alisema'): \t\t\t {uni_prob}")
print("=========================================\n\n")

##? bigram = "alisema serikali" --> "he/she said the government"
bi_counts = model.counts[["alisema"]]["serikali"]
bi_prob = model.score("serikali", ["alisema"])

print("BIGRAM COUNTS AND PROBABILITIES\n=========================================")
print(f"counts('serikali' | 'alisema'): \t {bi_counts}")
print(f"P('serikali' | 'alisema'): \t\t {bi_prob}")
print(f"verification: \t\t\t\t {bi_counts/uni_counts}")
print("=========================================\n\n")


##? trigram = "alisema serikali imetenga" --> "he/she said the government has set aside"
tri_counts = model.counts["alisema serikali".split()]["imetenga"]
tri_prob = model.score("imetenga", "alisema serikali".split())

print("TRIGRAM COUNTS AND PROBABILITIES\n=========================================")
print(f"counts('imetenga' | 'alisema serikali'): \t {tri_counts}")
print(f"P('imetenga' | 'alisema serikali'): \t\t {tri_prob}")
print(f"verification: \t\t\t\t\t {tri_counts/bi_counts}")
print("=========================================\n\n")

