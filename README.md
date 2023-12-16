# proyecto_12_SR_CJ
Proyecto 12 Sergio Rehbein y Camila Jauregui


# Quick Start
Proyecto 12 Sergio Rehbein y Camila Jauregui 
Exploración y Comparación de Técnicas de Regresión Simbólica

Se mostrará como se deben descargar y ejecutar los librerías que nos proporcionan en los papers para posteriormente poder aplicar los benchmark de comparación

## Pre- Instalación

Para cada código se recomienda tener un entorno virtual diferente, dado que pueden utilizar diferentes versiones de algunas librerías, como ejemplo:

    conda create -n nombre-ev


Ahora se procede a mostrar
## Installation EQL

    pip install EQL-NN

## Installation EQL + Encoders

Descomprimir archivo DeepSymRegTorch-main.zip

    pip install -r requirements.txt

## Installation AI_Feynman

Se recomienda encarecidamente configurar un entorno virtual nuevo escribiendo.

    virtualenv -p python3 feyn
    source feyn/bin/activate
    
Primero instala numpy con pip install numpy.
El paquete 'aifeynman' está disponible en PyPI y se puede instalar con pip install aifeynman, de la siguiente forma:

    pip install aifeynman

Luego se puede hacer uso importando

    import aifeynman


## Installation Phy-SO

Para instalar el paquete, se recomienda primero crear un entorno virtual con conda.

    conda create -n PhySO python=3.8

y activar:

    conda activate PhySO

Posteriormente descargar directamente desde github:

    git clone https://github.com/WassimTenachi/PhySO

Instalamos lo esencial:

    conda install --file requirements.txt

## BenchMark Nguyen

Dado que algunos modelos como el EQL y el AI_Feynman se debe crear de previamente de forma sintetica los diferentes funciones del Bencharmak Nguyen, se deja el código en formato .py para la generación de estos archivos y se debe usar de la siguiente forma (genera 1000 datos para utilizar):

    python3 nguyen_benchmark.py

# Ejecución de diferentes modelos y métricas.

Para cada modelo se dará el ejemplo con Nguyen 1, se debe iterar de la misma forma para las otras funciones del bencharmark.

## Ejecución EQL

    import tensorflow as tf
    import numpy as np
    import matplotlib.pyplot as plt
    
    from EQL.model import EQL
    EQLmodel = EQL(num_layers = 1)
    EQLmodel.build_and_compile_model()
    
    
    # Suponiendo que 'data.txt' es tu archivo y que está delimitado por espacios
    data = np.loadtxt('Nguyen1.txt')
    
    # Separar los datos en x e y
    x = data[:, 0]  # Esto asume que x es la primera columna
    y = data[:, 1]  # Esto asume que y es la segunda columna
    
    EQLmodel.fit(x, y, 0.1,t0 = 6000, t1 = 2000, t2 = 2000, atol = 0.001)
    EQLmodel.summary()

