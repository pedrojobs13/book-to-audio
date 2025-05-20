FROM ghcr.io/coqui-ai/tts-cpu:latest

WORKDIR /app

# Instalar dependências necessárias
RUN pip install --no-cache-dir gradio
RUN pip install pymupdf
RUN pip install langchain
RUN pip install langchain_core
RUN pip install dotenv
RUN pip install langchain-groq

# Criar diretório para os arquivos de saída
RUN mkdir -p /app/outputs

# Copiar o script Python e o arquivo de texto grande (se disponível)
COPY app.py /app/app.py
COPY Walter-Isaacson-Elon-Musk-2023-S.pdf /app/Walter-Isaacson-Elon-Musk-2023-S.pdf

# Usar o entrypoint explícito para evitar conflito com o comando "tts"
ENTRYPOINT ["python3"]

# Comando para executar o script Python
CMD ["/app/app.py"]