# Smartgrid
Algoritmen & Heuristieken, 
Lente 2023

Steeds meer huizen maken tegenwoordig gebruik van zonnepanelen of andere gedecentraliseerde manieren van energie-opwekking. Dit scheelt de bewoners geld, en vaak zijn dit groene manieren van energie opwekken, positief voor de bewoner en de samenleving. Overbodige energie kan worden verkocht aan een energieleverancier zodat deze ergens anders in het net gebruikt kan worden. Hier lopen we echter tegen problemen aan, want ons huidige energiegrid is niet gebouwd voor tweezijdige energie verkoop.

Dit project heeft als doel het optimaliseren van een energienetwerk met behulp van batterijen. Het onderzoekt algoritmen en heuristieken om de plaatsing en werking van batterijen in het energienetwerk te optimaliseren, zodat pieken en dalen in energieproductie kunnen worden opgevangen en energie kan worden verkocht aan energieleveranciers.

&nbsp;

#### Algoritmen:

Voor dit project maken wij gebruik van vier verschillende projecten. 

Random: 
Het random algoritme selecteert willekeurig een huis en voegt deze toe aan een batterij als deze voldoende capaciteit heeft om het huis aan te nemen.
Het vormt onze baseline en wordt onderandere gebruikt door het Hill Climber algoritme.

Greedy: 
Het Greedy algoritme koppelt huizen aan batterijen met de kortste afstand tot elkaar als er voldoende capaciteit is. 
Wanneer een batterij 'verzadigd' is gaat het algoritme naar de volgende batterij en koppelt daar huizen aan. Als er overgebleven huizen zijn, ontkoppelt het huis eerst een willekeurig huis en koppelt vervolgens, indien mogelijk, een nieuw huis. 

Hill Climber: 
Het Hill climber algoritme neemt een uitkomst van een random algoritme en verwisselt steeds 3 huizen van de ene batterij met 3 huizen van een andere batterij. 
Dit blijf hij doen totdat het na 2500 iteraties geen betere uitkomst meer kan vinden. 

K-means: 

&nbsp;

#### Installatie-instructies:

Zorg ervoor dat Python 3 is geïnstalleerd op je systeem.
Clone het project van de git-repository naar je lokale machine.
Ga naar de projectdirectory.
Installeer de benodigde bibliotheken met het volgende commando:

"pip3 install -r requirements.txt"

&nbsp;

#### Gebruiksinstructies:

Voer het hoofdscript uit om het energienetwerk te optimaliseren:
python main.py

Volg de instructies op het scherm om de gewenste parameters in te stellen, zoals de gewenste wijk, algoritme, en aantal runs.
Het script zal het optimalisatieproces uitvoeren en de resultaten weergeven, inclusief de geoptimaliseerde plaatsing van batterijen en de totale kosten van het energienetwerk.
De CSV-bestanden met de kosten per run zijn te vinden onder Huizen&batterijen/experimenten en de grafieken en griduitbeelding zijn te vinden onder figuren

&nbsp;

#### Auteurs:

- Michael Lin
- Teun Binkhorst
- Thom Hopstaken
- Bijdragers: Momenteel zijn er geen bijdragers aan dit project.

&nbsp;

#### Veelgestelde vragen (FAQ):

Wat is de doelstelling van dit project?
Dit project heeft als doel het optimaliseren van een energienetwerk met behulp van batterijen om pieken en dalen in energieproductie op te kunnen vangen.

Welke optimalisatie-algoritmen worden gebruikt?
Het project onderzoekt verschillende algoritmen en heuristieken, zoals een random algoritme, een greedy algoritme, een hill-climber algoritme en een k-means algoritme.

Kan ik bijdragen aan dit project?
Nee.