#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module qui vérifie les arguments d'entrés d'un  programme.
Utilisation: check( ["type[ name][ min max]", "type[ name][ min max]",...] )
où type peut-être: "all", "file", "dir", "int", "float",
"str", "bool", "list", "tuple", "dict")
[name] est optionnel
[min max] sont disponibles pour les int et les float

- print un message d'erreur en cas de non castabilité (sans perte) du type,
puis print le message d'utilisation et s'arrête.
- Dans le cas contraire, le programme ne fait rien.
"""

import sys
import os
from collections import namedtuple
Parametre = namedtuple("Parametre", ["type", "name", "min", "max"])

#A FAIRE: (mettre TO DO enlève des points pylint)
#4 rajouter les arguments optionnels
#5/liste de int, de char etc.
#6 mettre un mode non verbeux
#7 demander que le fichier soit lisible etc.
#8 pouvoir mettre uniquement un min et non 'min max'

def utilisation(tab_argv):
    """indique comment utiliser le programme"""
    print("\nUtilisation:", sys.argv[0], end=' ')
    for num_arg in range(len(tab_argv.type)):
        print("(", tab_argv.type[num_arg], ")", tab_argv.name[num_arg], sep='', end=' ')
    print()
    sys.exit(1)

def split_argv(tab_argv):
    """prend une list de ["type[ name][ min max ]", "type[ name][ min max ]",...] et la split en
    une liste de type et une liste de name. name est remplacé par "" lorsqu'il
    n'est pas donné. De même pour min et max"""
    tab_type_argv = list()
    tab_name_argv = list()
    tab_min_argv = list()
    tab_max_argv = list()
    for argv in tab_argv:
        try:
            arg = argv.split()
        except AttributeError:
            arg = [None, None]#est traité dans la suite du code
        tab_type_argv.append(arg[0])
        try:
            tab_name_argv.append(arg[1])
        except IndexError:
            tab_name_argv.append("") #si on ne précise pas le nom
        else:
            #si on a un deuxième argument, on peut rajouter un min et un max
            try:
                tab_min_argv.append(arg[2])
                tab_max_argv.append(arg[3])
            except IndexError:
                tab_min_argv.append("")
                tab_max_argv.append("")


    return Parametre(tab_type_argv, tab_name_argv, tab_min_argv, tab_max_argv)

def check_error(tab_argv):
    """check le nombre d'arguments, et les types"""
    dic_str_to_type = {"all": all, "file": "file", "dir": dir, "int": int, "float": float,\
                     "str": str, "bool": bool, "list": list, "tuple": tuple, "dict": dict}

    nb_valide_arg = len(tab_argv)
    nb_arg_entre = len(sys.argv) - 1

    tab_argv = split_argv(tab_argv)
    try:
        if nb_arg_entre == 1 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            utilisation(tab_argv)
        assert len(sys.argv) - 1 == nb_valide_arg
        for num_arg in range(nb_valide_arg):
            #on verifie que le programmeur a bien demandé un type qui existe:
            type_argv = dic_str_to_type[tab_argv.type[num_arg]] #peut lèver KeyError
            argument = sys.argv[num_arg + 1]
            if type_argv == "file":#cas particulier
                if not os.path.isfile(argument):
                    print("L'argument", argument, "doit être un fichier existant.")
                    utilisation(tab_argv)
                continue
            elif type_argv == dir:#cas particulier
                if not os.path.isdir(argument):
                    print("L'argument", argument, "doit être un dossier existant.")
                    utilisation(tab_argv)
                continue
            #on convertit la chaine "argument" avec le type voulu,
            #cela va lever l'exception "ValueError" si ce n'est pas possible
            #Avantage: puissant et court
            #Désavantage: peut laisser passer trop de choses
            argument_value = type_argv(argument) #peut lever ValueError

            if (type_argv == int or type_argv == float) and tab_argv.min[num_arg] != "":
                try:
                    min_value = type_argv(tab_argv.min[num_arg])
                    max_value = type_argv(tab_argv.max[num_arg])
                    assert min_value <= argument_value and argument_value <= max_value
                except AssertionError:
                    print("Erreur : on veut: ", min_value, " ⩽ ", tab_argv.name[num_arg], " ⩽ ",\
                    max_value, "\net ", tab_argv.name[num_arg], " = ", argument_value, sep='')
                    utilisation(tab_argv)

    except AssertionError:
        print(f"Erreur : Il faut {nb_valide_arg} paramètre(s) et non {len(sys.argv) - 1}.")
        utilisation(tab_argv)

    except ValueError:
        if tab_argv.name[num_arg]:
            print("Erreur : l'argument numéro ", num_arg + 1, " \"", tab_argv.name[num_arg]\
                  , "\" doit-être un ", tab_argv.type[num_arg], sep='')
        else:
            print("Erreur : l'argument numéro", num_arg + 1, \
                  "doit-être un", tab_argv.type[num_arg])
        utilisation(tab_argv)

    except KeyError:
        print("Erreur utilisation dans le programme: type inconnu. types accepté:\
            \n'all', 'file', 'dir', 'int', 'float', 'str', 'bool', 'list', 'tuple', 'dict'")
        sys.exit(2)

    #except PermissionError:
    #    print("Vous n'avez pas les permissions d'écrire")


def check(tab_argv):
    """Utilisation: check( tab_argv[] )
    où type_argv peut-être: all, file, dir, int, float, str, list, tuple, dict, bool)
    on peut également préciser le nom: "file nom.txt, int age, etc."""

    check_error(tab_argv)
