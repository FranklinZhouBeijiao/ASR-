import os
import json
from typing import Dict, List


def load_dataset(data_dir: str) -> Dict[str, Dict[str, List[str]]]:

    dataset = {}

    # 遍历每个语言目录 (en, zh)
    for lang in os.listdir(data_dir):
        lang_path = os.path.join(data_dir, lang)

        # 跳过非目录和隐藏文件（如 .DS_Store）
        if not os.path.isdir(lang_path) or lang.startswith("."):
            continue

        dataset[lang] = {"audio_paths": [], "reference_texts": []}

        # metadata.jsonl 路径
        metadata_path = os.path.join(lang_path, "metadata.jsonl")
        if not os.path.exists(metadata_path):
            print(f"[警告] 未找到 {metadata_path}，已跳过")
            continue

        # 读取 metadata.jsonl
        with open(metadata_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                item = json.loads(line)

                # 你的字段名
                audio_rel_path = item.get("wav_path")
                reference_text = item.get("transcription")

                if not audio_rel_path or not reference_text:
                    continue

                # 拼接音频完整路径
                # 因为 audio_rel_path 已经是 "./wavs/xxx.wav"，需要去掉 "./"
                audio_path = os.path.join(lang_path, audio_rel_path.lstrip("./"))

                if os.path.exists(audio_path):
                    dataset[lang]["audio_paths"].append(audio_path)
                    dataset[lang]["reference_texts"].append(reference_text)
                else:
                    print(f"[警告] 音频文件不存在: {audio_path}")

    return dataset


if __name__ == "__main__":
    # 测试加载
    test_data_dir = r"D:\desktop\hw1_testdata"
    dataset = load_dataset(test_data_dir)

    for lang, data in dataset.items():
        print(f"{lang} 数据量: {len(data['audio_paths'])}")