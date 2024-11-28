from ultralytics import YOLO
import cv2
import plotarVagas

# Função para fazer a predição dos carros
def predict_image(img_array):
    return model(img_array)

# Função para desenhar as predições dos carros na imagem
def plot_predictions(img_array, predictions):
    # Mapeia os IDs das classes para os nomes das classes personalizadas e desenha as caixas na imagem
    for result in predictions:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy.tolist()[0])  # Converte para lista e mapeia para inteiros
            confidence = box.conf.item()

            if confidence > THRESHHOLD_DETECTION:
                # Desenha a caixa de contorno e o rótulo na imagem
                cv2.rectangle(img_array, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img_array, f"{CLASS_NAME} {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return img_array

# Função para redimensionar a imagem para um tamanho fixo de largura de 800 pixels, mantendo a proporção
def resize_image(img_array, new_width=700):
    height, width, _ = img_array.shape
    new_height = int((new_width / width) * height)  # Calcula a nova altura mantendo a proporção
    resized_image = cv2.resize(img_array, (new_width, new_height))
    return resized_image

THRESHHOLD_DETECTION = 0.5
CLASS_NAME = "Carro"
model = YOLO("../assets/models/yolov8s.pt")

# Carregar a imagem
frame = cv2.imread("../assets/inputs/image03.jpeg")

# Fazer a predição
predictions = predict_image(frame)

# Plotar as predições na imagem
frame_ploted = plot_predictions(frame, predictions)

# Assegure-se de que a função plot_vagas receba os argumentos corretos
coordinate_vagas = plotarVagas.coordinate_vagas()
car_coordinates = []
for result in predictions:
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy.tolist()[0])
        car_coordinates.append((x1, y1, x2 - x1, y2 - y1))

# Agora, chamar a função do arquivo plotarVagas para desenhar as vagas
frame_with_vagas = plotarVagas.plot_vagas(frame_ploted, coordinate_vagas, car_coordinates)

# Redimensionar a imagem para 800 pixels de largura
frame_resized = resize_image(frame_with_vagas, 700)

# Exibir a imagem com as predições e as vagas redimensionadas
cv2.imshow("Previsoes com Estacionamento com Vagas", frame_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
