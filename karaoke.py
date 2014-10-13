#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import smallsmilhandler
import sys
from xml.sax import make_parser
import os


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self, fich):
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fich))
        self.lista = sHandler.get_tags()

    def __str__(self):
        for etiqueta in self.lista:
            print etiqueta[0],
            atributos = etiqueta[1]
            for atributo in atributos:
                print "\t", atributo, "=", atributos[atributo],
            print

    def do_local(self):
        for etiqueta in self.lista:
            atributos = etiqueta[1]
            for atributo in atributos:
                if atributo == "src":
                    os.system("wget -q " + atributos[atributo])
                    nombre = atributos[atributo].split("/")
                    atributos[atributo] = nombre[-1]
try:
    fich = sys.argv[1]
    karaoke = KaraokeLocal(fich)
    karaoke.__str__()
    karaoke.do_local()
    karaoke.__str__()
except IndexError:
    print "Usage: python karaoke.py file.smil"
