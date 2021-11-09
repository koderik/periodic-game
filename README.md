# Projektspecifikation Periodiska systemet
## Datastrukturer
### Filer
#### "avikt.txt"
Innehåller alla atomer och deras atomvikt
#### "period_coord.txt"
Innehåller x, y koordinater för det periodiska systemet och vilken atom som ligger på varje plats
### Atom
#### Instansvariabler:
- String name: Det förkortade namnet på atomen
- String weight: Vikten på atomen i enheten u
- Int x: Atomens x-koordinat i det periodiska systemet
- Int y: Atomens y-koordinat i det periodiska systemet
#### Metoder:
- Konstruktor: Skapar en instans av objektet med ursprungsvariablerna name och weight, båda sätts som tom sträng som default.
- set_xy: Ansätter atomens x och y koordinater
- set_number: Ansätter atomens atomnummer
### Atom_list
#### Instansvariabler:
- list a_list: Lista med atomer
#### Metoder:
- Konstruktor: Skapar en tom lista, tar in två strängar med namn på textfiler och fyller listan med atomer från de två filerna
- iter: Gör objektet itererbar genom att hänvisa till den interna listan.
- len: Ger objektet längd genom att hänvisa till den inre listan
- getitem: Ger objektet index genom att hänvisa till den indre listans index
- get_name: söker linjärt igeom den inre listan för att hitta en atom som har det sökta namnet
- get_number: söker linjärt igeom den inre listan för att hitta en atom som har det sökta atomnumret
- get_weight: söker linjärt igeom den inre listan för att hitta en atom som har den sökta atomvikten
- get_xy: söker linjärt igeom den inre listan för att hitta en atom som har de sökta x,y koordinaterna
- switch: byter plats på två element i den interna listan på platsen index och index+1
- fill_list: fyller listan med atomer och vikter utifrån en fil
- set_coords: Tilldelar atomer i listan x,y koordinater utifrån en fil
- set_numbers: sorterar listan (utifrån atomvikt) och tilldelar atomnummer, byter plats på några atomer för att göra systemet vetenskapligt korrekt

## Objekt
### MenyFrame
Grafisk ruta som visar alternativ för saker att göra i programmet
### ListFrame
Grafisk ruta som visar alla atomer, deras nummer namn och vikt
### QuestionFrame
Grafisk ruta som visar olika frågor att öva på, man kan gissa nummer namn och vikt.
### GameFrame
Spel där man ska fylla i ett periodiskt system genom att klicka i rutor 
## Algoritmer
### Frågealgoritmer
#### Atomnummer och Atomnamn
Programmet tar fram en valfri atom ur listan med random.choice() och sparar atomens namn, vikt och nummer. Sedan beroende på om frågan är ang. "name" eller "number" så sätts frågan till att innehålla atomnummer respektive atomnamn och det rätta svaret sparas. Sedan anropas en funktion när användaren skickar in sitt svar och då jämförs texten i textfältet med det rätta svaret och om man svarat rätt så meddelas det och spelet börjar om med en ny fråga. Man har tre försök.
#### Atomvikt
Programmet tar fram en valfri atom ur listan med random.choice() och sparar atomvikt som svar och atomnamn som fråga, sedan skickas den med  i en metod som tar fram två till slumpade atomer att visa vikten på. Tre knappar skapas med atomvikter som knapptext varav endast en är rätt svar.
#### Klicka på rätt atom
En atom väljs ur en lista med möjliga atomer och atomens namn sätts som fråga. Varje knapp i rutnätet har respektive atoms namn som medförande tag. Motsvarar den tryckta knappens tag namnet på den efterfrågade atomen har användaren svarat rätt och atomen tas ut från möjliga atomer att välja mellan och går vidare med en ny atom. Dessutom visas atomens namn på knappen och den byter färg till grönt.
### Grafikalgoritmer
#### Rita tabell
Programmet ritar en tabell med en bestämd maxhöjd (35 celler) för att ge rutan rimlig höjd och mer bredd. En nestlad for-loop med höjden som range printar tre bredvidliggande labels med atomens nummer, namn och vikt. Den nestlade loopen loopas tre gånger med x-värde som förflyttas åt höger.
#### Rita periodisk tabell
Programmet har sedan innan sparat en lista på formen "x, y, name" för alla atomer som skall visas i det periodiska systemet där 0 innebär att rutan inte innehåller en atom och därmed skall lämnas tom. När atomlistan skapas så läses denna fil igenom och varje atom tilldelas ett x och y värde. Två i varandra nestlade loopar går igenom alla möjliga x,y värden i det periodiska systemet och om den hittar en atom som matchar x,y så skapas en knapp med atomnamnet som tag och ??? som knapptext (tills användaren gissat rätt på den knappen) på den koordinaten i ett rutnät.

## Funktioner
Programmet har inga funktioner utan all funktionalitet sker genom interna klassmetoder.