import whisper
import soundfile as sf
import numpy as np
from .base_asr import BaseASR


class WhisperASR(BaseASR):
    def __init__(self, model_name: str = "base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path: str, language: str = None) -> str:
        # 使用 soundfile 读取音频
        audio_array, sampling_rate = sf.read(audio_path)

        # Whisper 需要单声道、16kHz 音频
        if len(audio_array.shape) > 1:
            audio_array = np.mean(audio_array, axis=1)

        if sampling_rate != 16000:
            # 如果需要，这里可以添加重采样代码
            pass

        audio_array = audio_array.astype(np.float32)
        # 调用 Whisper 模型
        result = self.model.transcribe(audio_array, language=language)

        return result["text"].strip()