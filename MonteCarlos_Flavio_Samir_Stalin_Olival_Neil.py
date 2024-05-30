import numpy as np
import matplotlib.pyplot as plt

def simular_puntos(num_puntos):
    dentro_circulo = 0
    puntos_x_dentro = []
    puntos_y_dentro = []
    puntos_x_fuera = []
    puntos_y_fuera = []

    for _ in range(num_puntos):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        distancia = np.sqrt(x**2 + y**2)
        
        if distancia <= 1:
            dentro_circulo += 1
            puntos_x_dentro.append(x)
            puntos_y_dentro.append(y)
        else:
            puntos_x_fuera.append(x)
            puntos_y_fuera.append(y)
    
    pi_estimado = 4 * dentro_circulo / num_puntos
    return pi_estimado, puntos_x_dentro, puntos_y_dentro, puntos_x_fuera, puntos_y_fuera

def graficar_resultados(num_puntos):
    pi_estimado, puntos_x_dentro, puntos_y_dentro, puntos_x_fuera, puntos_y_fuera = simular_puntos(num_puntos)
    
    plt.figure(figsize=(8, 8))
    plt.scatter(puntos_x_dentro, puntos_y_dentro, color='blue', label='Dentro del círculo')
    plt.scatter(puntos_x_fuera, puntos_y_fuera, color='red', label='Fuera del círculo')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Estimación de Pi usando Monte Carlo: {pi_estimado:.5f}')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.grid(True)
    circle = plt.Circle((0, 0), 1, color='black', fill=False)
    plt.gca().add_patch(circle)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()


num_puntos = 10000
graficar_resultados(num_puntos)

