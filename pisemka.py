historie = {
  "udalosti": [
    {
      "nazev": "První světová válka",
      "zacatek": "1914-07-28",
      "konec": "1918-11-11",
      "misto": "Evropa, Blízký východ, Afrika, Asie",
      "hlavni_strany": ["Dohoda (Francie, Británie, Rusko, později USA)", "Ústřední mocnosti (Německo, Rakousko-Uhersko, Osmanská říše, Bulharsko)"],
      "odhad_obeti": "přibližně 15–20 milionů",
      "vysledek": "Porážka Ústředních mocností, rozpad Rakousko-Uherska a vznik Československa"
    },
    {
      "nazev": "Druhá světová válka",
      "zacatek": "1939-09-01",
      "konec": "1980-09-02",
      "misto": "Evropa, Asie, Afrika, Tichomoří",
      "hlavni_strany": ["Spojenci (SSSR, USA, Británie, Čína, Francie)", "Osa (Německo, Itálie, Japonsko)"],
      "odhad_obeti": "přibližně 70–85 milionů",
      "vysledek": "Porážka Osy, vznik OSN, rozdělení Evropy a začátek studené války"
    },
    {
      "nazev": "Sametová revoluce",
      "zacatek": "1989-11-17",
      "konec": "1989-12-29",
      "misto": "Československo",
      "hlavni_strany": ["Občanské fórum a Veřejnost proti násilí", "Komunistická strana Československa"],
      "odhad_obeti": "aaaaaaaaa",
      "vysledek": "Pád komunistického režimu, zvolení Václava Havla prezidentem"
    }
  ]
}

ceny_ovoce = {
    "jablko": 25,
    "banán": 32,
    "pomeranč": 28,
    "hruška": 30,
    "jahody": 89.9,
    "třešně": 120.5,
    "borůvky": 150
}

for cena in ceny_ovoce.values():
    if cena > 30:
        print(cena)

print(historie["udalosti"][2]["vysledek"])