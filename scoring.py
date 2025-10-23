from asr.whisper_asr import WhisperASR  # 默认用 Whisper
from examples.score_dataset import evaluate_dataset
# from asr.vosk_asr import VoskASR
if __name__ == "__main__":
    # 数据集路径
    data_dir = r"D:\desktop\hw1_testdata"

    # 初始化 ASR 模型（可替换成其他实现）
    asr = WhisperASR(model_name="tiny")
    # 如果要用别的 ASR，比如：
    # asr = VoskASR(model_dir=r"D:\desktop\models\vosk-model-en-us-0.22")

    # 评测所有语言
    evaluate_dataset(data_dir, asr)
    # 如果只想评测中文
    # evaluate_dataset(data_dir, asr, lang="zh")
    # 如果只想评测英文
    # evaluate_dataset(data_dir, asr, lang="en")

