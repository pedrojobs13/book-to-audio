## Docker do para traduzir transformar audio-livro app.py

docker build -t tts-app .

docker run -it -p 7860:7860 tts-app


## Acessar os modelos:
    DIA:
        https://github.com/nari-labs/dia
    Chatterbox:
        https://github.com/resemble-ai/chatterbox
    Coqui:
        https://github.com/coqui-ai/TTS

## Criar venv
python -m venv venv

.\venv\Scripts\activate

## Instalar pacotes
pip install -r requirements.txt