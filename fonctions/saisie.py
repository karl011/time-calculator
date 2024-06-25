def saisir_duree(jours, heures, minutes, secondes):
    """Saisie d'une durée sous forme de jours, heures, minutes et secondes"""
    if not (isinstance(jours, int) and isinstance(heures, int) and isinstance(minutes, int) and isinstance(secondes, int)):
        return "Durée invalide. Veuillez saisir une durée sous la forme JJ:HH:MM:SS."
    if secondes < 0 or secondes >= 60:
        return "Durée invalide. Veuillez saisir une durée sous la forme JJ:HH:MM:SS."
    if minutes < 0 or minutes >= 60:
        return "Durée invalide. Veuillez saisir une durée sous la forme JJ:HH:MM:SS."
    if heures < 0 or heures >= 24:
        return "Durée invalide. Veuillez saisir une durée sous la forme JJ:HH:MM:SS."
    if jours < 0:
        return "Durée invalide. Veuillez saisir une durée sous la forme JJ:HH:MM:SS."
    return jours, heures, minutes, secondes