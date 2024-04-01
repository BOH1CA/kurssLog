# kurssLog

## Autor : Tanel Soidla

## Kirjeldus
- **Programeerimis Keel:** Python
kurssLog.py on script mis: 
1. laeb alla xml faili kindlalt URL-ilt
2. kontrollib kas failis olev NOK kurss on kõrgem kui 9.00€
3. Juhul kui kurss on kõrgem avab või loob faili "kurss.txt" kaustas "C:\kurss"
4. Kontrollib viimast logitud kuupäeva
5. Juhul kui tegu on järgmise päevaga siis kirjutatakse uus rida sõnumiga 'dd/mm/yy on kurss üle 8.00€'

## Kasutamine

### Variant 1:

1. Lae alla kirja manuses olev fail nimega kurssLog.rar
2. Paki lahti fail nimega "kurssLog.rar"
3. Ava fail kurssLog.exe topelt klick-iga või parem klick + ava
4. Kui kõik eeldused on täidetud uuendab või loob script faili "kurss.txt" kaustas "C:\kurss"
* Windows võib märkida kurssLog.exe ohtlikuks failiks kui see juhtub tuleb rakendus karantiinist vabastada

### Variant 2:

#### Eeldused kasutamiseks
Python3 peab olema arvutisse paigaldatud
    Python libary 'requests' peab olema paigaldatud

1. Lae alla kirja manuses olev fail "kurssLogpy.rar"
2. Paki lahti fail nimega "kurssLogpy.rar"
3. Ava konsool ja liigu kausta kuhu sai lahti pakitud "kurssLogpy.rar"
4. Sisesta konsooli käsk: "python kurssLog.py" ja vajuta Enter
5. Kui kõik eeldused on täidetud uuendab või loob script faili "kurss.txt" kaustas "C:\kurss"