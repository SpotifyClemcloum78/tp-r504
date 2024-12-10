from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Fonction de validation des identifiants avec plusieurs regex
def validate_username(username):
    errors = []
    # Vérification : au moins 6 caractères
    if not re.match(r'^.{6,}$', username):
        errors.append("Doit contenir au moins 6 caractères.")
    # Vérification : au moins une lettre minuscule
    if not re.search(r'[a-z]', username):
        errors.append("Doit contenir au moins une lettre minuscule.")
    # Vérification : au moins une lettre majuscule
    if not re.search(r'[A-Z]', username):
        errors.append("Doit contenir au moins une lettre majuscule.")
    # Vérification : au moins un chiffre
    if not re.search(r'\d', username):
        errors.append("Doit contenir au moins un chiffre.")
    # Vérification : au moins un caractère spécial parmi #%{}@
    if not re.search(r'[#%{}@]', username):
        errors.append("Doit contenir au moins un caractère spécial parmi #%{}@.")
    return errors

# Route principale pour afficher la table et le formulaire
@app.route('/', methods=['GET', 'POST'])
def index():
    # Exemple de données pour la table
    data = [
        ["ID", "Nom", "Prénom"],
        [1, "Dupont", "Jean"],
        [2, "Martin", "Sophie"],
        [3, "Durand", "Paul"]
    ]

    # Variables pour les messages
    errors = None
    success_message = None

    if request.method == 'POST':
        # Récupération de l'identifiant saisi
        username = request.form.get('username', '')

        # Validation avec les regex
        errors = validate_username(username)
        if not errors:
            success_message = "Succès : L'identifiant est valide !"

    # Rendu de la page avec les données, les erreurs, et le message
    return render_template('index.html', data=data, errors=errors, success_message=success_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

