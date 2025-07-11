#coding:utf-8
import cgi

print("Content-Type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>Facture</title>
    
    </head>
    <body>
        <h1>COMMENT AUTOMATISER L AJOUT ET LA SUPRESSION D UNE LIGNE DE TABLEAU</h1>
        <div>
        <div> 
                        <label>Numero:</label>&nbsp;
                        <input type="text" name="numero" id="numero" />&nbsp;&nbsp;
                        <label>Date:</label>&nbsp;
                        <input type="date" name="date" id="date" />&nbsp;&nbsp;
                        <label>Client:</label>&nbsp;
                        <select name="client" id="client">
                            <option value="client1">Client 1</option>
                            <option value="client2">Client 2</option>
                            <option value="client3">Client 3</option>
                            </select>
        </div>
        <div id="tableau">
            <table   border="1" id="table">
               
                    <tr>
                        <th>Produit</th>
                        <th>Quantite</th>
                        <th>Prix</th>
                        <th>Total</th>
                      
                        
                    </tr>
                
                <tbody id="tbody">
                    <!-- Les lignes seront ajoutées ici -->
                    <tr class="ligne" id="ligne1">
                        <td><input  name="produit" id="produit1", type="text"/></td>
                        <td><input  name="quantite" class="element" id="quantite1", type="text"/></td>
                        <td><input type="text" name="prix" class="element" id="prix1" /></td>
                        <td><input type="text" name="total" class="soustotal" id="soustotal1" readonly /></td>
                        <td><input type="checkbox" name="check" id="check1" /></td>
                    </tr>
                 
                   
                </tbody>
                <tfoot>
                    <tr>
                        <td colspan="3" style="text-align: left;">Total HT:</td>
                        <td><input type="text" name="totalHT" id="totalHT" readonly /></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td colspan="3" style="text-align: left;">TVA (20%):</td>
                        <td><input type="text" name="tva" id="tva" readonly /></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td colspan="3" style="text-align: left;">Total TTC:</td>
                        <td><input type="text" name="totalTTC" id="totalTTC" readonly /></td>
                        <td></td>
                    </tr>
                </tfoot>
               
            </table>
        </div>
        <br/>
        <div>
            <button type="button" id="addRow" >Ajouter une ligne</button> &nbsp;&nbsp;&nbsp;
            <button type="button" id="removeRow">Supprimer une ligne</button>
        </div>
        
        
        
        <script>
        
        function supprimerLigne() {
              let checks =  document.getElementsByName("check");
              let j = 0;
              let lignes = Array();
              for(let i = 0; i < checks.length; i++) {
                  if(checks[i].checked) {
                      let id = checks[i].getAttribute("id");
                      let numero = id.substring(id.length - 1, id.length);
                      lignes[j]= "ligne"+numero;
                      j++;
                     
                    }
                
                }
                for(let i = 0; i < lignes.length; i++) {
                    let ligne = document.getElementById(lignes[i]);
                    let parent = ligne.parentNode;
                    parent.removeChild(ligne);
                }
                calculerTotal();
            }
         
        
         function produit() {
                let id = this.getAttribute("id");
                let numero = id.substring(id.length - 1, id.length);
            
                let quantite = document.getElementById("quantite"+numero).value;
                let prix = document.getElementById("prix"+numero).value;
                let soustotal = document.getElementById("soustotal"+numero);
                
                let prixTotal = parseFloat(quantite) * parseFloat(prix);
                
                if(!isNaN(prixTotal)) {
                    soustotal.value = prixTotal.toFixed(2);
                }
                calculerTotal();    
            }
            
            function calculerTotal() {
                let soustotals = document.getElementsByClassName("soustotal");
                let montantHT = 0;
                
                for(let i = 0; i < soustotals.length; i++){
                    if (!isNaN(parseFloat(soustotals[i].value))) montantHT += parseFloat(soustotals[i].value);
                }
                let totalHT = document.getElementById("totalHT");
                totalHT.value = montantHT.toFixed(2);
                let tva = document.getElementById("tva");
                tva.value = (montantHT * 0.2).toFixed(2);
                let totalTTC = document.getElementById("totalTTC");
                totalTTC.value = (montantHT * 1.2).toFixed(2);
            }
                    
            
            let elements = document.getElementsByClassName("element");
            
                for(let i = 0; i < elements.length; i++){
                    elements[i].addEventListener("change", produit, false);
                }
        
        
        
         function creationLignr(tr, tbody, name, id, type, type2) {
                
                let td = document.createElement("td");
                let input = document.createElement("input");
                input.setAttribute("type", type);
                input.setAttribute("name", name);
                input.setAttribute("id", id);
                if(type2!= undefined) {
                    input.setAttribute("class", type2);
                    input.addEventListener("change", produit, false);}
                
                td.appendChild(input);
                tr.appendChild(td);
                tbody.appendChild(tr);
         }
                      
         function ajoutLigne() {
                let count = document.getElementById("tbody").getElementsByTagName("tr").length;
                let numero = count + 1;
                
                let tbody = document.getElementById("tbody");
                let tr = document.createElement("tr");
                tr.setAttribute("class", "ligne");
                tr.setAttribute("id", "ligne"+numero);
                creationLignr(tr, tbody, "produuit", "produit"+numero, "text" );
                creationLignr(tr, tbody, "quantite", "quantite"+numero, "text", "element" );
                creationLignr(tr, tbody, "prix", "prix"+numero, "text", "element");
                creationLignr(tr, tbody, "soustotal", "soustotal"+numero, "text", "soustotal");
                creationLignr(tr, tbody, "check", "check"+numero, "checkbox");
                
              
               
                
            }
                
        document.getElementById("addRow").addEventListener("click", ajoutLigne, false);
        document.getElementById("removeRow").addEventListener("click", supprimerLigne, false);
                
                
       
        </script>
        
    </body>
</html>
"""
print(html)