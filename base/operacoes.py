from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    stmt = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalar(stmt)

    if not livro:
        print(f"Livro '{titulo}' não encontrado.")
        return

    if not livro.disponivel:
        print(f"O livro '{titulo}' já está indisponível.")
        return

    livro.disponivel = False
    session.commit()
    print(f"Livro '{titulo}' emprestado com sucesso.")


def devolver_livro(session, titulo):
    stmt = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalar(stmt)

    if not livro:
        print(f"Livro '{titulo}' não encontrado.")
        return

    if livro.disponivel:
        print(f"O livro '{titulo}' já está disponível.")
        return

    livro.disponivel = True
    session.commit()
    print(f"Livro '{titulo}' devolvido com sucesso.")