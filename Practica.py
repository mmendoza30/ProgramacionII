import pandas as pd
import numpy as np
import math

df = pd.read_csv("diabetes.csv")
print("Dimensión de la tabla:", df.shape)

# Función que retorna el menor de tres valores
def maximo(A, B, C):
    return max(A, B, C)
