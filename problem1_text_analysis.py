def analyser_texte(phrase):
    phrase = phrase.lower()
    mots = phrase.split()
    
    nb_mots = len(mots)

    mot_long = max(mots, key=len)
    
    nb_voyelles = 0
    for lettre in phrase:
        if lettre in "aeiouy":
            nb_voyelles += 1

    nouvelle_phrase = []
    for mot in mots:
        if len(mot) % 2 == 0:
            nouvelle_phrase.append(mot.upper())
        else:
            nouvelle_phrase.append(mot)

    print("Mots :", nb_mots)
    print("Plus long :", mot_long)
    print("Voyelles :", nb_voyelles)
    print("Phrase :", " ".join(nouvelle_phrase))

phrase = input("Entrez une phrase : ")
analyser_texte(phrase)