#coding:utf-8
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue("numero"):
    numero = form.getvalue("numero")
    date = form.getvalue("date")
    client = form.getvalue("client")
    protduit = form.getvalue("produit")
    quantite = form.getvalue("quantite")
    prix = form.getvalue("prix")
    total = form.getvalue("total")
    
    
    
   
    
    
else:
    raise Exception("Pseudo non transmis")


print("Content-Type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Facture</title>
</head>
<body>
    
    <h1>Facture</h1>
    <h2> c'est la page resultat </h2>
"""
print(html)
print(f"<h2>Numero: {numero}</h2>")
print(f"<h2>Date: {date}</h2>")
print(f"<h2>Client: {client}</h2>")
print(f"<h2>Produit: {protduit}</h2>")
print(f"<h2>Quantite: {quantite}</h2>")
print(f"<h2>Prix: {prix}</h2>")

html="""
    
   
</body>
</html>
"""
print(html)