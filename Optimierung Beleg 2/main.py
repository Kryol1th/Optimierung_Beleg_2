import numpy as np                            # Paket für numerische Operationen
from numpy import ndarray

# Startvektor:
v_1: ndarray = np.array([0.5, 0.5])
v_0: ndarray = np.array([100.0, 100.0])

# Nebenbedingungen
NB = np.array([0.25, 1.0])

# Schrittweite
SW = np.array([0.01, 0.005, 0.0025, 0.001])

#Vektor zur Visualisierung
X_mem = np.array([0.5, 0.5])
print(X_mem)
# Abbruchbedingung
def found_optimum(v_0, v_1):
    if abs(zielfunktion(v_0) - zielfunktion(v_1)) < 0.01:
        return True
    else:
        return False

#Funktion zur Berechnung des Gradienten
def getGradient (v_1):
    grd: ndarray = np.array([0, 0])
    grd[0] = 100 * v_1[1] + 1 / v_1[1] - 1 / (v_1[0] ** 2 * v_1[1])
    grd[1] = 100 * v_1[0] - (v_1[0]/(v_1[1])**2) - 1 / (v_1[0] * v_1[1] ** 2)
    return grd

#Funktion zur Berechnung des Aktuellen Wertes der Zielfunktion
def zielfunktion(v_1):
    z = 100 * v_1[0] * v_1[1] + (v_1[0]/v_1[1]) + 1 / (v_1[0] * v_1[1])
    return z

#Iterative Schleife, bis Minimal Wert der Zielfunktion gefunden wurde
i = 1
gradient = getGradient(v_1)
while not found_optimum(v_0, v_1):
    v_0 = np.copy(v_1)
#Berechnung des neuen Punktes
    v_1[0] = v_0[0] - SW[i] * gradient[0]
    v_1[1] = v_0[1] - SW[i] * gradient[1]

    X_mem = np.vstack((X_mem, v_1))
    """
    print("-----------------")
    print(gradient)
    print(v_1[0], v_1[1])
    print(zielfunktion(v_1))
    print(zielfunktion(v_0))
    print(i)
    """
#Anpasung des Gradientens und der Schrittweite
    if zielfunktion(v_1) < zielfunktion(v_0):
        gradient = getGradient(v_1)
        if i < 3:
            i = i + 1
    if zielfunktion(v_1) >= zielfunktion(v_0):
        if i >= 0:
            i = i - 1

#Einhalten der Nebenbedingungen
    if v_1[0] <= NB[0] or v_1[0] >= NB[1] or v_1[1] <= NB[0] or v_1[1] >= NB[1]:
        if i >= 0:
            i = i - 1


#Ergebniss Ausgabe
print("---------------------------------------")
print("LÖSUNG:")
print("Iterationsablauf:", X_mem)
print("X1 =", v_1[0])  # WARUM IST DER WERT GERUNDET?????
print("X2 =", v_1[1])
print("Minimaler Wert der Zielfunktion:", zielfunktion(v_1))
print("---------------------------------------")

# Erstellung Plot
x_coordinates = [M_min, M_max]
y_coordinates = [alpha, alpha]
plt.plot(x_coordinates, y_coordinates, color="navy")
# Ausgabe Plot
#plt.show()
plt.title("Genetic")
plt.savefig("plot_genetic.png")