import os
from data_loader import load_dataset
from metrics.cer import calculate_cer
from metrics.wer import calculate_wer



# 如果要用别的 ASR，改成：
# from asr_scoring_tool.asr.other_asr import OtherASR as ASRModel

def evaluate_dataset(data_dir: str, asr_model, lang: str = None):
    """
    批量评测数据集
    :param data_dir: 数据集根目录
    :param asr_model: ASR 模型实例（必须实现 transcribe 方法）
    :param lang: 指定评测语言，None 表示评测所有语言
    """
    dataset = load_dataset(data_dir)

    # 如果指定了语言，只评测该语言
    languages = [lang] if lang else dataset.keys()

    for lang_code in languages:
        if lang_code not in dataset:
            continue

        audio_paths = dataset[lang_code]["audio_paths"]
        references = dataset[lang_code]["reference_texts"]

        total_cer = 0.0
        total_wer = 0.0
        count = 0

        print(f"\n===== 开始评测 {lang_code} 数据集 =====")
        for audio_path, ref_text in zip(audio_paths, references):
            hyp_text = asr_model.transcribe(audio_path, language=lang_code)

            if lang_code == "zh":
                # 中文只计算 CER
                cer = calculate_cer(ref_text, hyp_text, lang=lang_code)
                total_cer += cer
            elif lang_code == "en":
                # 英文只计算 WER
                wer = calculate_wer(ref_text, hyp_text, lang=lang_code)
                total_wer += wer

            count += 1

            # 每 10 条打印一次进度
            if count % 10 == 0:
                print(f"[{count}/{len(audio_paths)}]")

        if lang_code == "zh":
            avg_cer = total_cer / count if count > 0 else 0
            print(f"===== {lang_code} 数据集评测完成 =====")
            print(f"平均 CER: {avg_cer:.3f}\n")
        elif lang_code == "en":
            avg_wer = total_wer / count if count > 0 else 0
            print(f"===== {lang_code} 数据集评测完成 =====")
            print(f"平均 WER: {avg_wer:.3f}\n")

