import numpy as np
notas = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [5.0, 4.5, 6.0, 5.5],
    [9.0, 9.5, 8.5, 10.0],
    [3.0, 4.0, 5.0, 4.5],
    [8.0, 7.5, 9.0, 8.5]
])

medias_alunos = np.mean(notas, axis=1)
indice_maior_media = np.argmax(medias_alunos)

medias_provas = np.mean(notas, axis=0)
desvios_provas = np.std(notas, axis=0)
notas_normalizadas = (notas - medias_provas) / desvios_provas

mask_aprovados = medias_alunos >= 6.0
notas_aprovados = notas[mask_aprovados]

print("Médias de cada aluno:")
print(medias_alunos)
print(f"\nAluno com a maior média: Índice {indice_maior_media} (Média: {medias_alunos[indice_maior_media]:.2f})")

print("\nMatriz de notas normalizadas (por coluna):")
print(notas_normalizadas)

print("\nNotas originais dos alunos aprovados (Média >= 6.0):")
print(notas_aprovados)