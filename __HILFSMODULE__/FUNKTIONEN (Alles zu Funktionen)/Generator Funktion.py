# Definiere Generator Funktion
def quadrieren(n):
    """
    Generatoren sind eine einfache und mächtige Möglichkeit, Iteratoren zu kreieren.
    Äußerlich gleichen sie Funktionen. Syntaktisch betrachtet gibt es nur einen Unterschied: Statt der return-Anweisung
    findet man in einem Generator eine oder mehrere yield-Anweisungen.

    Alles, was man mit Generatoren machen kann, lässt sich auch mit klassenbasierten Iteratoren machen. Aber der ent-
    scheidende Vorteil der Generatoren liegt darin, dass die Methoden __iter__() und next() automatisch erzeugt werden.

    Was ist ein Iterator? Iteratoren sind Objekte, über die mir einer for-Schleife iteriert werden kann. Wir können
    auch sagen, dass ein Iterator ein Objekt ist, das Daten Element für Element zurückgibt. Das heißt, sie machen keine
    Arbeit, bis wir ausdrücklich nach ihrem nächsten Objekt fragen bzw. dieses anfordern. Sie arbeiten nach einem
    Prinzip, das in der Informatik als Lazy-Evaluation (deutsch: bequeme oder faule Auswertung) bekannt ist.
    """
    i = 1
    while i <= n:
        q = i * i
        yield q
        i += 1


# Schleife: Werte abrufen
# for x in quadrieren(10):
#     print(x, end=" ")

# Funktionsaufruf
werte = quadrieren(5)

# Bei jedem next ein schritt weiter
print(next(werte))
print(next(werte))
print(next(werte))
