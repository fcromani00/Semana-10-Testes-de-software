def converte(numeroEmRomano):
    tabela = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000 
    }

    acumulador = 0
    ultimovizinhodireita = 0
    for i in reversed(range(len(numeroEmRomano))):
        atual = tabela[numeroEmRomano[i]]

       
        if atual < ultimovizinhodireita:
            acumulador -= atual
        else:
            acumulador += atual

        ultimovizinhodireita = atual

    return acumulador
