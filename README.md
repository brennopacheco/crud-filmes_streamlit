# 🎬 Cadastro de Filmes com Python, SQLite e Streamlit

Este projeto é um CRUD básico para cadastro e listagem de filmes, utilizando **SQLite** como banco de dados e **Streamlit** para a interface web.
- [Aplicação Rodando AQUI](https://crud-filmes-brennp.streamlit.app/)

## 🚀 Tecnologias utilizadas
- [Python](https://www.python.org/)
- [SQLite](https://www.sqlite.org/)
- [Streamlit](https://streamlit.io/)

## 📂 Estrutura do Projeto
- `dados.py` → contém as funções para:
  - Conectar ao banco (`conecta_db`)
  - Criar a tabela de filmes (`cria_tabela`)
  - Inserir novos registros (`insere_dados`)
  - Listar todos os filmes (`obter_dados`)

- `form.py` → interface em Streamlit que permite:
  - Inserir novos filmes (nome, ano e nota)
  - Visualizar todos os filmes cadastrados em uma tabela

## ▶️ Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install streamlit
   ```

3. Execute o projeto:
```bash
   streamlit run form.py
   ```

