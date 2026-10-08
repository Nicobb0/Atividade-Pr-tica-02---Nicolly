from models import Autor, Livro


def popular_banco(session):
    autor1 = Autor(nome="Gabriel García Márquez", pais="Colômbia")
    autor2 = Autor(nome="J.R.R. Tolkien", pais="Reino Unido")
    autor3 = Autor(nome="Jane Austen", pais="Reino Unido")
    autor4 =  Autor(nome="Gleydson Brito", pais="República tcheca")

    session.add(autor1)

    livros = [
        Livro(titulo="Fantástico Mundo de Elliot", ano=2023, disponivel=True, autor=autor4),
        Livro(titulo="O Amor nos Tempos do Cólera", ano=1985, disponivel=False, autor=autor1),
        Livro(titulo="Crônica de uma Morte Anunciada", ano=1981, disponivel=True, autor=autor1),
        Livro(titulo="O Hobbit", ano=1937, disponivel=True, autor=autor2),
        Livro(titulo="O Senhor dos Anéis", ano=1954, disponivel=False, autor=autor2),
        Livro(titulo="Orgulho e Preconceito", ano=1813, disponivel=True, autor=autor3),
    ]

    session.add_all([autor2, autor3] + livros)
    session.commit()