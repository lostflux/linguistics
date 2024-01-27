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
def print_results(priors: DefaultDict[str, float], likelihoods: DefaultDict[str, DefaultDict[str, float]]) -> None:
    """
    Prints the priors and likelihoods in a readable format.
    """
    print("PRIORS")
    for c, p in priors.items():
        print(f"{c}: {p:.10f}")
    print("\n\nLIKELIHOODS")
    for f, d in likelihoods.items():
        for c, p in d.items():
            print(f"{f} | {c}: {p:.10f}")

class NaiveBayes():

    def __init__(self):
        self.prior = defaultdict(float)
        self.likelihood = defaultdict(lambda: defaultdict(float))
        self.total_words = None


    def train(self, train_set):
        """
        Trains a Naive Bayes classifier on a training set.
        Specifically, fills in self.prior and self.likelihood such that:
        self.prior[class] = log(P(class))
        self.likelihood[feature][class] = log(P(feature|class))
        """
        doc_count = defaultdict(int)
        word_count = defaultdict(lambda : defaultdict(int))
        total_words = defaultdict(int)

        # iterate over training documents
        for root, dirs, files in os.walk(train_set):
            for name in files:
                class_label = root.split('/')[-1]
                # print("current class label is: {}".format(class_label))
                doc_count[class_label] += 1
                with open(os.path.join(root, name)) as f:
                    contents = f.read().split()
                    for word in contents:
                        word_count[class_label][word] += 1
                        total_words[class_label] += 1

        # normalize counts to probabilities, and take logs
        # let's now do log probabilities
        total = sum(doc_count.values())
        self.prior = {
            class_label: log(doc_count[class_label]/total)
            for class_label in doc_count
        }
        
        for class_label in doc_count:
            total_word_count = total_words[class_label] + len(word_count[class_label])
            for word in word_count[class_label]:
                self.likelihood[word][class_label] = log((word_count[class_label][word]+1)/total_word_count)

        # updated global variables
        self.total_words = total_words
        self.vocabulary_size = {class_label: len(word_count[class_label]) for class_label in word_count}

        print_results(self.prior, self.likelihood)

    def test(self, dev_set):
        """
        Tests the classifier on a development or test set.
        Returns a dictionary of filenames mapped to their correct and predicted
        classes such that:
        results[filename]["correct"] = correct class
        results[filename]["predicted"] = predicted class
        """
        results = defaultdict(dict)
        # iterate over testing documents
        for root, directories, files in os.walk(dev_set):
            for name in files:
                with open(os.path.join(root, name)) as f:
                    # calculate log-probabilities for each class
                    # from log-probabilities, get most likely class
                    words = f.read().split()
                    class_score = {class_label : self.prior[class_label] for class_label in self.prior}
                    # calculate log-probabilities for each class
                    for word in words:
                        for class_label in self.prior:
                            total_word_count = self.total_words[class_label]
                            vocabulary_size = self.vocabulary_size[class_label]
                            word_log_probability = self.likelihood[word].get(class_label, log(1/(total_word_count+vocabulary_size)))
                            class_score[class_label] += word_log_probability
                    # from log-probabilities, get most likely class
                    predicted_most_likely_class = max(class_score.items(), key=itemgetter(1))[0]
                    correct_class = root.split('/')[-1]
                    # print("predicted_most_likely_class: {}, correct_class: {}".format(predicted_most_likely_class, correct_class))
                    results[name] = {'correct':correct_class, 'predicted':predicted_most_likely_class}
        
        return results

    def evaluate(self, results):
        """
        Given results, calculates the following:
        Precision, Recall, F1 for each class
        Accuracy overall
        Also, prints evaluation metrics in readable format.
        """
        # you may find this helpful
        confusion_matrix = defaultdict(lambda: defaultdict(int))
        for result in results.values():
            confusion_matrix[result['correct']][result['predicted']] += 1
        for class_label in confusion_matrix:
            true_positive = confusion_matrix[class_label][class_label]
            false_positive = sum(
                confusion_matrix[other][class_label] for other in confusion_matrix if other != class_label)
            false_negative = sum(
                confusion_matrix[class_label][other] for other in confusion_matrix if other != class_label)

            precision = true_positive / (true_positive + false_positive) if true_positive + false_positive > 0 else 0
            recall = true_positive / (true_positive + false_negative) if true_positive + false_negative > 0 else 0
            f1 = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0

            print("Class: {}, Precision: {}, Recall: {}, F1 Score: {}".format(class_label, precision, recall, f1))

        total_correct = sum(confusion_matrix[class_label][class_label] for class_label in confusion_matrix)
        total_predictions = sum(sum(confusion_matrix[class_label].values()) for class_label in confusion_matrix)
        accuracy = total_correct / total_predictions if total_predictions > 0 else 0
        print("Overall Accuracy: {}".format(accuracy))

        print("Confusion Matrix: {}".format(confusion_matrix))

if __name__ == "__main__":
    nb = NaiveBayes()
    # make sure these point to the right directories
    #nb.train("movie_reviews/train")
    nb.train("movie_reviews_small/train")
    #results = nb.test("movie_reviews/dev")
    results = nb.test("movie_reviews_small/test")
    nb.evaluate(results)
