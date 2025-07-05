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
        margin-left: 20px;
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
        padding: center;
        border: none;
        margin-top: 15px;
        style: bold;
        width: 100px;
        height: 35px;
        
        
      }
      
      #tableau, #button {
        border: solid 1px #333;
        float: left;
        }
        
      #button {
        margin-left: 20px;
        width: 150px;
        height: 35px;
        }
        
      #plus, #moins {
        width: 55px;
        height: 35px;
        background-color: gray;
        }
      #submit  {
        clear: both;
        margin-top: 20px;
        border-top: solid 1px #333;
       
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
      
      <div>
     
      <div class="form" id="tableau">
        <table border="1" cellspacing="0" cellpadding="5" id="table">
         
            <tr>
              <th>Produit</th>
              <th>Quantité</th>
              <th>Prix Unitaire (€)</th>
              <th>Total (€)</th>
            </tr>
         
         
           
            <tr id="totalHT">
              <td colspan="3" class="center">Total HT</td>
              
              <td><input type="text" name="totalHT" id="totalHT1">&nbsp;€</td>
            </tr> 
            <tr>
              <td colspan="3" class="center">TVA (20%)</td>
              
              <td><input type="text" name="tva" id="tva">&nbsp;€</td>
            </tr>
          
        
            <tr>
              <td colspan="3" class="center">Total TTC</td>
              
              <td><input type="text" name="montantTTC" id="montantTTC">&nbsp;€</td>
            </tr>
         
        </table>
        </div>
        <div id="button">
          <input type="button" id="plus" value="+" />
          <input type="button" id="moins" value="-" />
        </div>
         </div>
        
      <div class="center" id="submit">
        
        <input type="submit" value="Valider" id="btn" />
        <br /><br />
      </div>
      
    </form>
 
  <script>
           
            
    function crationLigne(name, id, tr, ligneTotalHT, type, typezone) {
      
      let td = document.createElement("td");
      let input = document.createElement("input");
      input.setAttribute("type", typezone );
      input.setAttribute("name", name);
      input.setAttribute("id", id );
      
      if(type!= undefined) {
        input.setAttribute("class", type);
        
        if (type == "element") input.addEventListener("change", produit, false)
        }
      
      td.appendChild(input);
      tr.appendChild(td);
      
      let parent = ligneTotalHT.parentNode;
      parent.insertBefore(tr, ligneTotalHT);
     
      
    }

    function ajoutLigne() {
      let lignes = document.getElementsByClassName("ligne");
      let numeroLigne = lignes.length + 1;
      let ligneTotalHT = document.getElementById("totalHT");
      let tr = document.createElement("tr");
      tr.setAttribute("class", "ligne");
      tr.setAttribute("id", "ligne" + numeroLigne);
      crationLigne("produit", "produit"+ numeroLigne, tr, ligneTotalHT, "text");
      crationLigne("quantite", "quantite"+numeroLigne, tr, ligneTotalHT, "element", "text");
      crationLigne("prix", "prix"+numeroLigne, tr, ligneTotalHT, "element", "text");
      crationLigne("total", "total"+numeroLigne, tr, ligneTotalHT, "sousTotal", "text");
      crationLigne("sup", "sup"+numeroLigne, tr, ligneTotalHT, "sup", "checkbox");
     
    }
    
    function supprimerLigne() {
      let sups = document.getElementsByClassName("sup");
      let j = 0;
      let lignes = Array();
      for (let i = 0; i < sups.length; i++) {
        if(sups[i].checked){
          let id = sups[i].getAttribute("id");
          let position = id.substring(id.length - 1, id.length);
          lignes[j] = "ligne" + position;
          j++;
        }
      }
      
      for (let i = 0; i < lignes.length; i++) {
        let ligne = document.getElementById(lignes[i]);
        let parent = ligne.parentNode;
        parent.removeChild(ligne);
      }
      calculTotal() 
    
    }
    
    function produit() {
      
        let  num = this.getAttribute("id");
      
        let position = num.substring(num.length - 1, num.length);
       
        let quantite = document.getElementById("quantite" + position).value;
        let prix = document.getElementById("prix" + position).value;
        let total = document.getElementById("total" + position);
        let sousTotal = parseFloat(quantite) * parseFloat(prix);
        
        if ((sousTotal === "") || (isNaN(sousTotal))) {
            total.value = "Une case est vide";
        }
        else if (sousTotal < 0) {
            total.value = "Valeur négative";
        } 
        
        else {
        total.value = sousTotal;
        calculTotal()
        }
      }
        
    function calculTotal() {
       let montantTotal = 0
        let sousTotals = document.getElementsByClassName("sousTotal");
        for (let i = 0; i < sousTotals.length; i++) {
          if (!isNaN(parseFloat(sousTotals[i].value))) montantTotal = montantTotal + parseFloat(sousTotals[i].value);   
        }
        let totalHT = document.getElementById("totalHT1");
         totalHT.value = montantTotal;
         
        let tva = document.getElementById("tva");
         tva.value = montantTotal * 0.2;
        
        let montantTTC = document.getElementById("montantTTC");
          montantTTC.value = montantTotal + parseFloat(tva.value);
    }
        
        
           
    let elements = document.getElementsByClassName("element");
    for (let i = 0; i < elements.length; i++) {
        elements[i].addEventListener("change", produit, false);
    }
    
    let plus = document.getElementById("plus");
    plus.addEventListener("click", ajoutLigne, false);
    
    let moins = document.getElementById("moins");
    moins.addEventListener("click", supprimerLigne, false);
    
    
    
  </script>
</html>

"""

print(html)
        