import streamlit as st
import pandas as pd
import dados

st.set_page_config(page_title="Filmes", layout="wide")
st.title("Filmes")

# Carrega dados para montar selects e tabela
filmes = dados.obter_dados()
df = pd.DataFrame(filmes, columns=["id", "nome", "ano", "nota"]) if filmes else pd.DataFrame(columns=["id","nome","ano","nota"])

left, middle, right = st.columns(3)

# ----------------- ADICIONAR -----------------
with left:
    st.subheader("Adicionar")
    with st.form("form_add", border=True):
        nome = st.text_input("Nome do Filme:", key="add_nome")
        ano  = st.number_input("Ano do Filme:", min_value=2010, max_value=2025, step=1, format="%d", key="add_ano")
        nota = st.slider("Nota do filme:", 0.0, 10.0, 5.0, key="add_nota")
        add_ok = st.form_submit_button("➕ Adicionar")
    if add_ok:
        dados.cria_tabela()
        dados.insere_dados(nome, int(ano), float(nota))
        st.success("Filme cadastrado!")
        st.rerun()

# ----------------- EDITAR -----------------
with middle:
    st.subheader("Editar")
    if df.empty:
        st.info("Sem filmes para editar.")
    else:
        opcoes_edit = [(int(r.id), f"[{int(r.id)}] {r.nome} — {int(r.ano)} — {float(r.nota):.1f}") for _, r in df.iterrows()]
        sel_edit = st.selectbox("Escolha um filme", options=opcoes_edit, format_func=lambda x: x[1], key="sel_edit")
        sel_id = sel_edit[0]
        atual = df[df["id"] == sel_id].iloc[0]

        with st.form("form_edit", border=True):
            novo_nome = st.text_input("Nome", value=str(atual["nome"]), key="edit_nome")
            novo_ano  = st.number_input("Ano", min_value=2010, max_value=2025, step=1, format="%d", value=int(atual["ano"]), key="edit_ano")
            nova_nota = st.slider("Nota", 0.0, 10.0, float(atual["nota"]), key="edit_nota")
            edit_ok = st.form_submit_button("✏️ Salvar alterações")
        if edit_ok:
            afetadas = dados.editar_dados(sel_id, novo_nome, int(novo_ano), float(nova_nota))
            if afetadas:
                st.success(f"Filme [{sel_id}] atualizado.")
            else:
                st.warning("Nada alterado.")
            st.rerun()

# ----------------- EXCLUIR -----------------
with right:
    st.subheader("Excluir por ID")
    if df.empty:
        st.info("Sem filmes para excluir.")
    else:
        opcoes_del = [(int(r.id), f"[{int(r.id)}] {r.nome} — {int(r.ano)} — {float(r.nota):.1f}") for _, r in df.iterrows()]
        sel_del = st.selectbox("Selecione o filme", options=opcoes_del, format_func=lambda x: x[1], key="sel_del")
        if st.button("🗑️ Excluir", key="btn_del", width="stretch"):
            afetadas = dados.deletar_dados(sel_del[0])
            if afetadas:
                st.success(f"Filme [{sel_del[0]}] excluído.")
            else:
                st.warning("Nenhum registro excluído.")
            st.rerun()

# ----------------- LISTA -----------------
st.header("Lista de Filmes:")
if df.empty:
    st.info("Nenhum filme cadastrado ainda.")
else:
    st.dataframe(df, use_container_width=True)
