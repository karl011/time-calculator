from flask import Flask, request, render_template
from fonctions import saisir_duree, calcul_duree, afficher_duree

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultat', methods=['POST'])
def resultat():
    duree1_jours = int(request.form['duree1_jours'])
    duree1_heures = int(request.form['duree1_heures'])
    duree1_minutes = int(request.form['duree1_minutes'])
    duree1_secondes = int(request.form['duree1_secondes'])
    duree2_jours = int(request.form['duree2_jours'])
    duree2_heures = int(request.form['duree2_heures'])
    duree2_minutes = int(request.form['duree2_minutes'])
    duree2_secondes = int(request.form['duree2_secondes'])
    operation = request.form['operation']
    duree1 = saisir_duree(duree1_jours, duree1_heures, duree1_minutes, duree1_secondes)
    duree2 = saisir_duree(duree2_jours, duree2_heures, duree2_minutes, duree2_secondes)
    if isinstance(duree1, str) or isinstance(duree2, str):
        return duree1 or duree2
    resultat = calcul_duree(duree1, duree2, operation)
    return render_template('resultat.html', resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)