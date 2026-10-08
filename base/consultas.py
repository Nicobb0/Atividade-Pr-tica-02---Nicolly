from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    stmt = select(Livro)
    livros = session.scalars(stmt).all()
    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"Título: {livro.titulo} | Autor: {livro.autor.nome} | Status: {status}")


def listar_livros_disponiveis(session):
    stmt = select(Livro).where(Livro.disponivel == True)
    livros = session.scalars(stmt).all()
    for livro in livros:
        print(f"Título: {livro.titulo} | Autor: {livro.autor.nome}")


def buscar_livros_por_titulo(session, trecho):
    stmt = select(Livro).where(Livro.titulo.contains(trecho))
    livros = session.scalars(stmt).all()
    if not livros:
        print(f"Nenhum livro encontrado com o termo '{trecho}'.")
        return
    for livro in livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"Título: {livro.titulo} | Autor: {livro.autor.nome} | Status: {status}")


def listar_livros_por_autor(session, nome_autor):
    stmt = select(Autor).where(Autor.nome.contains(nome_autor))
    autor = session.scalar(stmt)
    if not autor:
        print(f"Autor '{nome_autor}' não encontrado.")
        return

    for livro in autor.livros:
        status = "Disponível" if livro.disponivel else "Indisponível"
        print(f"Título: {livro.titulo} | Status: {status}")