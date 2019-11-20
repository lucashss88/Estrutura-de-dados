def encontra_indice(chave, chaves):
    for i in range(len(chaves)):
        if (chaves[i] == chave):
            return i
    return '–1'
p = [1,2,3,4,5,6,7,8,9]
chave = 5
index = encontra_indice(chave, p)
print(index)