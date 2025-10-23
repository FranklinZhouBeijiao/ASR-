from metrics.cer import calculate_cer
from metrics.wer import calculate_wer

# 中文示例
ref_zh = "今天天气很好，我们去公园散步。"
hyp_zh = "今天天气不错，我们去公园走走。"
cer_zh = calculate_cer(ref_zh, hyp_zh, "zh")
print(f"中文 CER: {cer_zh:.2f}")

# 英文示例
ref_en = "The quick brown fox jumps over the lazy dog."
hyp_en = "The quick brown fox jump over the lazy dog."
cer_en = calculate_cer(ref_en, hyp_en)
wer_en = calculate_wer(ref_en, hyp_en)
print(f"英文 CER: {cer_en:.2f}, WER: {wer_en:.2f}")