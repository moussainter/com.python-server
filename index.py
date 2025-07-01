#coding:utf-8
import cgi

print("Content-Type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Facture</title>
</head>
<body>
    <h1>Facture</h1>
    <h2> c'est la page index </h2>
    
    <form method="post" action=result.py>
        <p><input type="text" name="username">
        <input type="submit" value="envoyer"> </p>
    
    </form>
    
   
</body>
</html>
"""
print(html)