import pandas as pd
DATAFRAME = pd.read_csv("tags.csv", usecols=["movieId", "tag"], sep=",")
print(DATAFRAME)

DATAFRAME_MOVIES = pd.read_csv("movies.csv", usecols=["movieId", "title"], sep=",")
print(DATAFRAME_MOVIES)

username = input("\nNome de Usuário:")
id_filme = int(input("ID do Filme:"))

tags   = []
filmes = []

filme = DATAFRAME["movieId"].values
tag   = DATAFRAME["tag"].values

for i in range(len(DATAFRAME["movieId"].values)):
    if id_filme == filme[i]:
        if tag[i] not in tags:
            tags.append(tag[i].lower())

for j in range(len(DATAFRAME["tag"].values)):
    if tag[j].lower() in tags:
        if filme[j] not in filmes:
            filmes.append(filme[j])

filmes_id       = DATAFRAME_MOVIES["movieId"]
filmes_nome     = DATAFRAME_MOVIES["title"]
filme_escolhido = ""

filmes_recomendados = []

for k in range(len(DATAFRAME_MOVIES["title"].values)):
    if filmes_id[k] == id_filme:
        filme_escolhido = filmes_nome[k]

for l in range(len(filmes)):
    for m in range(len(DATAFRAME_MOVIES["title"])):
        if filmes[l] == filmes_id[m]:
            filmes_recomendados.append(filmes_nome[m])

print("\nUsuário:", username
      + "\nFilme:", "[" + str(id_filme) + "]", filme_escolhido)
print("Tags:", str(tags).strip("[]")
      + "\nFilmes Recomendados:\n",
      str(filmes)+"\n"+
      str(filmes_recomendados).strip("[]"))
