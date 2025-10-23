# pip install vosk
from .base_asr import BaseASR
from vosk import Model, KaldiRecognizer
import wave
import json
import os


class VoskASR(BaseASR):
    def __init__(self, model_dir: str = None):
        if model_dir and os.path.exists(model_dir):
            self.model = Model(model_dir)
        else:
            # 自动下载模型(如果支持)或使用默认模型
            self.model = Model(lang="en-us")  # 默认英文

    def transcribe(self, audio_path: str, language: str = None) -> str:
        wf = wave.open(audio_path, "rb")
        rec = KaldiRecognizer(self.model, wf.getframerate())

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            rec.AcceptWaveform(data)

        result = rec.FinalResult()
        text = json.loads(result).get("text", "")
        return text