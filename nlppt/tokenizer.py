#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nlpnet
import itertools

from settings import NLPNET_DATA
from settings import STOPWORDS

def tokenizer(text):
    sentences = nlpnet.tokenize(text,language='pt')

    # flat a list of lists
    tokens = list(itertools.chain.from_iterable(sentences))

    return tokens

def filter_stopwords(tokens):

    return [w for w in tokens if w not in STOPWORDS]
