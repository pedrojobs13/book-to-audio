import os
import pymupdf  # fitz
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

# TTS
from TTS.api import TTS
import torch

load_dotenv()

model = init_chat_model("llama3-8b-8192", model_provider="groq")

device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(model_name="tts_models/en/ljspeech/vits--neon", progress_bar=False, gpu=device == "cuda").to(device)

system_template = """
Extraia o texto fornecido e retorne exclusivamente o conteúdo textual puro, sem qualquer introdução, comentário, cabeçalho, rodapé ou texto adicional como 'Aqui está o texto reescrito' ou similares. No início do texto, adicione o número da página no formato 'Página {paginaAtual}: ', seguido do texto extraído. Não adicione, modifique ou interprete o conteúdo além de incluir o número da página. Ignore completamente se o texto estiver vazio e não produza nenhuma saída nesse caso. Não inclua tabelas, imagens ou outros elementos não textuais. A saída deve conter apenas o texto fornecido com o número da página no início, sem nenhuma outra palavra ou frase além do conteúdo original e do indicador de página.
"""

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

doc = pymupdf.open("Walter-Isaacson-Elon-Musk-2023-S.pdf")

os.makedirs("audios", exist_ok=True)

for page in doc:
    text = page.get_text()
    paginaAtual = page.number

    if not text.strip():
        print(f"Página {paginaAtual} vazia, pulando.")
        continue

    prompt = prompt_template.invoke({"text": text, "paginaAtual": paginaAtual})
    response = model.invoke(prompt, temperature=0.0)

    content = response.content.strip()
    if content:
        audio_path = f"audios/pagina_{paginaAtual}.wav"
        print(f"Gerando áudio da página {paginaAtual}...")
        tts.tts_to_file(text=content, file_path=audio_path)
    else:
        print(f"Nenhum conteúdo retornado para a página {paginaAtual}, pulando.")
