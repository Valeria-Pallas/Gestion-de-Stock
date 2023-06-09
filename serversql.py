import tkinter as tk
import mysql.connector
import csv

"""mysql> CREATE DATABASE magasin;
Query OK, 1 row affected (0,07 sec)

mysql> USE magasin;
Database changed
mysql> CREATE TABLE produit (
    -> id int primary key auto_increment,
    -> nom varchar (255),
    -> description text,
    -> prix int,
    -> id_categorie int);
Query OK, 0 rows affected (0,13 sec)

mysql> CREATE TABLE categorie (
    -> id int primary key auto_increment,
    -> nom varchar (255));
Query OK, 0 rows affected (0,04 sec)
"""

serversql = tk.Tk()
class Produits:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="velvet",
            database="magasin"
        )
        
        self.mycursor = self.db.cursor()
    
    def create(self, nom, description ,prix, quantite, id_categorie):
        sql = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
        val = (nom, description, prix, quantite, id_categorie),
        self.mycursor.execute(sql, val),
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement inséré.")
        
    def read (self):
        self.mycursor.execute("SELECT * FROM produit")
        result = self.mycursor.fetchall()
        for row in result:
            print(row)
            
    def update(self, id, nom, description, prix, quantite, id_categorie):
        sql = "UPDATE produit SET nom = %s, description =%s, prix = %s, quantite = %s, id_categorie = %s WHERE id = %s"
        val = (nom, description, prix, quantite, id_categorie, id)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement(s) mis a jour.")
    
    def delete(self, id):
        sql = "DELETE FROM produit WHERE id = %s"
        val = (id)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement(s) supprimé(s).")

class Categorie:
    def __init__(self):
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="velvet",
        database="magasin"
        )
        self.mycursor = self.db.cursor()
        mycursor = db.cursor()
        mycursor.execute("SELECT SUM(nom) FROM categorie")
        result = mycursor.fetchoquantite()
        print("superficie totale des categories:", result[0])
        
    def create(self, nom):
        sql = "INSERT INTO categorie nom) VALUES (%s, %s)"
        val= (nom)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement inséré.")
        
    def read(self,):
        self.mycursor.execute("SELECT * FROM categorie")
        result = self.mycursor.fetchall()
        for row in result:
            print(row)
    
    def update(self, id, nom):
        sql = "UPDATE categorie SET nom = %s WHERE id = %s"
        val = (nom, id)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement(s) modifié(s)")
    
    def delete(self, id):
        sql = "DELETE FROM categorie WHERE id = %s"
        val = (id,)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement(s) supprimé")



# create the widgets for the serversql
nom_label = tk.Label(serversql, text="nom")
nom_entry = tk.Entry(serversql)
description_label = tk.Label(serversql, text="description")
description_entry = tk.Entry(serversql)
prix_label = tk.Label(serversql, text="prix")
prix_entry = tk.Entry(serversql)
quantite_label = tk.Label(serversql, text="quantite")
quantite_entry = tk.Entry(serversql)
id_categorie_label = tk.Label(serversql, text="id_categorie")
id_categorie_entry = tk.Entry(serversql)
add_button = tk.Button(serversql, text="Add", command=Produits)

# position the widgets on the serversql
nom_label.grid(row=0, column=0)
nom_entry.grid(row=0, column=1)
description_label.grid(row=1, column=0)
description_entry.grid(row=1, column=1)
prix_label.grid(row=2, column=0)
prix_entry.grid(row=2, column=1)
quantite_label.grid(row=3, column=0)
quantite_entry.grid(row=3, column=1)
id_categorie_label.grid(row=4, column=0)
id_categorie_entry.grid(row=4, column=1)
add_button.grid(row=5, column=1)

 #establish MySQL connection and cursor
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="magasin"
)
cursor = db.cursor()

# execute SQL query to select data from table
cursor.execute("SELECT * FROM produit")

# get all rows of data from cursor
rows = cursor.fetchall()

# open CSV file in write mode
with open("produit.csv", "w", newline="") as csvfile:
    # create CSV writer
    writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # write header row
    writer.writerow(["id", "nom", "description","prix", "id_categorie"])
    
    # write data rows
    for row in rows:
        writer.writerow(row)

# close cursor and MySQL connection
cursor.close()
db.close()

#Sur le tableau de bord, la liste complète des produits en stock sont affichés. L’utilisateur
#doit avoir la possibilité d’ajouter un produit, de supprimer un produit et de modifier le
#produit (stock, prix, ...).


# Open the CSV file and read its contents
with open('produit.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    rows = list(reader)

# Create a listbox to display the contents of the CSV file
listbox = tk.Listbox(serversql)
for row in rows:
    listbox.insert(tk.END, ', '.join(row))


# Add the listbox to the serversql and pack it
listbox.pack()


# Run the serversql
serversql.mainloop()
