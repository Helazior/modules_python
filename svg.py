#!/usr/bin/env python3

"""
Un module pour générer des images au format SVG.

Ce module fournit diverses fonctions pour générer des éléments SVG
sous forme de chaînes de caractères.
Ces chaînes DOIVENT être écrites dans un fichier en respectant la
structure SVG pour obtenir une image valide.
"""

from collections import namedtuple

# Definition de la structure Point composée de deux attributs x et y
Point = namedtuple('Point', 'x y')

def genere_balise_debut_image(largeur, hauteur):
    """
    Retourne la chaine de caractères correspondant à la balise ouvrante pour
    décrire une image SVG de dimensions largeur x hauteur pixels. Les paramètres
    sont des entiers.
    Remarque : l’origine est en haut à gauche et l’axe des Y est orienté vers le
    bas.
    """
    return "<svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='" + str(largeur) + "' height='" + str(hauteur) + "'>"

def genere_balise_fin_image():
    """
    Retourne la chaine de caractères correspondant à la balise svg fermante.
    Cette balise doit être placée après tous les éléments de description de
    l’image, juste avant la fin du fichier.
    """
    return "</svg>"

def genere_balise_debut_groupe(couleur_ligne, couleur_remplissage, epaisseur_ligne):
    """
    Retourne la chaine de caractères correspondant à une balise ouvrante
    définissant un groupe d’éléments avec un style particulier. Chaque groupe
    ouvert doit être refermé individuellement et avant la fermeture de l’image.
    Les paramètres de couleur sont des chaînes de caractères et peuvent avoir
    les valeurs :
    -- un nom de couleur reconnu, par exemple "red" ou "black" ;
    -- "none" qui signifie aucun remplissage (attention ici on parle de la chaîne
        de caractère "none" qui est différente de l'objet None).
    Le paramètre d’épaisseur est un nombre positif ou nul, représentant la
    largeur du tracé d'une ligne en pixels.
    """
    return "    <g stroke='"+couleur_ligne+"' stroke-width='"+str(epaisseur_ligne)+"' fill='"+couleur_remplissage+"'>"

def genere_balise_fin_groupe():
    """
    Retourne la chaine de caractères correspondant à la balise fermante pour un
    groupe d’éléments.
    """
    return "    </g>"

def genere_cercle(centre, rayon):
    """
    Retourne la chaine de caractères correspondant à un élément SVG représentant
    un cercle (ou un disque, cela dépend de la couleur de remplissage du groupe
    dans lequel on se trouve).
    centre est une structure de données de type Point, et rayon un nombre de
    pixels indiquant le rayon du cercle.
    """
    return "        <circle cx='"+str(centre.x)+"' cy='"+str(centre.y)+"' r='"+str(rayon)+"'/>"

def genere_segment(dep, arr):
    """
    Retourne la chaîne de caractères correspondant à un
    ségment SVG. Ce segment relie les points dep et arr.
    """
    return "        <line x1=\"" + str(dep.x) + "\" y1=\"" + str(dep.y) + "\" x2=\"" + str(arr.x) +"\" y2=\"" + str(arr.y) + "\"/>"

def genere_polygone(points):
    chaine_retour = "       <polygon points=\""
    for point in points:
        chaine_retour += str(int(point[0])) + "," + str(int(point[1])) + " "
    chaine_retour = chaine_retour[:-1] + "\"/>"
    return chaine_retour

def genere_rectangle(coordonnee, taille):
    """
    genere_rectangle(nametuple coordonnee, namedtaple taille)
    return genere_polygone de 4 points formant un carre
    """
    points = [coordonnee, (coordonnee.x + taille.x, coordonnee.y), (coordonnee.x + taille.x, coordonnee.y + taille.y), (coordonnee.x, coordonnee.y + taille.y)]
    return genere_polygone(points)

def genere_text(pos, text):
    """
    affiche un texte
    la position est un numedtuple
    """
    return "    <text x=\""+ str(pos.x)+ "\" y=\""+ str(pos.y) +"\">"+text+"</text>"


def genere_balise_debut_groupe_transp(niveau_opacite):
    return "    <g opacity='"+niveau_opacite+"'>"

def genere_balise_debut_groupe_taille_police(taille_police):
    return "    <g font-size='"+str(taille_police)+"'>"
