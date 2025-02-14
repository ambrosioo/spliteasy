import pandas as pd
import os
from tkinter import Tk, Button, filedialog, messagebox, simpledialog, Label

# Função para dividir o arquivo


def split_excel():
    # Abrir diálogo para selecionar o arquivo
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo CSV",
        filetypes=[("Arquivos CSV", "*.csv")]
    )

    if not file_path:
        return

    try:
        # Solicitar o número de linhas por arquivo ao usuário
        chunk_size = simpledialog.askinteger(
            "Número de Linhas",
            "Quantas linhas você deseja em cada arquivo?",
            minvalue=1
        )

        if not chunk_size:
            return

        # Lendo o arquivo CSV e garantindo que todas as colunas sejam tratadas como texto
        df = pd.read_csv(file_path, sep=',', header=0, dtype=str)
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        output_dir = os.path.dirname(file_path)

        # Calcular o número de partes
        num_chunks = (len(df) // chunk_size) + \
            (1 if len(df) % chunk_size != 0 else 0)

        for i, chunk in enumerate(range(0, len(df), chunk_size)):
            # Gerar cada chunk (pedaço)
            chunk_df = df.iloc[chunk:chunk + chunk_size]
            # Criar o nome do arquivo
            output_file = os.path.join(output_dir, f"{file_name}_{i + 1}.csv")
            # Salvar o chunk
            chunk_df.to_csv(output_file, index=False)

        # Mostrar mensagem de sucesso
        messagebox.showinfo("Sucesso", f"Arquivo dividido em {
                            num_chunks} partes!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


# Configuração do Tkinter
root = Tk()
root.title("Divisor de Arquivo CSV")
root.geometry("300x200")

# Exibir o nome "SplitEasy" no topo
Label(
    root,
    text="SplitEasy",
    font=("Arial", 16, "bold"),
    fg="blue"
).pack(pady=10)

# Botão para adicionar arquivo
Button(
    root,
    text="Adicionar Arquivo",
    command=split_excel,
    width=20,
    height=2,
    bg="blue",
    fg="white"
).pack(pady=40)

# Iniciar a interface gráfica
root.mainloop()
