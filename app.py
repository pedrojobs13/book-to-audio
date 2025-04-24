import torch 
from TTS.api import TTS
import gradio as gr

device = "cuda" if torch.cuda.is_available() else "cpu"

def generate_audio(text, model_name):
    tts = TTS(model_name=model_name, progress_bar=False, gpu=device=="cuda").to(device)
    audio_path = tts.tts_to_file(text=text, file_path="output.wav")
    return audio_path

generate_audio("example", "tts_models/en/ljspeech/fast_pitch")