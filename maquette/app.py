from flask import Flask, render_template, url_for, flash, request, redirect
import pyodbc as odbc


DSN = 'Driver={SQL Server};Server=DESKTOP-DU03FQL\\SQLEXPRESS;Database=Gestion_des_Magasins;'
conn = odbc.connect(DSN)
cursor = conn.cursor()
# uid = <username>;
# pwd = <password>;



app = Flask(__name__)
app.config['SECRET_KEY']='clés_flash'


@app.route("/")
def index():
    return render_template("page1.html")


@app.route("/page2/")
def page2():
    return render_template("page2.html")


@app.route("/page3/")
def page3():
    return render_template("page3.html")


@app.route("/page4/", methods=["GET", "POST"])
def page4():
    if request.method == "POST":
        Nom = request.form["Nom"]
        Adresse = request.form["Adresse"]
        Telephone = request.form["Telephone"]
        email = request.form["email"]

        DSN = 'Driver={SQL Server};Server=DESKTOP-DU03FQL\\SQLEXPRESS;Database=Gestion_des_Magasins;'
        conn = odbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Magasin (NomMagasin, Adresse, Telephone, Email)
            VALUES (?, ?, ?, ?)
          ''', (Nom, Adresse, Telephone, email))
        conn.commit()
        conn.close()
        # flash("Votre Magasin a été enregistré avec succès !", 'info')
        return redirect(url_for('pages5'))
    data = ''
    return render_template("page4.html", data=data)

@app.route("/pages5", methods=['GET','POST'])
def pages5():
    DSN = "Driver={SQL Server};Server=DESKTOP-DU03FQL\\SQLEXPRESS;Database=Gestion_des_Magasins;"
    conn = odbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("select * from Magasin")
    data = cursor.fetchall()
    conn.close()
    return render_template("pages5.html", data = data)

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item_id = int(item_id)

    # Connexion à la base de données
    conn = odbc.connect(DSN)

    # Création d'un objet curseur
    cursor = conn.cursor()

    # Récupération des données du magasin depuis la base de données
    cursor.execute('SELECT * FROM magasin WHERE IdMagasin = ?', (item_id,))
    data = cursor.fetchone()

    # Si la méthode de la requête est POST, mise à jour des données du magasin dans la base de données
    if request.method == 'POST':
        # Récupération des données du formulaire
        Nom = request.form['Nom']
        Adresse = request.form['Adresse']
        Telephone = request.form['Telephone']
        email = request.form['email']

        # Mise à jour des données du magasin dans la base de données
        cursor.execute('''
            UPDATE Magasin
            SET NomMagasin = ?, Adresse = ?, Telephone = ?, Email = ?
            WHERE IdMagasin = ?
        ''', (Nom, Adresse, Telephone, email, item_id))

        # Validation des modifications dans la base de données
        conn.commit()

        # Fermeture de la connexion à la base de données
        conn.close()

        # Affichage d'un message de succès à l'utilisateur
        flash(f'Le magasin numéro {item_id} a été modifié avec succès !', 'info')

        # Redirection de l'utilisateur vers la page du magasin
        return redirect(url_for('pages5'))

    # Retour du modèle de formulaire du magasin
    return render_template('page4.html', data=data)

@app.route('/delete/<int:item_id>', methods=['GET', 'POST'])
def delete(item_id):
    item_id = int(item_id)

    conn = odbc.connect(DSN)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Magasin WHERE IdMagasin = ?', (item_id,))

    conn.commit()
    conn.close()

    flash(f'Le magasin numéro {item_id} a été supprimé avec succès !', 'info')
    return redirect(url_for('pages5'))


@app.route("/page6/")
def page6():
    return render_template("page6.html")


@app.route("/page7/")
def page7():
    return render_template("page7.html")


@app.route("/page8/")
def page8():
    return render_template("page8.html")


@app.route("/page9/")
def page9():
    return render_template("page9.html")


if __name__ == "__main__":
    app.run()
