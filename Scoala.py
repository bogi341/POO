class Scoala:
    def __init__(elevi,profesori,director,clase,metri_patrati):
        self.elevi = elevi
        self.profesori = profesori
        self.director = director
        self.clase = clase
        self.metri_patrati = metri_patrati

    def __str__(self):
        return f"Scoala cu {self.elevi} elevi,are {self.profesori} profesori, directorul {self.director}.Ea are {self.clase} clase, si {self.metri_patrati} metri patrati."

    def numar_total_persoane(self):
        return self.elevi + self.profesori + 1 # 1 este de la director

    def densitate_elevi(self):
        return self.elevi / self.metri_patrati

    def schimba_director(self, nou_director):
        self.director = nou_director
        print(f"Noul director al școlii este {self.director}.")

    # Exemplu
    scoala1 = scoala(elevi=500, profesori=30, director="Director1", clase=20, metri_patrati=10000)
    scoala2 = scoala(elevi=450, profesori=25, director="Director2", clase=18, metri_patrati=9500)

    print(scoala1)
    print(scoala2)



