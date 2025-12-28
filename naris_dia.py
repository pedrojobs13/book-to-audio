from transformers import AutoProcessor, DiaForConditionalGeneration
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

torch_device = "cuda"
model_checkpoint = "nari-labs/Dia-1.6B-0626"

text = [
    "[S1] Fala meu irmão. [S2] You get full control over scripts and voices. [S1] Wow. Amazing. (laughs) [S2] Try it now on Git hub or Hugging Face."
]
processor = AutoProcessor.from_pretrained(model_checkpoint)
inputs = processor(text=text, padding=True, return_tensors="pt").to(device)

model = DiaForConditionalGeneration.from_pretrained(model_checkpoint).to(device)
outputs = model.generate(
    **inputs, max_new_tokens=3072, guidance_scale=3.0, temperature=1.8, top_p=0.90, top_k=45
)

outputs = processor.batch_decode(outputs)
processor.save_audio(outputs, "example.mp3")