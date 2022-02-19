class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def imprime(self):
        print(f'Nome: {self.nome} - {self.ano} - LIKES: {self.likes}')


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.ano} - Duração: {self.duracao} min - LIKES: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.ano} - {self.temporadas} Temporadas - LIKES: {self.likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, idx):
        return self._programas[idx]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for x in playlist_fim_de_semana:
    print(x)
