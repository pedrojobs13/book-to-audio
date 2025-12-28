import torch
import torchaudio as ta


device = "cuda" if torch.cuda.is_available() else "cpu"

# Para rodar no cpu
if(device == 'cpu'):
    original_load = torch.load

    def cpu_load(*args, **kwargs):
        if 'map_location' not in kwargs:
            kwargs['map_location'] = torch.device('cpu')
        return original_load(*args, **kwargs)

    torch.load = cpu_load

from chatterbox.tts import ChatterboxTTS
from chatterbox.mtl_tts import ChatterboxMultilingualTTS


# Multilingual examples

multilingual_model = ChatterboxMultilingualTTS.from_pretrained(device='cpu')


#text = "Fala arthur vipz esse é um modelo de voz em português"

#wav_chinese = multilingual_model.generate(text, language_id="pt")

#ta.save("testeport.wav", wav_chinese, multilingual_model.sr)



# If you want to synthesize with a different voice, specify the audio prompt

AUDIO_PROMPT_PATH = "audio.wav"

text = "Olá"
wav = multilingual_model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH, language_id="pt", top_p=0.5, temperature=0.7)

ta.save("test-2.wav", wav, multilingual_model.sr)



