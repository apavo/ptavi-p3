#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import SmallSMILHandler
import sys
from xml.sax import make_parser

def imprimir(sHandler):
    for etiqueta in sHandler.lista:
        print etiqueta[0], 
        atributos=etiqueta[1]
        for atributo in atributos:
            print "\t", atributo, "=", atributos[atributo], 
        print
try:
    parser = make_parser()
    sHandler = SmallSMILHandler.SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open(sys.argv[1]))
    imprimir(sHandler)
except IndexError:
    print "Usage: python karaoke.py file.smil"

    
