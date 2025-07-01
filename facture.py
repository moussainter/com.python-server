#coding:utf-8
import cgi

print("Content-Type: text/html; charset=utf-8\n")

html = """
<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Facture</title>
<head>
<body>
    <h1>Facture</h1>
    <p>Cette page est une facture.</p>
    
    <form method="post" action="result.py">
        <p> <input type="text" name="name" placeholder="Votre nom" required> </p>
        <input type="submit" value="Envoyer">
    </form>

</body>
</html>
"""
print(html)
        