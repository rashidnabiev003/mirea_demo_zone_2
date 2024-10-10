from IPython.display import Audio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

# API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-medium"
# headers = {"Authorization": "Bearer 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"}

def generate_audio(prompt_text=["metal"], path="test"):
    model = MusicGen.get_pretrained("medium", "cuda")
    model.set_generation_params(duration=10)
    audio = model.generate(prompt_text)
    audio_write(path, audio[0].cpu(), model.sample_rate, strategy="loudness")
    
#generate_audio()