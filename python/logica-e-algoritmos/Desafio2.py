import numpy as np

imagem = np.array([
    [200, 180, 160, 140, 120, 100],
    [ 90,  80,  70,  60,  50,  40],
    [255, 240, 210, 190, 170, 150],
    [ 30,  20,  10,   5,   2,   0]
], dtype=np.uint8)

brilho_geral = np.mean(imagem)

brilho_linhas = np.mean(imagem, axis=1)
brilho_colunas = np.mean(imagem, axis=0)

indice_linha_escura = np.argmin(brilho_linhas)

imagem_binaria = imagem.copy()

imagem_binaria[imagem >= 128] = 255
imagem_binaria[imagem < 128] = 0

print(f"Brilho médio geral: {brilho_geral:.2f}")
print(f"Médias por linha: {brilho_linhas}")
print(f"Médias por coluna: {brilho_colunas}")
print(f"A linha mais escura é a de índice {indice_linha_escura} (Média: {brilho_linhas[indice_linha_escura]:.2f})")

print("\nImagem Binária (Preto e Branco):")
print(imagem_binaria)