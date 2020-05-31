import pandas as pd
DATAFRAME = pd.read_csv("tags.csv", usecols=["movieId", "tag"], sep=",")
print(DATAFRAME)

DATAFRAME_MOVIES = pd.read_csv("movies.csv", usecols=["movieId", "title"], sep=",")
print(DATAFRAME_MOVIES)

username = input("\nNome de Usuário:")
idFilme = int(input("ID do Filme:"))

tags   = []
filmes = []

filme = DATAFRAME["movieId"].values
tag   = DATAFRAME["tag"].values

for i in range(len(DATAFRAME["movieId"].values)):
    if idFilme == filme[i]:
        if tag[i] not in tags:
            tags.append(tag[i].lower())

for j in range(len(DATAFRAME["tag"].values)):
    if tag[j].lower() in tags:
        if filme[j] not in filmes:
            filmes.append(filme[j])

filmesId       = DATAFRAME_MOVIES["movieId"].values
filmesNome     = DATAFRAME_MOVIES["title"].values
filmeEscolhido = ""

filmesRecomendados = []

for k in range(len(DATAFRAME_MOVIES["title"].values)):
    if filmesId[k] == idFilme:
        filmeEscolhido = filmesNome[k]

for l in range(len(filmes)):
    for m in range(len(DATAFRAME_MOVIES["title"].values)):
        if filmes[l] == filmesId[m]:
            filmesRecomendados.append(filmesNome[m])

print("\nUsuário:", username
      + "\nFilme:", "[" + str(idFilme) + "]", filmeEscolhido)
print("Tags:", str(tags).strip("[]")
      + "\nFilmes Recomendados:\n",
      str(filmes)+"\n"+
      str(filmesRecomendados).strip("[]"))
