class Fila:
    def __init__(self,head=None):
        self._head=head
    def remove(self):
        self._head=self._head.get_proximo()
    def add(self,no):
        p=self._head
        while(p.get_proximo()!=None):
            p=p.get_proximo()
        p.set_proximo(no)
    def printAll(self):