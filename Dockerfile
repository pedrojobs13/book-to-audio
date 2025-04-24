# Use a imagem base do Coqui-AI TTS (CPU version)
FROM ghcr.io/coqui-ai/tts-cpu:latest

# Expor a porta 7860 para o Gradio (caso você use no futuro)
EXPOSE 7860

# Definir o diretório de trabalho
WORKDIR /app

# Instalar gradio (seu código importa esta biblioteca)
RUN pip install --no-cache-dir gradio

# Copiar seu arquivo app.py para dentro do container
COPY app.py /app/app.py

# Especificar o entrypoint para evitar conflitos com o comando 'tts'
ENTRYPOINT ["python3"]

# Executar seu script app.py
CMD ["/app/app.py"]