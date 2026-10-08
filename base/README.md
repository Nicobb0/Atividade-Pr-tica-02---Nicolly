# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo disponivel em Livro?
O campo disponivel é um valor booleano (True ou False) que controla o estado atual de empréstimo do livro. Ele permite verificar se o exemplar está livre para ser emprestado ou se já se encontra emprestado, servindo de base para as validações das funções de empréstimo e devolução.

2. Por que é necessário chamar session.commit() após emprestar ou devolver?
Quando se altera o valor de livro.disponivel, a modificação ocorre apenas na memória dentro da sessão ativa do SQLAlchemy. A chamada ao session.commit() é necessária para confirmar a transação e salvar permanentemente a alteração no banco de dados.

3. Em qual consulta você usa o relacionamento entre Livro e Autor?

listar_livros, listar_livros_disponiveis e buscar_livros_por_titulo: ao aceder diretamente a livro.autor.nome para obter o nome do autor associado ao livro sem precisar de um JOIN manual.

listar_livros_por_autor: ao navegar pela relação inversa autor.livros para obter a lista de livros pertencentes a um determinado autor.
