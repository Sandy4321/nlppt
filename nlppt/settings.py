#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Path to NLPNet Data
NLPNET_DATA = os.path.join(os.path.dirname(__file__), 'data','nlpnet')

# NLTK Stopwords
STOPWORDS = [u'de', u'a', u'o', u'que', u'e', u'do', u'da', u'em', u'um', u'para', u'com', u'n\xe3o', u'uma', u'os', u'no', u'se', u'na', u'por', u'mais', u'as', u'dos', u'como', u'mas', u'ao', u'ele', u'das', u'\xe0', u'seu', u'sua', u'ou', u'quando', u'muito', u'nos', u'j\xe1', u'eu', u'tamb\xe9m', u's\xf3', u'pelo', u'pela', u'at\xe9', u'isso', u'ela', u'entre', u'depois', u'sem', u'mesmo', u'aos', u'seus', u'quem', u'nas', u'me', u'esse', u'eles', u'voc\xea', u'essa', u'num', u'nem', u'suas', u'meu', u'\xe0s', u'minha', u'numa', u'pelos', u'elas', u'qual', u'n\xf3s', u'lhe', u'deles', u'essas', u'esses', u'pelas', u'este', u'dele', u'tu', u'te', u'voc\xeas', u'vos', u'lhes', u'meus', u'minhas', u'teu', u'tua', u'teus', u'tuas', u'nosso', u'nossa', u'nossos', u'nossas', u'dela', u'delas', u'esta', u'estes', u'estas', u'aquele', u'aquela', u'aqueles', u'aquelas', u'isto', u'aquilo', u'estou', u'est\xe1', u'estamos', u'est\xe3o', u'estive', u'esteve', u'estivemos', u'estiveram', u'estava', u'est\xe1vamos', u'estavam', u'estivera', u'estiv\xe9ramos', u'esteja', u'estejamos', u'estejam', u'estivesse', u'estiv\xe9ssemos', u'estivessem', u'estiver', u'estivermos', u'estiverem', u'hei', u'h\xe1', u'havemos', u'h\xe3o', u'houve', u'houvemos', u'houveram', u'houvera', u'houv\xe9ramos', u'haja', u'hajamos', u'hajam', u'houvesse', u'houv\xe9ssemos', u'houvessem', u'houver', u'houvermos', u'houverem', u'houverei', u'houver\xe1', u'houveremos', u'houver\xe3o', u'houveria', u'houver\xedamos', u'houveriam', u'sou', u'somos', u's\xe3o', u'era', u'\xe9ramos', u'eram', u'fui', u'foi', u'fomos', u'foram', u'fora', u'f\xf4ramos', u'seja', u'sejamos', u'sejam', u'fosse', u'f\xf4ssemos', u'fossem', u'for', u'formos', u'forem', u'serei', u'ser\xe1', u'seremos', u'ser\xe3o', u'seria', u'ser\xedamos', u'seriam', u'tenho', u'tem', u'temos', u't\xe9m', u'tinha', u't\xednhamos', u'tinham', u'tive', u'teve', u'tivemos', u'tiveram', u'tivera', u'tiv\xe9ramos', u'tenha', u'tenhamos', u'tenham', u'tivesse', u'tiv\xe9ssemos', u'tivessem', u'tiver', u'tivermos', u'tiverem', u'terei', u'ter\xe1', u'teremos', u'ter\xe3o', u'teria', u'ter\xedamos', u'teriam']

# Some more stopwords
STOPWORDS.extend([u'\xc3\xa9'])
