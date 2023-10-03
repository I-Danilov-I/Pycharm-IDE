# Definiere zwei Listen
hauptstadt = ["Paris", "Rom", "Berlin"]
land = ["Frankreich", "Italien", "Deutschland"]

# Verbinde die beiden Listen und ausgeben
land_hauptstadt = list(zip(hauptstadt, land))
print("Datentyp:", type(land_hauptstadt), "\n" + "Liste:", list(land_hauptstadt))

for i in land_hauptstadt:
    print(i, type(i))

