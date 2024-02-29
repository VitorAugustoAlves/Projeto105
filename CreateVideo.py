import os
import cv2

path = "Projeto105-main/images"
images =[]
imagens = os.listdir(path)

for arquivo in imagens:
    img1, ext = os.path.splitext(arquivo)
    img2, ext = os.path.splitext(arquivo)
    img3, ext = os.path.splitext(arquivo)
    img4, ext = os.path.splitext(arquivo)
    img5, ext = os.path.splitext(arquivo)
    img6, ext = os.path.splitext(arquivo)
    img7, ext = os.path.splitext(arquivo)
    img8, ext = os.path.splitext(arquivo)
    img9, ext = os.path.splitext(arquivo)
    img10, ext = os.path.splitext(arquivo)
if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
    file_name = path+'/'+arquivo
    print(file_name)
    images.append(file_name)
else:
    print('{arquivo} tem uma extenção não suportada.')

count = len(images)

print("Lista de imagens:")
print(images)
print(f"Número total de imagens: {count}")

if count > 0:
    frame = cv2.imread(images[0])
    height, width, channels = frame.shape
    print(f"Largura: {width} pixels")
    print(f"Altura: {height} pixels")
    print(f"Número de Canais: {channels}")
    size = (width, height)
    print(f"Dimensões da imagem: {size}")
    out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
    print("Vídeo 'Project.avi' criado com sucesso.")
    for i in range(count):
        image_path = images[i]
        img = cv2.imread(image_path)
        out.write(img)
    
    out.release()
    print("Vídeo criado com sucesso.")
    print("O vídeo 'Project.avi' está completo.")

else:
    print("Não há imagens na lista.")

print("Tamanho da imagem:")
print(size)