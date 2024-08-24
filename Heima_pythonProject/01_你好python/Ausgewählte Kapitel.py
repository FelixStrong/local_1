import matplotlib.pyplot as plt
import numpy as np

# Quasistatische Steifigkeitskennlinie für ein Elastomerlager mit Anschlägen

# Erstellen der Verformung x-Achse (in mm)
deformation = np.linspace(-10, 10, 400)

# Definition der Steifigkeitskennlinie mit Anschlägen
def stiffness_curve(x):
    if x < -5:
        return -100
    elif x > 5:
        return 100
    else:
        return 20 * x

stiffness = [stiffness_curve(x) for x in deformation]

# Zeichnen des Diagramms
plt.figure(figsize=(8, 6))
plt.plot(deformation, stiffness, label='Steifigkeitskennlinie', color='blue')

# Diagrammachsen beschriften
plt.xlabel('Verformung $x$ (mm)')
plt.ylabel('Kraft $F$ (N)')

# Charakteristische Bereiche kennzeichnen
plt.axvline(x=-5, color='red', linestyle='--', label='Anschlag negativ')
plt.axvline(x=5, color='green', linestyle='--', label='Anschlag positiv')

# Bereiche benennen
plt.text(-7, -80, 'Negativer Anschlag', color='red', verticalalignment='center')
plt.text(7, 80, 'Positiver Anschlag', color='green', verticalalignment='center')
plt.text(0, 50, 'Elastischer Bereich', color='black', verticalalignment='center')

plt.title('Quasistatische Steifigkeitskennlinie eines Elastomerlagers')
plt.legend()
plt.grid(True)
plt.show()
