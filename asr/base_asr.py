from abc import ABC, abstractmethod

class BaseASR(ABC):
    @abstractmethod
    def transcribe(self, audio_path: str, language: str = None) -> str:
        """
        给定音频路径，返回识别文本
        :param audio_path: 音频文件路径
        :param language: 语言代码，如 "en", "zh"
        :return: 识别出的文本
        """
        pass