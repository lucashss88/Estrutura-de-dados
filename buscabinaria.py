def encontra_indice_binaria(chave, chaves):
    limiteInf = 0
    limiteSup = len(chaves) - 1
    metade = 0
    while (limiteInf <= limiteSup):
        metade = (limiteInf + limiteSup)//2
        if (chaves[metade] == chave):
            return metade
        if (chave < chaves[metade]):
            limiteSup = metade - 1
        else:
            limiteInf = metade + 1

    return '–1' # chave não encontrada
chaves = [1,2,3,4,5,6,7,8,9,10]
chave = 8
index = encontra_indice_binaria(chave, chaves)
print(index)