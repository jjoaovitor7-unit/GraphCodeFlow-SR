import pandas as pd
dfTAGS = pd.read_csv("tags.csv", usecols=["movieId", "tag"], sep=",")
# print(dfTAGS)

dfMOVIES = pd.read_csv("movies.csv", usecols=["movieId", "title"], sep=",")
# print(dfMOVIES)

print("Sistema de Recomendação")

username = input("Nome de Usuário:")
idFilme  = int(input("ID do Filme:"))

tags               = []
filmes             = []
filmesRecomendados = []

filme = dfTAGS["movieId"].values
tag   = dfTAGS["tag"].values

for i in range(len(dfTAGS["movieId"].values)):
    if idFilme == filme[i]:
        if tag[i] not in tags:
            tags.append(tag[i].lower())

for j in range(len(dfTAGS["tag"].values)):
    if tag[j].lower() in tags:
        if filme[j] not in filmes:
            filmes.append(filme[j])

filmesId       = dfMOVIES["movieId"].values
filmesNome     = dfMOVIES["title"].values
filmeEscolhido = ""

for k in range(len(dfMOVIES["title"].values)):
    if filmesId[k] == idFilme:
        filmeEscolhido = filmesNome[k]

for l in range(len(filmes)):
    for m in range(len(dfMOVIES["title"].values)):
        if filmes[l] == filmesId[m]:
            filmesRecomendados.append(filmesNome[m])

print("\nUsuário:", username
      + "\nFilme:", "[" + str(idFilme) + "]", filmeEscolhido)
print("Tags:", str(tags).strip("[]")
      + "\nFilmes Recomendados:\n",
      str(filmes)+"\n"+
      str(filmesRecomendados).strip("[]"))
