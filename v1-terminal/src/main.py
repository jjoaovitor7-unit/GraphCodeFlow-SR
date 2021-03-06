#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    import pandas as pd
    dfTAGS = pd.read_csv("v1-terminal/data/tags.csv", usecols=["movieId", "tag"], sep=",")
    # print(dfTAGS)

    dfMOVIES = pd.read_csv("v1-terminal/data/movies.csv", usecols=["movieId", "title"], sep=",")
    # print(dfMOVIES)

    print("Sistema de Recomendação")

    username = input("Nome de Usuário:")
  #!/usr/bin/env python3
# -*- coding: utf-8 -*-  idFilme = int(input("ID do Filme:"))

    tags = []
    filmes = []
    filmesRecomendados = []

    filmesCol = dfTAGS["movieId"].values
    tagsCol = dfTAGS["tag"].values

    for i in range(len(filmesCol)):
        if idFilme == filmesCol[i]:
            if tagsCol[i] not in tags:
                tags.append(tagsCol[i].lower())

    for j in range(len(tagsCol)):
        if tagsCol[j].lower() in tags:
            if filmesCol[j] not in filmes:
                filmes.append(filmesCol[j])

    filmesId = dfMOVIES["movieId"].values
    filmesNome = dfMOVIES["title"].values
    filmeEscolhido = ""

    for k in range(len(filmesId)):
        if filmesId[k] == idFilme:
            filmeEscolhido = filmesNome[k]

    for l in range(len(filmes)):
        for m in range(len(filmesNome)):
            if filmes[l] == filmesId[m]:
                filmesRecomendados.append(filmesNome[m])

    print("\nUsuário:", username
        + "\nFilme:", "[" + str(idFilme) + "]", filmeEscolhido)

    print("Tags:")
    for n in range(len(tags)):
        print(tags[n], end=" ")

    print("\nFilmes Recomendados:")
    for o in range(len(filmes)):
        print("[" + str(filmes[o]) + "] " + filmesRecomendados[o])


if __name__ == "__main__":
    main()
