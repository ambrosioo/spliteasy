import streamlit as st
import pandas as pd
import os

# Título da aplicação
st.title("SplitEasy - Divisor de Arquivos CSV")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Selecione um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Solicitar o número de linhas por arquivo
    chunk_size = st.number_input(
        "Quantas linhas por arquivo?", min_value=1, value=100)

    # Botão para dividir o arquivo
    if st.button("Dividir Arquivo"):
        # Ler o arquivo CSV
        df = pd.read_csv(uploaded_file, dtype=str)

        # Calcular o número de partes
        num_chunks = (len(df) // chunk_size) + \
            (1 if len(df) % chunk_size != 0 else 0)

        # Dividir o arquivo e salvar as partes
        for i, chunk in enumerate(range(0, len(df), chunk_size)):  # Corrigido aqui
            chunk_df = df.iloc[chunk:chunk + chunk_size]
            output_file = f"parte_{i + 1}.csv"
            chunk_df.to_csv(output_file, index=False)
            st.write(f"Arquivo salvo: {output_file}")

        # Mensagem de sucesso
        st.success(f"Arquivo dividido em {num_chunks} partes!")
