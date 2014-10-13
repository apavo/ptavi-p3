#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista = []

    def startElement(self, name, attrs):

        if name == "root-layout":
            self.rootlayout = {}
            self.guardar(attrs, self.rootlayout)
            self.lista.append([name, self.rootlayout])
        elif name == "region":
            self.region = {}
            self.guardar(attrs, self.region)
            self.lista.append([name, self.region])
        elif name == "img":
            self.img = {}
            self.guardar(attrs, self.img)
            self.lista.append([name, self.img])
        elif name == "audio":
            self.audio = {}
            self.guardar(attrs, self.audio)
            self.lista.append([name, self.audio])
        elif name == "textstream":
            self.textstream = {}
            self.guardar(attrs, self.textstream)
            self.lista.append([name, self.textstream])

    def guardar(self, attrs, diccionario):
        atributos = attrs.keys()
        n = 0
        while n < len(atributos):
            diccionario[str(atributos[n])] = str(attrs.get(atributos[n], ""))
            n = n + 1

    def get_tags(self):
        return self.lista

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
