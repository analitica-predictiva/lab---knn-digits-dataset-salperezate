"""
Clasificación usando k-NN - Digits Dataset
-----------------------------------------------------------------------------------------

En este laboratio se construirá un clasificador usando k-NN para el dataset de digitos.

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets


def pregunta_01():
    """
    Complete el código presentado a continuación.
    """

    # Cargue el dataset digits
    #digits = ____.____()
    digits = datasets.load_digits()

    # Imprima los nombres de la variable target del dataset
    #print(____.____)
    print(digits.target_names)

    # Imprima las dimensinoes de matriz de datos
    #print(____.____.____)
    print(digits.data.shape)

    # Imprima las dimensiones del vector de salida
    #print(____.____.____)
    print(digits.target.shape)


def pregunta_02():
    """
    Complete el código presentado a continuación.
    """
    # Importe KNeighborsClassifier de sklearn.neighbors
    from sklearn.neighbors import KNeighborsClassifier

    # Importe train_test_split de sklearn.model_selection
    from sklearn.model_selection import train_test_split

    # Cargue el dataset digits
    #digits = ____.____()
    digits = datasets.load_digits()

    # Cree los vectors de características y de salida
    #X = ____.____
    #y = ____.____
    X = digits.data
    y = digits.target

    # Divida los datos de entrenamiento y prueba. Los conjuntos de datos están
    # estratificados. La semilla del generador de números aleatorios es 42.
    # El tamaño del test es del 20%
    # X_train, X_test, y_train, y_test = ____(
    #     ____, ____, test_size=____, random_state=____, stratify=____
    # )
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Cree un clasificador con siete vecinos
    #knn = ____
    knn = KNeighborsClassifier(n_neighbors=7)

    # Entrene el clasificador
    #____
    knn.fit(X_train, y_train)

    # Imprima la precisión (score) del clasificador en el conjunto de datos de prueba
    #print(round(knn.score(____, ____), 4))
    print(round(knn.score(X_test, y_test), 4))


def pregunta_03():
    """
    Complete el código presentado a continuación.
    """

    # Importe KNeighborsClassifier de sklearn.neighbors
    from sklearn.neighbors import KNeighborsClassifier

    # Importe train_test_split de sklearn.model_selection
    from sklearn.model_selection import train_test_split

    # Cargue el dataset digits
    #digits = ____.____()
    digits = datasets.load_digits()

    # Cree los vectors de características y de salida
    #X = ____.____
    #y = ____.____
    X = digits.data
    y = digits.target

    # Divida los datos de entrenamiento y prueba. Los conjuntos de datos están
    # estratificados. La semilla del generador de números aleatorios es 42.
    # X_train, X_test, y_train, y_test = ____(
    #     ____, ____, test_size=____, random_state=____, stratify=____
    # )
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Inicialice los arreglos para almacenar la precisión para las muestras de
    # entrenamiento y de prueba
    neighbors = np.arange(1, 9)
    train_accuracy = np.empty(len(neighbors))
    test_accuracy = np.empty(len(neighbors))

    # Se itera sobre diferentes valores de vecinos
    for i, k in enumerate(neighbors):
        # Cree un clasificador con k vecinos
        #knn = ____
        knn = KNeighborsClassifier(n_neighbors=k)

        # Entrene el clasificador con los datos de entrenamiento
        #____
        knn.fit(X_train, y_train)

        # Calcule la precisión para el conjunto de datos de entrenamiento
        #train_accuracy[i] = knn.score(____, ____)
        train_accuracy[i] = knn.score(X_train, y_train)

        # Calcule la precisión para el conjunto de datos de prueba
        #test_accuracy[i] = knn.score(____, ____)
        test_accuracy[i] = knn.score(X_test, y_test)

    # Almacenamiento de los resultados como un dataframe
    df = pd.DataFrame(
        {
            "k": neighbors,
            "train_accuracy": train_accuracy,
            "test_accuracy": test_accuracy,
        }
    )

    return df
