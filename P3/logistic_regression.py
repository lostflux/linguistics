#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#=======================================================================
# LING48/CS72 Homework 3.1: Logistic Regression
# Kenneth Lai (kenneth.han.lai@dartmouth.edu)
# Last modification: 2024/01/24
#=======================================================================

"""
CS-72: Accelerated Computational Linguistics
Student: Amittai Siavava
Assignment 3: Logistic Regression
Date: 2024/01/24

This program runs a logistic regression classifier on a dataset of movie reviews.

To use, pick the relevant datasets below and run the program on the terminal
with the following command:

```bash
    python3 logistic_regression.py
```    

"""

import os
import numpy as np
from collections import defaultdict, Counter
from math import ceil
from random import Random
from scipy.special import expit # logistic (sigmoid) function
from typing import *
import pandas as pd

class LogisticRegression():

    def __init__(self, verbose: bool = True):
        #? map class names (e.g. pos, neg) to class indices (e.g. 0, 1)
        self.class_dict = {}
        
        #? maps class indices to class names
        self.reverse_class_dict = {}
        
        #? maps feature names (words) to feature indices (0, 1, 2, ..., V-1)
        self.feature_dict = {}
        
        #? parameter vector (weights and bias)
        self.theta = None # weights (and bias)
        
        #? whether to print stats during training and evaluation
        self.verbose = verbose

    def make_dicts(self, train_set):
        """
        Given a training set, fills in self.class_dict, self.reverse_class_dict, and
        self.feature_dict. Also initializes the parameter vector self.theta.
        """
        classes = set()
        vocabulary = set()
        # iterate over training documents
        for root, dirs, files in os.walk(train_set):
            # class names are in dirs
            classes.update(dirs)
            for name in files:
                with open(os.path.join(root, name)) as f:
                    words = f.read().split()
                    vocabulary.update(words)
                    
        #? populate class_dict, reverse_class_dict, and feature_dict
        for i, c in enumerate(classes):
            self.class_dict[c] = i
            self.reverse_class_dict[i] = c
            
        for word_index, word in enumerate(vocabulary):
            self.feature_dict[word] = word_index
            
        self.theta = np.zeros(len(self.feature_dict) + 1)

    def load_data(self, data_set):
        """
        Loads a dataset. Specifically, returns a list of filenames, and dictionaries
        of classes and documents such that:
        classes[filename] = class of the document
        documents[filename] = feature vector for the document (use self.featurize)
        """
        filenames = []
        classes = dict()
        documents = dict()
        # iterate over documents
        for root, dirs, files in os.walk(data_set):
            for name in files:
                with open(os.path.join(root, name)) as f:
                    #? get class name c from root
                    _, c = os.path.split(root)
                    words = f.read().split()
                    filenames.append(name)
                    classes[name] = c
                    documents[name] = self.featurize(words)
        return filenames, classes, documents

    def featurize(self, document):
        """
        Given a document (as a list of words), returns a feature vector.
        Note that the last element of the vector, corresponding to the bias, is a
        "dummy feature" with value 1.
        """
        
        vector = np.zeros_like(self.theta)

        #? increment counts at indices corresponding to each word
        counts = Counter(document)
        for word, count in counts.items():
            # NOTE: if wor is not in feature dict,
            #  did something wrong happen in make_dicts?
            #  probably... BUT a word in the test set might not be in the training set
            #  so I opted to ignore such here.
            if word in self.feature_dict:
                vector[self.feature_dict[word]] = count
                
                #! is there any (dis)advantage to normalizing the counts?
        
        
        vector[-1] = 1
        return vector

    def train(self, train_set, batch_size=3, n_epochs=1, eta=0.1):
        """
        Trains a logistic regression classifier on a training set.
        """
        
        if self.theta is None:
            self.make_dicts(train_set)
        filenames, classes, documents = self.load_data(train_set)
        filenames = sorted(filenames)
        n_minibatches = ceil(len(filenames) / batch_size)
        
        for epoch in range(n_epochs):
            # if self.verbose:
            #     print(f"Epoch {epoch+1} of {n_epochs}")
            loss = 0
            for i in range(n_minibatches):
                # list of filenames in minibatch
                minibatch = filenames[i * batch_size: (i + 1) * batch_size]
                
                # TODO 1: create and fill in matrix X and vector y
                X = np.array([documents[name] for name in minibatch])
                y = np.array([self.class_dict[classes[name]] for name in minibatch])

                # TODO 2: compute y_hat
                y_hat = expit(self.theta @ X.T)
                
                # TODO 3: update cross-entropy loss
                loss += -np.sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
                
                # TODO 4: compute gradient
                grad = np.dot(X.T, y_hat - y) / batch_size

                # TODO 5: update weights (and bias)
                self.theta -= eta * grad
                
            loss /= len(filenames)
            if self.verbose:
                print(f"Epoch {epoch:4d} of {n_epochs:4d}: {loss}")
            
            # randomize order
            Random(epoch).shuffle(filenames)
            
    def reset(self):
        """
        Resets the parameter vector to all zeros.
        """
        self.theta = np.zeros_like(self.theta)

    def test(self, dev_set):
        """
        Tests the classifier on a development or test set.
        Returns a dictionary of filenames mapped to their correct and predicted
        classes such that:
        results[filename]["correct"] = correct class
        results[filename]["predicted"] = predicted class
        """
        results = defaultdict(dict)
        filenames, classes, documents = self.load_data(dev_set)
        for name in filenames:
            # ? compute y_hat
            y_hat = expit(self.theta @ documents[name])
            
            #? get most likely class (recall that P(y=1|x) = y_hat)
            results[name]["predicted"] = self.reverse_class_dict[1 if y_hat > 0.5 else 0]
            results[name]["correct"] = classes[name]
            
        return results

    def evaluate(self, results: Dict[str, Dict[str, str]]) -> None:
        """
        Given results, calculates the following:
        Precision, Recall, F1 for each class
        Accuracy overall
        Also, prints evaluation metrics in readable format.
        """
        # you may find this helpful
        CM = defaultdict(Counter)
        for result in results.values():
            actual = result['correct']
            predicted = result['predicted']
            CM[actual][predicted] += 1
            
        res = defaultdict(lambda: defaultdict(None))
        
        for class_name in CM:
            TP = CM[class_name][class_name]
            FP = 0
            for other_class in CM:
                if other_class != class_name:
                    FP += CM[other_class][class_name]
                    
            FN = 0
            for other_class in CM:
                if other_class != class_name:
                    FN += CM[class_name][other_class]
                    
            TN = 0
            for other_class in CM:
                for other_class2 in CM:
                    if class_name not in (other_class, other_class2):
                        TN += CM[other_class][other_class2]
                        
                    
            precision = recall = f1 = accuracy = specificity = 0
            if TP + FP > 0:
                precision = TP / (TP + FP)
                
            if TP + FN > 0:
                recall = TP / (TP + FN)
                
            if precision + recall > 0:
                f1 = 2 * precision * recall / (precision + recall)
                
            if TP + FP + TN + FN > 0:
                accuracy = (TP + TN) / (TP + FP + TN + FN)
                
            if TN + FP > 0:
                specificity = TN / (TN + FP)
            
            res[class_name] = {
                "metrics": pd.DataFrame(
                    [[precision, recall, f1, accuracy, specificity]],
                    index=["MEASURE"],
                    columns=["PRECISION", "RECALL", "F1", "ACCURACY", "SPECIFICITY"]
                ),
                "CM": pd.DataFrame(
                    [[TP, FP], [FN, TN]],
                    index=["ACTUAL POSITIVE", "ACTUAL NEGATIVE"],
                    columns=["PREDICTED POSITIVE", "PREDICTED NEGATIVE"]
                )
            }
            
        if self.verbose:
            self.print_results(res)
        return res
            
    def print_results(self, res: Dict[str, Dict[str, pd.DataFrame]]) -> None:
        for class_name in res:
            print(f"\n\n\n\n") # some space for distinction
            print(f"-------------------------------------------------------------")
            print(f"CLASS: {class_name}")
            print(f"-------------------------------------------------------------")
            print(f"\n-------------------------------------------------------------")
            print(f"METRICS")
            print(f"-------")
            print(f"{res[class_name]['metrics']}")
            print(f"-------------------------------------------------------------")
            print(f"\n-------------------------------------------------------------")
            print(f"CONFUSION MATRIX")
            print(f"----------------")
            print(f"{res[class_name]['CM']}")
            print(f"-------------------------------------------------------------")

if __name__ == "__main__":
    lr = LogisticRegression()
    # make sure these point to the right directories
    lr.make_dicts("movie_reviews/train")
    # lr.make_dicts("movie_reviews_small/train")
    lr.train("movie_reviews/train", batch_size=3, n_epochs=100, eta=0.001)
    # lr.train("movie_reviews_small/train", batch_size=3, n_epochs=1, eta=0.1)
    results = lr.test("movie_reviews/dev")
    # results = lr.test("movie_reviews_small/test")
    lr.evaluate(results)
