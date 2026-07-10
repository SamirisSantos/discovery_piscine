#!/usr/bin/env python3
def array_of_names(names):
    return [f"{key.capitalize()} {value.capitalize()}" for key, value in names.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))

# .items()
# O Python olha para o dicionário names 
# que você enviou e usa o método .items().
