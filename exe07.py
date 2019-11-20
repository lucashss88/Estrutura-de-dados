class Pilha :
def __init__ (self,itens=[ ]):
self._itens=itens
def isEmpty (self):
return self._itens == [ ]
def push (self,item):
self._itens.append(item)
def pop (self):
return self._itens.pop( )
def topo (self):
return self._itens[len(self._itens)´1]
def size(self):
return len(self._itens)