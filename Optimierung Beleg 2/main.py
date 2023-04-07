
import numpy as np                            # Paket für numerische Operationen
# import matplotlib.pyplot as plt             # Paket fürs grafische Darstellen
# from matplotlib import rc
# from gooey import Gooey, GooeyParser        # grafische Benutzeroberfläche (GUI)

# Startvektor:
v_0 = np.array([0.5, 0.5])
v_1 = np.array([100, 100])

# Nebenbedingungen
NB = np.array([0.25, 1])

# Schrittweite
SW = np.array([0.01, 0.005, 0.0025, 0.001])


# Abbruchbedingung

def found_optimum(v_0, v_1):
    if abs(v_0.zielfunktion() - v_1.zielfunktion()) < 0.01:
        return True
    else:
        return False

def gradient (v):
    gradient = 1
    return gradient

i = 0
gradient = v_0.gradient()

while not found_optimum(v_0, v_1):
    v_temp = v_1+1
    print(v_temp.x1, v_temp.x2)
    v_1.x1 = v_0.x1 - SW[1] * gradient[0]
    v_1.x2 = v_0.x2 - SW[1] * gradient[1]
    print(v_temp.x1, v_temp.x2)

    print(v_1.x1, v_1.x2)
    print(v_0.x1, v_0.x2)

    if v_0.zielfunktion() < v_1.zielfunktion():
        gradient = v_0.gradient()
        if i < 3:
            i = i + 1
    if v_0.zielfunktion() > v_1.zielfunktion():
        if i > 0:
            i = i - 1
    if v_1.x1 < NB[0] or v_1.x1 > NB[1] or v_1.x2 < NB[0] or v_1.x2 > NB[1]:
        if i > 0:
            i = i - 1
    print(v_temp.x1, v_temp.x2)
    v_0 = v_temp
    print(v_0.x1, v_0.x2)
    print(v_temp.x1, v_temp.x2)

    print(v_0.zielfunktion())
    print(v_1.zielfunktion())
    print(v_0.zielfunktion() - v_1.zielfunktion())
    print('---------------------------')

