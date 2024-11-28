import cv2

# Função para redimensionar a imagem para um tamanho fixo de largura de 700 pixels, mantendo a proporção
def resize_image(img_array, new_width=700):
    height, width, _ = img_array.shape
    new_height = int((new_width / width) * height)  # Calcula a nova altura mantendo a proporção
    resized_image = cv2.resize(img_array, (new_width, new_height))
    return resized_image, (width / new_width), (height / new_height)

# Carrega a imagem
image_path = '../assets/inputs/image01.jpeg'
image = cv2.imread(image_path)

# Verifica se a imagem foi carregada corretamente
if image is None:
    print("Erro ao carregar a imagem.")
    exit()

# Redimensiona a imagem para um tamanho fixo de largura de 700 pixels, mantendo a proporção
resized_image, scale_x, scale_y = resize_image(image, 700)

# Lista para armazenar as coordenadas das vagas
vagas = []

print("Selecione os retângulos das vagas. Pressione Enter após selecionar cada retângulo. Pressione Esc para finalizar.")

# Define a janela como ajustável
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

while True:
    # Permite ao usuário selecionar a ROI (Região de Interesse)
    roi = cv2.selectROI("Image", resized_image, fromCenter=False, showCrosshair=True)
        
    # Se a ROI não foi selecionada, o usuário pressionou ESC para sair
    if roi == (0, 0, 0, 0):
        break
    
    x, y, w, h = roi
    vagas.append((int(x * scale_x), int(y * scale_y), int(w * scale_x), int(h * scale_y)))  # Coordenadas originais

    # Desenha o retângulo na imagem para visualização imediata
    cv2.rectangle(resized_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow('Image', resized_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# Verifica se foram capturadas coordenadas
if len(vagas) > 0:
    # Imprime as coordenadas processadas
    for i, (x, y, w, h) in enumerate(vagas):
        print(f"Vaga {i + 1}: (x={x}, y={y}, w={w}, h={h})")

    # Mostra a imagem com os retângulos das vagas desenhados
    for (x, y, w, h) in vagas:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Vagas de Estacionamento', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nenhuma coordenada capturada.")
