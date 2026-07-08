#!/usr/bin/env python3
import sys

def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)

# isinstance()
# verifica se um objeto pertence a um determinado tipo (classe).
# return True or False

#  Default Parameter
# Um default parameter é um parâmetro de função que já possui 
# um valor definido. Isso significa que, 
# se o usuário não passar um argumento, a função utilizará esse valor padrão.

# def saudacao(nome="Visitante"):
    # print(f"Olá, {nome}!")