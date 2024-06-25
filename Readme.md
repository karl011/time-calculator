# Mini projet "time-calculator"
"time-calculator" est un outil de calcul de durée qui permet aux utilisateurs d'ajouter et de soustraire des durées sous forme de jours, d'heures, de minutes et de secondes. L'outil est implémenté en Python et utilise le framework Flask pour fournir une interface web conviviale. Les utilisateurs peuvent saisir deux durées et choisir l'opération à effectuer (addition ou soustraction). L'outil renvoie alors le résultat sous forme de durée.

Le référentiel contient le code source de l'application, ainsi que les instructions pour l'installer et l'exécuter localement. Le code est organisé en plusieurs modules pour faciliter la maintenance et le développement futur.

# Démarrer time-calculator pour calculer des heures
1. Pour créer un environnement virtuel, vous pouvez utiliser la commande 
```bash
python -m venv env
```
2. Puis activer l'environnement virtuel avec la commande
```bash
source env/bin/activate
```
(sur Linux/Mac) ou
```bash
env\Scripts\activate
```
(sur Windows)

3. Lancez l'application Flask en exécutant le fichier app.py dans votre terminal :
```bash
python app.py
```
4. Ouvrez votre navigateur web et accédez à l'adresse http://127.0.0.1:5000/ pour afficher la page d'accueil de votre application.

5. Pour désactiver l'environnement virtuel dans votre terminal, vous pouvez utiliser la commande ```deactivate```
(sous Windows) ou 
```source deactivate```
(sous Linux/Mac). Cette commande doit être exécutée dans le terminal où vous avez activé l'environnement virtuel.
# Installation des dépendances

### 1. Pour installer Flask, vous pouvez utiliser la commande dans votre terminal.
```bash
pip install flask
```
Assurez-vous que vous utilisez la bonne version de pip correspondant à votre environnement Python (par exemple, pip3 pour Python 3).

Si vous rencontrez des problèmes d'installation, vous pouvez essayer d'utiliser un environnement virtuel Python pour isoler votre application Flask des autres bibliothèques installées sur votre système.
Pour créer un environnement virtuel, vous pouvez utiliser la commande 
```bash
python -m venv env
```
dans votre terminal, puis activer l'environnement virtuel avec la commande
```bash
source env/bin/activate
```
(sur Linux/Mac) ou
```bash
env\Scripts\activate
```
(sur Windows).
Vous pouvez ensuite installer Flask dans l'environnement virtuel avec la commande
```bash
pip install flask
```
### 2. Lancez l'application Flask en exécutant le fichier app.py dans votre terminal :
```bash
python app.py
```