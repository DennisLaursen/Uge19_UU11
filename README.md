## Uge19_UU11
Restantfunktion

## Introduktion
Da jeg ikke har erfaring nok med kodning til at kunne lave machinelearning opgaven, har jeg i stedet valgt en mere simpel Python opgave, hvor jeg vha. Pandas laver en restantopfølgningsfunktion til en forening.
Jeg har brugt Uge 18 (Undervisningsuge 10) til at sætte mig ind i helt basal kodning, C samt Python, ved hjælp af CS50 introduktionsvideoer til programmering. Og den efterfølgende uge (uge 19) er jeg så gået i gang med selve programmeringen.

Jeg har tager udgangspunkt i restantprocessen på mit gamle arbejde, Dansk Vegetarisk Forening, hvor jeg var ansvarlig for restantprocessen, og har opsat et arbejdsflow for denne. Jeg har derfor brugt bruge min dokumentation/arbejdsbeskrivelse fra mit gamle arbejde, og i høj grad taget udgangspunkt i dette.
Jeg har genereret testdata vha. Mockaroo og ChatGPT (navn, mail, betalingskanal, betalingsfrekvens og restantdato).

## Sådan fungerer koden
Koden er delt op i flere filer i mappen 'processing', og hver del fungerer som følger, og afspejler hver sin delproces af restantforløbet.

# Indledende trin
Her har brugeren (den person, der tænkes at bruge koden) eksporteret en restantliste fra CRM-systemet. Det forudsættes, at det pågældende CRM-system har en automatiseret funktion, der fanger restanter - altså folk der er bagud med deres kontingentbetaling til foreningen - og eksporterer dette til en Excel- eller .csv-fil.
Det indledende trin bearbejder dokumentet på følgende vis, og gemmer resultatet i en ny fil (den gamle fil beholdes og ændres ikke):
- Datoer konverteres
- Datostempel (seenest screenet) tilføjes som dokumentation
- Gamle restanter, der er mere end 3 måneder gamle, slettes. Årsagen til dette er at vi gerne vil sikre, at folk, der misser flere måneds- eller kvartalsbetalinger, atter fanges i restantforløbet. Eksempel: Karen Karensen misser sin kontingentbetaling 01-02-2025, betaler 08-02-2025, men misser så atter sin kontingentbetaling 01-05-2025, hvorfor vi skal rykke Karen Karensen igen. Hvis Karen stadig står på restantlisten, vil systemet fortolke hende som en igangværende/løst restantsag, men skal altså behandles på ny, og skal ind i flowet på ny, som en ny sag.
- Dubletter fjernes på baggrund af nøgleværdi (medlemsnummer). Dette gør vi også, så brugeren nemt kan kopiere det nyeste data ind fra CRM-systemet, og koden selv sørger for dublethåndteringen. Dette skyldes, at vi følger op på restanter efter 14 dage, og udmelder dem, der endnu ikke har fornyet. Hvis Ole Olesen kommer i restance den 01-03-2025, og vi kører koden igen den 08-03-2025, så er Ole Olesen stadig en igangværende restantsag (fordi han først skal rykkes den 15-03-2025), og hans dublet skal derfor slettes, så vi ikke behandler ham som en ny restantsag.
- Slutteligt gemmes dokumentet som en ny .csv-fil, 'restantliste_screenet.csv'

Brugeren skal gemme det færdige dokument 'restantliste_screenet' til to ting:
1) Det næste trin i restantprocessen
2) Når restantprocessen skal køres på ny i fremtiden

# Trin 1: send mail
Her er det meningen, at koden løber restanterne fra 'restantliste_screenet' listen igennem, og sender dem en E-mail på baggrund af deres betalingskanal. Jeg er i skrivende stund (d. 9/5-25) ikke blevet færdig med denne del af opgaven, men planen med dette trin er som følger:
- Koden skal sende en E-mail til den enkelte restant, med udgangspunkt i vedkommendes betalingskanal (betalingskort, MobilePay, Betalingsservice osv.), og bruge vedkommendes oplysninger i fletfelter. Derudover skal koden også indsætte dét fornyelseslink, der er i arket (og som brugeren skal hente fra CRM-systemet), i den E-mail der sendes til medlemmet i restance.
- Vi skal sikre os, at mailen dels sendes i henhold til gældende GDPR-regler (f.eks. sikre, at mailen ikke indeholder CPR-nummer); dels at vi gemmer en kopi af den sendte mail.
- Når E-mailen er sendt, skal koden lave en ny kolonne i .csv-filen, der hedder "mail sendt", og skrive dags dato.
- I den "virkelige verden", jf. 'Restanter arbejdsbeskrivelse' dokumentet, er der mange forskellige flow koden skal tage højde for, da forskellige betalingskanaler kan give forskellige "fejl". F.eks. kan folk afvise deres MobilePay betaling i MobilePay app'en, og denne restantsag skal håndteres på en anden måde, end hvis et Dankort er udløbet. Girokort, der ikke kommer frem med posten, skal håndteres på en 3. måde; Betalingsservice aftaler der er lukket på en 4. måde, og så fremdeles. I denne første version af programmeringsopgaven vil jeg altså "lege" at vi har fungerende integrationer til CRM-systemet, der f.eks. kan hente det korrekte, unikke fornyelseslink på det enkelte medlem; og jeg har derfor genereret en masse testdata-links, som jeg vil arbejde videre med i stedet.

