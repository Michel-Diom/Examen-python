students = [
    ("Ali", 12),
    ("Fatou", 17),
    ("Moussa", 9),
    ("Awa", 14),
    ("Ibrahima", 7)
]

def calculer_resultats(liste):
    notes = [etudiant[1] for etudiant in liste] 
    admis = []
    
    for nom, note in liste:
        if note >= 10:
            admis.append(nom)
    
    admis.sort()
    
    moyenne = sum(notes) / len(notes)
    return moyenne, max(notes), admis


def afficher_tout(moyenne, note_max, admis):
    print("Moyenne de la classe :", moyenne)
    print("Meilleure note :", note_max)
    print("Étudiants admis :", admis)


moy, maximum, liste_admis = calculer_resultats(students)
afficher_tout(moy, maximum, liste_admis)