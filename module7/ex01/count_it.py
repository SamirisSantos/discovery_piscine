#!/usr/bin/env python3
import sys
if len(sys.argv) == 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    for argument in sys.argv[1:]:
        print(f"{argument}: {len(argument)}")

# if len(sys.argv) == 1:
#     print("none")
# else:
#     print(f"parameters: {len(sys.argv) - 1}")
#     len_arg = len(sys.argv) - 1
#     for argument in sys.arv[1:]
#         count = 0
#         for caractere in sys.argv[i]:
#             count += 1
#         print(f"{sys.argv[i]}: {count}")

# -- about slicing

# Slicing

# A estrutura completa do fatiamento é lista[início:fim:passo].
# Quando omitimos o valor depois dos dois pontos, 
# o Python entende que deve ir até o final da lista

# frutas = ['maçã', 'banana', 'laranja', 'uva']
# Índices:   0         1          2        3
# resultado = frutas[1:]
# print(resultado) 
# Saída: ['banana', 'laranja', 'uva']