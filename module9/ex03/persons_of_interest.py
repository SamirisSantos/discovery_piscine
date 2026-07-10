#!/usr/bin/env python3
def famous_births(persons):
    sorted_persons = sorted(persons.values(), key=lambda person: person["date_of_birth"])
    for person in sorted_persons:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

women_scientists = {
    "ada": {
        "name": "Ada Lovelace",
        "date_of_birth": "1815"
    },
    "cecilia": {
        "name": "Cecila Payne",
        "date_of_birth": "1900"
    },
    "lise": {
        "name": "Lise Meitner",
        "date_of_birth": "1878"
    },
    "grace": {
        "name": "Grace Hopper",
        "date_of_birth": "1906"
    }
}

famous_births(women_scientists)

# Ada Lovelace (1815–1852) — 
# 	matemática britânica considerada a primeira programadora da história, 
# 	por seu trabalho com a máquina analítica de Charles Babbage.

# Lise Meitner (1878–1968) — 
# 	física austríaca que ajudou a descobrir a fissão nuclear, 
# 	mas foi injustamente excluída do Prêmio Nobel dado a seu colega Otto Hahn.

# Cecilia Payne (1900–1979) — 
# 	astrônoma britano-americana que descobriu que as estrelas são compostas 
# 	majoritariamente de hidrogênio e hélio, revolucionando a astrofísica.

# Grace Hopper (1906–1992) — matemática e almirante da marinha americana, 
# 	pioneira da computação que criou um dos primeiros compiladores e 
# 	ajudou a desenvolver a linguagem COBOL.