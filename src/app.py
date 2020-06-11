#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import tkinter as tk
from tkinter.ttk import Combobox as CB

__version__ = "1.0"


def main(self):
    import pandas as pd
    dfTAGS   = pd.read_csv("tags.csv", usecols=["movieId", "tag"], sep=",")
    dfMOVIES = pd.read_csv("movies.csv", usecols=["movieId", "title"], sep=",")

    lUsername = tk.Label(self, text="Nome de Usuário:")
    eUsername = tk.Entry(self)

    lFilme = tk.Label(self, text="Filme:                   ")
    eFilme = tk.Entry(self)

    lUsername.grid(row=0, column=0)
    eUsername.grid(row=0, column=1)

    lFilme.grid(row=1, column=0)
    eFilme.grid(row=1, column=1)


    def show_profile():
        wProfile = tk.Toplevel()

        vUsername = eUsername.get()
        vFilmeID  = eFilme.get()

        tags   = []
        filmes = []

        filmesCol = dfTAGS["movieId"].values
        tagsCol   = dfTAGS["tag"].values

        for i in range(len(filmesCol)):
            if int(vFilmeID) == int(filmesCol[i]):
                if tagsCol[i] not in tags:
                    tags.append(tagsCol[i].lower())

        for j in range(len(tagsCol)):
            if tagsCol[j].lower() in tags:
                if filmesCol[j] not in filmes:
                    filmes.append(filmesCol[j])

        filmesId       = dfMOVIES["movieId"].values
        filmesNome     = dfMOVIES["title"].values
        filmeEscolhido = ""

        for k in range(len(filmesNome)):
            if int(filmesId[k]) == int(vFilmeID):
                filmeEscolhido = filmesNome[k]

        lUsernameProfile = tk.Label(wProfile, text="Nome de usuário: " + vUsername)
        lUsernameProfile.grid(row=0, column=0, sticky=tk.W)

        lFilmeID   = tk.Label(wProfile, text="ID do Filme: " + str(vFilmeID))
        lFilmeID.grid(row=1, column=0, sticky=tk.W)

        lFilmeNome = tk.Label(wProfile, text="Nome do Filme: " + filmeEscolhido)
        lFilmeNome.grid(row=2, column=0, sticky=tk.W)

        lTags      = tk.Label(wProfile, text="Tags:")
        lTags.grid(row=3, column=0, sticky=tk.W)
        cbTags     = CB(wProfile, width=30, values=tags).grid(row=3, column=1)

        filmesRecomendados = []
        for l in range(len(filmes)):
            for m in range(len(filmesNome)):
                if filmes[l] == filmesId[m]:
                    filmesRecomendados.append(filmesNome[m])

        lFilmesIDRecomendados  = tk.Label(wProfile, text="ID de Filmes Recomendados:")
        lFilmesIDRecomendados.grid(row=4, column=0, sticky=tk.W)
        cbFilmesIDRecomendados = CB(wProfile, width=30, values=filmes)
        cbFilmesIDRecomendados.grid(row=4, column=1)

        lFilmesRecomendados    = tk.Label(wProfile, text="Filmes Recomendados:")
        lFilmesRecomendados.grid(row=5, column=0, sticky=tk.W)
        cbFilmesRecomendados   = CB(wProfile, width=30, values=filmesRecomendados)
        cbFilmesRecomendados.grid(row=5, column=1)

        wProfile.mainloop()

    bEnviar = tk.Button(self, text="Enviar", command=show_profile)
    bEnviar.grid(row=2, column=0)


def run():
    root = tk.Tk()
    root.title("Sistema de Recomendação")
    root.geometry("295x85")
    root.resizable(False, False)
    main(root)
    root.mainloop()


if __name__ == "__main__":
    run()
