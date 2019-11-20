class País:
    def __init__(self,nome,capital,dimensao,paises=[]):
        self.nom=nome
        self.cap=capital
        self.dim=dimensao
        self.pai=paises
    def get_nome(self):
        return self.nom
    def get_capital(self):
        return self.cap
    def get_dimensao(self):
        return self.dim
    def get_paises(self):
        return self.pai
    def adiciona_pai(self,novo_pai):
        try:
            self.pai.index(novo_pai)
        except:
            self.pai.append(novo_pai)
pais1=País('Brasil','Brasília','8',['Uruguai','Argentina','Chile'])
pais1.adiciona_pai('Armênia')
pais1.adiciona_pai('Uruguai')
print('Nome:',pais1.nom,'\n','Capital:',pais1.cap,'\n','Dimensão:',pais1.dim,'km2','\n','Fronteira:',pais1.pai)


