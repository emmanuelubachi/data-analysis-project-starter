import csv

# Open the CSV file
with open("wrong_text.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    replacements = {}

    # Iterate over each row in the CSV
    for row in reader:
        # Skip empty rows
        if len(row) == 0:
            continue

        # Get the incorrect and correct texts
        incorrect_text = row[0]
        correct_text = row[1]

        # Add the mapping to the replacements dictionary
        replacements[incorrect_text] = correct_text

# Print the resulting dictionary
print(replacements)

replacements = {
    "Carbonate de cobalt 25% au moins de Co": "Carbonate de cobalt ≤  25% Co",
    "Cobalt autrement presenté 90%Co ou moins": "Cobalt autrement presenté ≤ 90% Co ",
    "Cobalt autrement presente, cement de cuivre 25.81 de Co": "Cobalt autrement presenté, cement de cuivre 25-81 % Co",
    "Cobalt cathodes a 99,3%": "Cobalt cathodes à 99,3%",
    "Cobalt en granulés teneur supérieure ou égale 99,3% de cobalt": "Cobalt en granulés teneur ≥ à 99,3% Co",
    "Cobalt Separ,Magn. Et Scorie Lectrom 55%Co o\nu moins": "Cobalt Separ,Magn. et Scorie Lectrom ≤ 55%Co",
    "Cobalt séparateur magnétique d'une teneur de 55 à 60% en cobalt": "Cobalt séparateur magnétique d'une teneur de 55 à 60% Co",
    "Cobalt séparateur magnétique d'une teneur de 61 à 65% en cobalt": "Cobalt séparateur magnétique d'une teneur de 61 à 65% Co",
    "Concentres de Cuivre d'une teneur de 31 a 35%": "Concentrés de Cuivre d'une teneur de 31 à 35%",
    "Concentres de Cuivre d'une teneur de 36 a 40%": "Concentrés de Cuivre d'une teneur de 36 à 40%",
    "Concentres mixtes Cobalt-Cuivre 10-15% de Cu et 4% ou moins de Co": "Concentrés mixtes Cobalt-Cuivre 10-15% Cu et ≤ 4% Co",
    "Concentres mixtes Cobalt-Cuivre 16-20% de Cu et 4% ou moins de Co": "Concentrés mixtes Cobalt-Cuivre 16-20% Cu et ≤ 4% Co",
    "Concentres mixtes Cobalt-Cuivre 21-25% de Cu et 4% ou moins de Co": "Concentrés mixtes Cobalt-Cuivre 21-25% Cu et ≤ 4% Co",
    "Concentres mixtes de Cobalt-Cuivre de 10-15%\nCu et 8-10%Co": "Concentrés mixtes de Cobalt-Cuivre de 10-15%\nCu et 8-10% Co",
    "Concentres mixtes de Cobalt-Cuivre de 21-25%Cu et 8-10%Co": "Concentrés mixtes de Cobalt-Cuivre de 21-25% Cu et 8-10% Co",
    "Concentres mixtes de Cobalt-Cuivre de 26-30%Cu et 5-7%Co": "Concentrés mixtes de Cobalt-Cuivre de 26-30% Cu et 5-7% Co",
    "concentrés simple de cuivre d'une teneur de 21 à 25% en cuivre": "concentrés simple de cuivre d'une teneur de 21 à 25% Cu",
    "concentrés simple de cuivre d'une teneur de 26 à 35% en cuivre": "concentrés simple de cuivre d'une teneur de 26 à 35% Cu",
    "concentrés simple de cuivre d'une teneur de 45% en cuivre ou plus": "Concentrés simple de cuivre d'une teneur ≥ 45% Cu",
    "Concentres simples de Cobalt d'une teneur de  7 à 10% de cobalt": "Concentrés simples de Cobalt d'une teneur de 7 à 10% Co",
    "Concentres simples de Cobalt d'une teneur de  7% de Co ou moins": "Concentrés simples de Cobalt d'une teneur ≤ 7% Co",
    "Concentres simples de Cobalt d'une teneur de 11 a 13% de Co": "Concentrés simples de Cobalt d'une teneur de 11 à 13% Co",
    "Concentres simples de Cobalt d'une teneur de 11 à 15% de Cobalt": "Concentrés simples de Cobalt d'une teneur de 11 à 15% Co",
    "Concentres simples de Cobalt d'une teneur de 14 a 16% de Co": "Concentrés simples de Cobalt d'une teneur de 14 à 16% Co",
    "Concentres simples de Cobalt d'une teneur de 16 à 20% de Cobalt": "Concentres simples de Cobalt d'une teneur de 16 à 20% Co",
    "Concentres simples de Cobalt d'une teneur de 8 a 10% de Co": "Concentrés simples de Cobalt d'une teneur de 8 à 10% de Co",
    "Concentres simples de Cobalt d'une teneur de\n 11 a 13% de Co": "Concentrés simples de Cobalt d'une teneur de 11 à 13% Co",
    "Concentres simples de Cobalt d'une teneur de\n 14 a 16% de Co": "Concentrés simples de Cobalt d'une teneur de 14 à 16%  Co",
    "Concentres simples de Cobalt d'une teneur de\n 8 a 10% de Co": "Concentrés simples de Cobalt d'une teneur de 8 à 10% Co",
    "Cuivre autrement presenté 90%Cu ou moins": "Cuivre autrement presenté ≤ 90% Cu",
    "Cuivre Blister ou cuivre noir DE 76-80%de Cu": "Cuivre Blister ou cuivre noir de 76-80% Cu",
    "Cuivre non affiné, cuivre blister ou cuivre noir d'une teneur =< 75% de cuivre": "Cuivre non affiné, cuivre blister ou cuivre noir d'une teneur ≤ 75% Cu",
    "Hydroxyde de cobalt de 25% Co ou moins": "Hydroxyde de cobalt ≤ 25% Co",
    "Hydroxyde de cobalt de plus de 45% Co": "Hydroxyde de cobalt > 45% Co",
    "Hydroxydes de cobalt d'une teneur inférieure ou égale à 25% en cobalt": "Hydroxydes de cobalt d'une teneur ≤  à 25% Co",
    "hydroxydes de cobalt d'une teneur supérieure ou égale à 41% en cobalt": "hydroxydes de cobalt d'une teneur ≥ à 41% Co",
    "Minerais COBALTICUPRIFERES 10-15% Co": "Minerais cobalticuprifères 10-15% Co",
}