# Trin 2: Opfølgning og udmelding
I dette trin, 14 dage efter 1. trin er lavet, skal koden ind og tjekke om de enkelte medlemmer har fornyet deres betalingsaftale. Hvis betalingsaftalen er fornyet, skal den næste betaling rykkes til så hurtig som muligt; og hvis betalingsaftalen ikke er fornyet, skal medlemmet udmeldes, og have sendt en udmeldelsesmail.
Denne del af koden er jeg i skrivende stund (d. 9/5-25) ikke nået til. Og da meget af dette ligeledes kræver integrationer til et CRM-system, vil jeg ligeledes generere testdata at arbejde med, f.eks. en falsk 0603-fil fra Betalingsservice.

# requirements.txt filen
Jeg har skrevet 'pip freeze' i terminalen, og kopieret teksten ind i requirements.txt filen. Når koden skal køres på en ny computer, skal brugeren skrive 'pip install -r requirements.txt' i terminalen.

## Forudsætninger
- Restantlisten skal gemmes som en UTF-8 .csv fil, for at Æ, Ø og Å vises korrekt

## Begrænsninger/videreudviklinger
- En begrænsning i denne kode, er at jeg ikke har et testmiljø i et CRM-system, jeg kan integerere til. Derfor kræver denne kode manuel bearbejdning i form af at en medarbejder manuelt skal trække seneste restanter fra foreningens CRM-system, for at kunne bruge koden. Hvis man kunne integrere koden/forbinde koden vha. en API til et CRM-system, kunne man automatisere koden yderligere. Derudover har mit fokus været at få koden til at bearbejde de "lokale" filer, og en API-integration til et CRM-system er derfor en oplagt videreudvikling. En sådan videreudvikling vil også have den fordel, at man via REST eller JSON-kommandoer kan skrive en bemærkning i et browserbaseret CRM-system, så medarbejdere/frivillige, der bruger CRM-systemet, kan se hvad "computeren" har lavet på det pågældende medlem.
- Hvis jeg skal videreudvikle denne kode, skal jeg også gøre mig følgende reflektioner angående betalingskanaler: I og med at hver betalingskanal har forskellige "flows" og systemer, skal de, i en mere avanceret udgave af denne kode, håndteres på forskellig vis. Eksempelvis har PBS/Betalingsservice en række 0603-kørsler på bestemte tidspunkter på dagen, samt deadlines på 8. sidste bankdag i måneden for ændringer i PBS-betalingsaftaler. Og betalinger med MasterCard går igennem en platform der hedder Bambora, mens VISA/Dankort går direkte igennem Nets. Hvis alle betalinger er samlet i ét CRM- eller opkrævningsssystem, vil dét gøre programmering meget lettere. Men det betyder stadig, at der er en række forbehold, koden skal tage højde for. Eksempelvis kan restantkoden først tjekke om en PBS-aftale er genaktiveret, når en betaling er kommet ind i den nye måned (men hvis koden kan få adgang til 0603-filerne, så vil vi her kunne tjekke samt "løse" restanten, så snart 0603-kørslerne giver os besked om at den pågældende aftale er genaktiveret); men en Dankort-betalingsaftale er mere fleksibel, og kan sættes til opkrævning dagen efter. **Den største udfordring med denne kode bliver at følge op på restanter, samt rykke betalingen til at den paser**.

# Firmaer, der har med betalinger at gøre:
- Nets
- Bambora/Worldline
- QuickPay
- MasterCard
- MobilePay
- PBS/Betalingsservice
- CRM-systemer
- Opkrævningssystemer (som Online Fundraising)
Det er bare de firmaer, jeg kan huske på rygradden. Der er også et par stykker, jeg ikke kan huske navnene på. Så der er en del kanaler at tage højde for, hvis man skulle lave en komplet kode til opfølgning af restanter.

## Links og eksterne henvisninger
- Word-dokumentet 'Restanter arbejdsbeskrivelse': Den procesbeskrivelse, jeg har udviklet på mit gamle arbejde (Dansk Vegetarisk Forening), og som er udgangspunktet for denne kodning
- CS50: https://cs50.harvard.edu/x/2025/
- Mockaroo: https://www.mockaroo.com/
- ChatGPT hjælp: https://chatgpt.com/share/6818b817-f640-8005-ba1a-b5bc5bad3813