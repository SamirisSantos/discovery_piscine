#!/usr/bin/env python3

#def is_red(name):
#	return family[name] == "red"

def find_the_redheads(family):
    # filter(is_red,family.keys())
    redheads = filter(lambda name: family[name] == "red", family.keys())
    return list(redheads)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))

# family.keys() Pega todos os nomes (as chaves do dicionário)
# filter() Passa por cada nome e mantém só os que têm family[name] == "red"
# lambda parametros: expressão | função pequena e sem nome (função anônima), tudo numa única linha.
# lambda → palavra-chave que diz "vou criar uma função aqui", 
# list(...)Converte o objeto filter (que é um iterador) numa lista de verdade