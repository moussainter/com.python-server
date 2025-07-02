#coding:utf-8
import cgi


print("Content-Type: text/html; charset=utf-8\n")

html = """
<!DOCTYPE html>
<html lang="fr">
  <head>
    
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Facture</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 40px;
        border: solid 2px #333;
      }
      table {
        border-collapse: collapse;
        width: 70%;
        margin: 20px;
      }
      th,
      td {
        border: 1px solid #333;
        padding: 8px 12px;
        text-align: left;
      }
      th {
        background-color: #bab3b3;
      }
      tfoot td {
        font-weight: bold;
      }
      .form1 {
        margin-left: 20px;
      }
      .center {
        text-align: left;
        margin-left: 20px;
      }
      #btn {
        background-color: #4caf50;
        color: white;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        margin-left: 20px;
      }
    </style>
  </head>
  <body>
    <h2 class="center">Facture</h2>
    <form action="result.py" method="post">
      <div class="form1">
        <label>Numéro</label>
        <input type="text" name="numero" id="numero" value="Numero fact." />
        <span>&nbsp; </span><span>&nbsp; </span>
        <label> Date</label>
        <input type="date" name="date" id="date" value="2023-10-01" />
        <span>&nbsp; </span><span>&nbsp; </span>
        <label>Client</label>
        <select name="client" id="client">
          <option value="clt1">Client 1</option>
          <option value="clt2">Client 2</option>
          <option value="clt3">Client 3</option>
          <option value="clt4">Client 4</option>
        </select>
      </div>
      <div class="form">
        <table>
          <thead>
            <tr>
              <th>Produit</th>
              <th>Quantité</th>
              <th>Prix Unitaire (€)</th>
              <th>Total (€)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input type="text" name="produit" id="produit1" /></td>
              <td><input type="text" name="quantite" id="quantite1" /></td>
              <td><input type="text" name="prix" id="prix1" /></td>
              <td><input type="text" name="total" id="total1" readonly /></td>
            </tr>
            <tr>
              <td><input type="text" name="produit" id="produit2" /></td>
              <td><input type="text" name="quantite" id="quantite2" /></td>
              <td><input type="text" name="prix" id="prix2" /></td>
              <td><input type="text" name="total" id="total2" readonly /></td>
            </tr>
            <tr>
              <td><input type="text" name="produit" id="produit3" /></td>
              <td><input type="text" name="quantite" id="quantite3" /></td>
              <td><input type="text" name="prix" id="prix3" /></td>
              <td><input type="text" name="total" id="total3" readonly /></td>
            </tr>

            <tr>
              <td colspan="3" class="center">Total HT</td>
              <td><input type="text" name="totalHT" id="totalHT">&nbsp;€</td>
            </tr>
            <tr>
              <td colspan="3" class="center">TVA (20%)</td>
              <td><input type="text" name="tva" id="tva">&nbsp;€</td>
            </tr>
          </tbody>
          <tfoot>
            <tr>
              <td colspan="3" class="center">Total TTC</td>
              <td><input type="text" name="montantTTC" id="montantTTC">&nbsp;€</td>
            </tr>
          </tfoot>
        </table>

        <input type="submit" value="Valider" id="btn" />
        <br /><br />
      </div>
    </form>
  </body>
  <script>
  
    function produit() {
        let quantite1 = document.getElementById("quantite1").value;
        let prix1 = document.getElementById("prix1").value;
        let total1 = document.getElementById("total1");
        if (quantite1 == "" || prix1 == "") {
            total1.value = "";
        } 
        else {
        total1.value = parseFloat(quantite1) * parseFloat(prix1);}
        }
            
    let quantite1 = document.getElementById("quantite1");
    let prix1 = document.getElementById("prix1");
    let total = document.getElementById("total1");
    
    quantite1.addEventListener("change", produit, false);
    prix1.addEventListener("change", produit, false);
  </script>
</html>

"""

print(html)
        