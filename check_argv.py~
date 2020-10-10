#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module qui vérifie les arguments d'entrés d'un  programme.
Utilisation: check( ["type[ name]", "type[ name]",...] )
où type peut-être: "all", "file", "dir", "int", "float",
"str", "bool", "list", "tuple", "dict")
name est optionnel

- print un message d'erreur en cas de non castabilité (sans perte) du type,
puis print le message d'utilisation et s'arrête.
- Dans le cas contraire, le programme ne fait rien.

"""
import sys
import os
from collections import namedtuple
Parametre = namedtuple("Parametre", ["type", "name"])

#A FAIRE: (mettre TO DO enlève des points pylint)
#4 rajouter les arguments optionnels
#5/liste de int, de char etc.
#6 mettre un mode non verbeux

def utilisation(tab_argv):
    """indique comment utiliser le programme"""
    print("Utilisation:", sys.argv[0], end=' ')
    for num_arg in range(len(tab_argv.type)):
        print("(", tab_argv.type[num_arg], ")", tab_argv.name[num_arg], sep='', end=' ')
    print()
    sys.exit(1)

def separe_type_name(tab_argv):
    """prend une list de ["type[ name]", "type[ name]",...] et la splite en
    une liste de type et une liste de name. name est remplacé par "" lorsqu'il
    n'est pas donné."""
    tab_type_argv = list()
    tab_name_argv = list()
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

    return Parametre(tab_type_argv, tab_name_argv)

def check_error(tab_argv):
    """check le nombre d'arguments, et les types"""
    dic_str_to_type = {"all": all, "file": "file", "dir": dir, "int": int, "float": float,\
                     "str": str, "bool": bool, "list": list, "tuple": tuple, "dict": dict}

    nb_valide_arg = len(tab_argv)
    nb_arg_entre = len(sys.argv) - 1

    tab_argv = separe_type_name(tab_argv)
    try:
        if nb_arg_entre == 1 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            utilisation(tab_argv)
        assert len(sys.argv) - 1 == nb_valide_arg
        for num_arg in range(nb_valide_arg):
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
            type_argv(argument)

    except AssertionError:
        print("Il faut", nb_valide_arg, "paramètre(s) et non", len(sys.argv) - 1, ".")
        utilisation(tab_argv)

    except ValueError:
        if tab_argv.name[num_arg]:
            print("l'argument numéro ", num_arg + 1, " \"", tab_argv.name[num_arg]\
                  , "\" doit-être un ", tab_argv.type[num_arg], sep='')
        else:
            print("l'argument numéro", num_arg + 1, \
                  "doit-être un", tab_argv.type[num_arg])
        utilisation(tab_argv)

    except KeyError:
        print("Exception error: type inconnu. types accepté:\
            \n'all', 'file', 'dir', 'int', 'float', 'str', 'bool', 'list', 'tuple', 'dict'")
        sys.exit(2)

    #except PermissionError:
    #    print("Vous n'avez pas les permissions d'écrire")



def check(tab_argv):
    """Utilisation: check( tab_argv[] )
    où type_argv peut-être: all, file, dir, int, float, str, list, tuple, dict, bool)
    on peut également préciser le nom: "file nom.txt, int age, etc."""

    check_error(tab_argv)
