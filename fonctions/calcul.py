def calcul_duree(duree1, duree2, operation):
    """Calcul de la somme ou de la différence de deux durées"""
    j1, h1, m1, s1 = duree1
    j2, h2, m2, s2 = duree2
    if operation == "+":
        secondes_totales = s1 + s2
        minutes_totales = m1 + m2 + secondes_totales // 60
        secondes_totales %= 60
        heures_totales = h1 + h2 + minutes_totales // 60
        minutes_totales %= 60
        jours_totaux = j1 + j2 + heures_totales // 24
        heures_totales %= 24
    elif operation == "-":
        secondes_totales = s1 - s2
        minutes_totales = m1 - m2
        heures_totales = h1 - h2
        jours_totaux = j1 - j2
        if secondes_totales < 0:
            minutes_totales -= 1
            secondes_totales += 60
        if minutes_totales < 0:
            heures_totales -= 1
            minutes_totales += 60
        if heures_totales < 0:
            jours_totaux -= 1
            heures_totales += 24
        if jours_totaux < 0:
            print("La deuxième durée est supérieure à la première.")
            return None
    return jours_totaux, heures_totales, minutes_totales, secondes_totales