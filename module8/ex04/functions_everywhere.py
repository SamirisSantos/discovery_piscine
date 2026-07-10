#!/usr/bin/env python3
import sys

def shrink(str):
    return str[:8]

#print(shrink("physically"))

def enlarge(argument):
    if len(sys.argv) == 1:
        print("none")
    else:
        for arg in argument[1:]:
            if len(arg) > 8:
                print(shrink(arg))
            else:
                while len(arg) < 8:
                    arg += "z"
                print(arg)

enlarge(sys.argv)

# o método ljust()
# que completa a string até um tamanho desejado.
# texto = "abc"
# resultado = texto.ljust(8, "z")
# print(resultado)

# for arg in arguments[1:]:
#     if len(arg) > 8:
#         print(shrink(arg))
#     else:
#         print(arg.ljust(8, "z"))