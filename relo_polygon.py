import math
import numpy as np
def regular_polygon_Relo_from_module(n=3, center=np.array([0, 0]), r=1, N=100):    
    """возвращает матрицу, каждая строка которой содержит координаты точек, описывающих границу правильного многоугольника Рело
    
    Arguments:
    
    n: количество вершин правильного многоугольника Рело; является нечетным целым числом большим  2 ; стандартное значение n = 3;
    center: массив координат центра правильного многоугольника Рело; стандартнное значение center = np.array([0, 0]);
    r: ширина правильного многоугольника Рело; является положительным числом; стандартное значение r = 1;
    N: количество точек для описания одной стороны правильного многоугольника Рело; является натуральным числом; стандартное значение N = 100.
    
    Returns: ([[x1, y1], [x2, y2], ...])
    """
    
    assert n > 2, 'number of vertices n should be positive and greater than 2'
    assert n % 2, 'number of vertices n should be odd'
    assert r > 0, 'radius r should be positive'
    assert N > 0, 'number of points N should be positive'
    
    alpha = 2 * math.pi / n
    beta = alpha / 2
    
    l = r * math.sqrt(2 * (1 - math.cos(beta)))
    R = l / (2 * math.sin(math.pi / n))
    
    t = np.arange(0, 2 * np.pi, 2 * np.pi / n)
    vertices = center + R * np.transpose([np.cos(t), np.sin(t)])
    
    angle = np.linspace(-beta / 2, beta / 2, N)
    
    sides = [vertices[i] + r * np.transpose([np.cos(angle + np.pi + i * alpha), np.sin(angle + np.pi + i * alpha)]) for i in range(n)]
    sides = np.concatenate(sides)
    
    return sides