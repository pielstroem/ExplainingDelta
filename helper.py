#!/usr/bin/env python
# -*- coding: utf-8 -*-

# At the moment, this script contains an unsystematic collection of
# classes and functions

import csv

import numpy as np

def read_csv(filename):
    """Read the given CSV file. The first row of the file should contain
    the document names, the first column the terms.

    """
    with open(filename) as infile:
        csvreader = csv.reader(infile)
        matrix = np.array(list(csvreader))
        documents = matrix[0][1:]
        terms = matrix[:,0][1:]
        # delete first row (contains documents)
        matrix = np.delete(matrix, 0, 0)
        # delete first column (contains words)
        matrix = np.delete(matrix, 0, 1)
        # Scikit-learn expects rows to be samples and columns to be
        # features, therefore we transpose the matrix (and we make
        # sure we have floats)
        matrix = np.array(matrix.T, dtype=float)
        return terms, documents, matrix


def extract_authors_from_document_names(documents):
    """We assume document names are in the format
    'Surname,-First-Names_Title of work' and extract the author name.

    """
    return np.array([d.split("_")[0] for d in documents])


def transform_to_relative_frequency(matrix, terms, min_df=1):
    """Change absolute term frequencies to relative
    frequencies. Optionally remove all terms with a document frequency
    smaller than min_df.

    """
    # all frequencies greater than 0 are set to 1:
    ones_and_zeros = np.array(matrix > 0, dtype=int)
    # find all columns with sum greater than min_df:
    filter_vector = ones_and_zeros.sum(axis=0) > min_df
    # use only those columns:
    matrix_small = matrix[:,filter_vector]
    terms_small = terms[filter_vector]
    # calculate relative frequencies
    matrix_small = matrix_small / matrix_small.sum(axis=1, keepdims=True)
    return matrix_small, terms_small


def select_most_frequent(matrix, terms, k):
    """Select the k most frequent features."""
    sums = matrix.sum(axis=0)
    top_sums = np.argsort(sums)[-k:]
    return matrix[:,top_sums], terms[top_sums]
