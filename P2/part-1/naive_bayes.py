#!/usr/bin/env python3

#=======================================================================
# LING48/CS72 Homework 2.1: Naive Bayes
# Kenneth Lai (kenneth.han.lai@dartmouth.edu)
# Last modification: 2024/01/17
#=======================================================================
"""
Dartmouth CS-72: Accelerated Computational Linguistics
Winter 2024
Student: Amittai Wekesa
"""

import os
from collections import defaultdict, Counter
from math import log
from operator import itemgetter # you may find this helpful
from typing import *
import pandas as df

class NaiveBayes():

    def __init__(self):
        self.prior = defaultdict(float)
        self.likelihood = defaultdict(lambda: defaultdict(float))
        
        #? other instance vars
        # self.word_counts = Counter()      
        self.vocab_size = Counter()
        self.vocab = set()
        self.labels = set()
        self.words = defaultdict(lambda: defaultdict(int))
        
        # self.vocab_size = 0


    def train(self, train_set: str) -> None:
        """
        Trains a Naive Bayes classifier on a training set.
        Specifically, fills in self.prior and self.likelihood such that:
        self.prior[class] = log(P(class))
        self.likelihood[feature][class] = log(P(feature|class))
        """
        document_counts = Counter()
        class_word_counts = defaultdict(Counter)

        #? accumulate counts
        for root, dirs, files in os.walk(train_set):
            for name in files:
                label = root.split('/')[-1]
                self.labels.add(label)
                document_counts[label] += 1
                with open(os.path.join(root, name)) as f:
                    for word in f.read().split():
                        self.vocab.add(word)
                        class_word_counts[label][word] += 1

        #? norm to log probabilities
        self.vocab_size = { label: sum(class_word_counts[label].values()) for label in document_counts }
        self.vocab_size["total"] = len(self.vocab)
        
        document_counts_sum = sum(document_counts.values())
        self.prior = {
            label: log(document_counts[label] / document_counts_sum)
            for label in document_counts
        }
        
        for word in self.vocab:
            for label in self.labels:
                numerator = class_word_counts[label][word] + 1
                denominator = self.vocab_size[label] + self.vocab_size["total"]
                self.likelihood[word][label] = log(numerator / denominator)
                
        
        for label in document_counts:
            self.words[label] = {
                "total": sum(class_word_counts[label].values()),
                "unique": len(class_word_counts[label])
            }


    def test(self, dev_set: str) -> Dict[str, Dict[str, str]]:
        """
        Tests the classifier on a development or test set.
        Returns a dictionary of filenames mapped to their correct and predicted
        classes such that:
        results[filename]["correct"] = correct class
        results[filename]["predicted"] = predicted class
        """
        
        results = {}
        for root, directories, files in os.walk(dev_set):
            
            for filename in files:
                actual = root.split('/')[-1]
                # print(f"{actual = }")
                with open(os.path.join(root, filename)) as f:
                    
                    sequence = f.read().split()
                    sums = self.prior.copy()
                    
                    for word in sequence:
                        for label in sums:
                            if word in self.vocab:
                                sums[label] += self.likelihood[word][label]
                            else:
                                sums[label] += log(1 / (self.words[label]["total"] + self.vocab_size["total"]))

                    results[filename] = {
                        "correct": actual,
                        "predicted": max(sums.items(), key=itemgetter(1))[0]
                    }
                    
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
            
        res = {}
        
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
                "metrics": df.DataFrame(
                    [[precision, recall, f1, accuracy, specificity]],
                    index=["MEASURE"],
                    columns=["PRECISION", "RECALL", "F1", "ACCURACY", "SPECIFICITY"]
                ),
                "CM": df.DataFrame(
                    [[TP, FP], [FN, TN]],
                    index=["ACTUAL POSITIVE", "ACTUAL NEGATIVE"],
                    columns=["PREDICTED POSITIVE", "PREDICTED NEGATIVE"]
                )
            }
            
        self.print_results(res)
            
    def print_results(self, res: Dict[str, Dict[str, df.DataFrame]]) -> None:
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
    nb = NaiveBayes()
    # make sure these point to the right directories
    
    #! -------------------------------------
    
    #? small dataset
    # nb.train("movie_reviews_small/train")
    # results = nb.test("movie_reviews_small/test")
    
    #? main dataset
    nb.train("movie_reviews/train")
    results = nb.test("movie_reviews/dev")
    
    #! -------------------------------------
    
    nb.evaluate(results)
