import streamlit as st
import pandas as pd

# Título da aplicação
st.title("SplitEasy - Divisor de Arquivos CSV")

# Inicializar o session state para armazenar as partes
if 'partes' not in st.session_state:
    st.session_state.partes = []

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Selecione um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Solicitar o número de linhas por arquivo
    chunk_size = st.number_input("Quantas linhas por arquivo?", min_value=1, value=100)

    # Botão para dividir o arquivo
    if st.button("Dividir Arquivo"):
        # Ler o arquivo CSV
        df = pd.read_csv(uploaded_file, dtype=str)

        # Limpar as partes anteriores (se houver)
        st.session_state.partes = []

        # Dividir o arquivo e armazenar as partes no session state
        for i, chunk in enumerate(range(0, len(df), chunk_size)):
            chunk_df = df.iloc[chunk:chunk + chunk_size]
            csv = chunk_df.to_csv(index=False).encode('utf-8')
            st.session_state.partes.append((f"parte_{i + 1}.csv", csv))

        # Mensagem de sucesso
        st.success(f"Arquivo dividido em {len(st.session_state.partes)} partes!")

# Exibir botões de download para todas as partes
if st.session_state.partes:
    st.write("### Partes do Arquivo")
    for nome_arquivo, dados_csv in st.session_state.partes:
        st.download_button(
            label=f"Baixar {nome_arquivo}",
            data=dados_csv,
            file_name=nome_arquivo,
            mime="text/csv",
        )
