import numpy as np                          # Paket für numerische Operationen
import matplotlib.pyplot as plt             # Paket fürs grafische Darstellen
from matplotlib import rc
from gooey import Gooey, GooeyParser        # grafische Benutzeroberfläche (GUI)

"""
Optimierung Übung 2 mit grafischer Benutzeroberfläche
"""

# Anpassung Schriftart & -größe für Plots
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

plt.rcParams['figure.figsize'] = [5, 3]     # Anpassung der Plot-Größe

# grafische Benutzeroberfläche
@Gooey()
def GUI():
    parser = GooeyParser(description='Parametereingabe gradientenbasierte Optimierung')

    parser.add_argument('-Startpunkt-x1', '-my-arg', widget='IntegerField',
                        gooey_options={
                            'min': 2,
                            'max': 10,
                            'increment': 1})

    parser.add_argument('-Startpunkt-x2', '-my-arg2', widget='IntegerField',
                        gooey_options={
                            'min': 2,
                            'max': 10,
                            'increment': 1})

    parser.add_argument('-e', '--modus', nargs='+',
                        choices=['mitNorm', 'ohneNorm', 'umRdgsGrad'])

    parser.add_argument('-Iterationen', widget='Slider', gooey_options={
        'min': 10,
        'max': 100,
        'increment': 10
    })

    parser.add_argument(
        '-f', '--plot',
        metavar='Auswertungsabbildung anzeigen',
        action='store_true',
        #help='show plot'
    )

    args = parser.parse_args()
    return args

# Eingaben der Oberfläche
args = GUI()


# Definition der Optimierungsaufgabe
def zf(xVec, l1=1414.2, l2=1153.5):
    """
    Definiton Zielfunktion
    
    :param xVec: Vektor der Eingangsparameter x
    :param l1: Länge Stab 1
    :param l2: Länge Stab 2
    :return: Zielfunktion z = f(x)
    """
    
    z = xVec[0]*l1 + xVec[1]*l2
    return z


def gradZF(xVec, l1=1414.2, l2=1153.5):
    """
    Definition Gradient der Zielfunktion
    
    :param xVec: Vektor der Eingangsparameter x
    :param l1: Länge Stab 1
    :param l2: Länge Stab 2
    :return: Gradient der Zielfunktion 
    """
    
    return np.asanyarray([l1, l2])


def nebenbedinungen(xVec):
    """
    Definition der Nebenbedingungen
    
    :param xVec: Vektor der Eingangsparameter x
    :return: Werte der Nebenbedingungen
    """
    
    g1 = 0.5163 - xVec[0]
    g2 = 0.7324 - xVec[1]
    g3 = (1 / xVec[0]) + (1.6414 / xVec[1]) - 2.6527

    return np.asanyarray([g1, g2, g3])


def gradientDerNB(xVec):
    """
    Gradient der Nebenbedingungen
    
    :param xVec: Vektor der Eingangsparameter x
    :return: Gradienten aller Nebenbedingungen
    """

    gradG1 = np.asanyarray([-1, 0])
    gradG2 = np.asanyarray([0, -1])
    gradG3 = np.asanyarray([-(1/xVec[0]**2), -(1.6414/xVec[1]**2)])

    return [gradG1, gradG2, gradG3]


def ausgabe(i, x):
    """
    Definition der Standardausgaabe des Iterationsfortschritts

    :param i: Iterationsschritt
    :param x: Eingabevektor
    :return: None
    """

    print('------ITERATION %i ------' %i)
    print('Entwurfsvektor: %2.4f %2.4f' %(x[0], x[1])+
    ' -- Zielfunktionswert: %f' %zf(x))
    print('Nebenbedingungen: %f %f %f' %(nebenbedinungen(x)[0], nebenbedinungen(x)[1], nebenbedinungen(x)[2]))


# Parameter der Optimierung (teilweise abgerufen aus GUI)
x = [int(args.Startpunkt_x1), int(args.Startpunkt_x2)]      # x = [3, 2] Startpunkt
lambdaVal = 5*10**-5          # Lambda
iterationen = int(args.Iterationen)                 # iterationen = 10       # Vorgegebene Anzahl der Iterationen
modus = str(args.modus[0])
# modus = 'umRdgsGrad'   # 'mitNorm' - mit Gradientennormalisierung
# 'ohneNorm' - ohne Gradientennormalisierung
# 'umRdgsGrad' - mit Umrandungsgradient


def run_optimierung(x, lambdaVal, iterationen, modus, args):
    xSpeicher = []  # Speicher-Vektor der Eingangsgrößen
    zSpeicher = []  # Speicher-Vektor der Zielfunktion
    # Optimierung
    for i in range(iterationen):
        if modus == 'mitNorm':
            # Suchrichtung mit Gradientennormalisierung
            y = -(gradZF(x)/np.linalg.norm(gradZF(x)))

        elif modus == 'ohneNorm':
            # Suchrichtung ohne Gradientennormalisierung
            y = -gradZF(x)

        elif modus == 'umRdgsGrad':
            # Suchrichtung mit Nebenbedingungen
            y = -gradZF(x)
            nb = nebenbedinungen(x)
            for idxNB, gradNB in enumerate(gradientDerNB(x)):
                if nb[idxNB] > 0:
                    y += -gradNB*(np.linalg.norm(gradZF(x))/np.linalg.norm(gradNB))
        else:
            raise ValueError("Falscher Auswertungsmodus")

        x = x+lambdaVal*y   # neuer Entwurfspunkt
        ausgabe(i, x)
        xSpeicher.append(x)
        zSpeicher.append(zf(x))

    # Plot der Zielfunktion und des Eingabevektors über Iterationsschritte
    if args.plot is True:
        # Erstellung der Grafik
        fig, ax = plt.subplots(1, 2)
        # plot des input Vektors über Iterationsschritte
        xArray = np.asanyarray(xSpeicher)
        ax[0].plot(xArray[:, 0], xArray[:, 1], 'r.-')
        # Überschrift und Achsenbeschriftungen
        ax[0].set_title('Entwurfsraum')
        ax[0].set_xlabel(r'$x_1\ [\textrm{cm}^2]$')
        ax[0].set_ylabel(r'$x_2\ [\textrm{cm}^2]$')
        # plot der Zielfunktion über Iterationsschritte
        ax[1].plot(zSpeicher, 'b.-')
        # Überschrift und Achsenbeschriftungen
        ax[1].set_title('Ergebnisraum')
        ax[1].set_xlabel('Iterationen')
        ax[1].set_ylabel(r'$z(x_1,\,x_2)\ [\textrm{cm}^3]$')
        ax[1].set_xlim(0, iterationen)
        # erstelle Raster
        for axi in ax:
            axi.grid()
        # positioniere subplots
        fig.tight_layout()
        fig.subplots_adjust(wspace=0.65)
        plt.show()


run_optimierung(x, lambdaVal, iterationen, modus, args)
