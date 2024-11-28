import cv2
import numpy as np

# Função para desenhar as vagas na imagem
def plot_vagas(img_array, coordinate_vagas, car_coordinates):
    for space_rect in coordinate_vagas:
        # Verifica se algum carro está dentro da vaga
        is_occupied = any(is_car_in_parking_space(car_rect, space_rect) for car_rect in car_coordinates)

        # Define a cor do retângulo: vermelho se ocupado, verde se livre
        color = (0, 0, 255) if is_occupied else (0, 255, 0)

        (x, y, w, h) = space_rect
        cv2.rectangle(img_array, (x, y), (x + w, y + h), color, 2)

    return img_array

# Função para verificar se um retângulo A está dentro de um retângulo B
def is_car_in_parking_space(car_rect, space_rect):
    (xA, yA, wA, hA) = car_rect
    (xB, yB, wB, hB) = space_rect

    # Verifica se o carro está dentro da vaga
    if (xA >= xB and yA >= yB and (xA + wA) <= (xB + wB) and (yA + hA) <= (yB + hB)):
        return True
    return False

def coordinate_vagas():
    vagasCoordinates = [
        (41, 439, 571, 324),
        (889, 958, 345, 569),
        (34, 777, 566, 356),
        # (218, 428, 156, 229),
        # (377, 428, 142, 237)
    ]
    return vagasCoordinates
