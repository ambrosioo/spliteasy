import streamlit as st
import pandas as pd
import os

# Título da aplicação
st.title("SplitEasy - Divisor de Arquivos CSV")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Selecione um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Solicitar o número de linhas por arquivo
    chunk_size = st.number_input("Quantas linhas por arquivo?", min_value=1, value=100)

    # Botão para dividir o arquivo
    if st.button("Dividir Arquivo"):
        # Ler o arquivo CSV
        df = pd.read_csv(uploaded_file, dtype=str)

        # Calcular o número de partes
        num_chunks = (len(df) // chunk_size) + (1 if len(df) % chunk_size != 0 else 0)

        # Dividir o arquivo e gerar botões de download
        for i, chunk in enumerate(range(0, len(df), chunk_size)):
            chunk_df = df.iloc[chunk:chunk + chunk_size]
            csv = chunk_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=f"Baixar parte {i + 1}",
                data=csv,
                file_name=f"parte_{i + 1}.csv",
                mime="text/csv",
            )

        # Mensagem de sucesso
        st.success(f"Arquivo dividido em {num_chunks} partes!")
