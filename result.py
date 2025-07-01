#coding:utf-8
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue("username"):
    username = form.getvalue("username")
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

print(f"Blonjour {username} !")

html="""
    
   
</body>
</html>
"""
print(html)