from .levenshtein import levenshtein_distance
from preprocessing.text_normalizer import normalize_text


def calculate_wer(ref: str, hyp: str, lang: str = "en") -> float:
    ref_norm = normalize_text(ref, lang)
    hyp_norm = normalize_text(hyp, lang)
    # print("*",ref_norm,hyp_norm)
    # 分词策略：英文按空格，中文按字符
    ref_tokens = ref_norm.split() if lang == "en" else list(ref_norm)
    hyp_tokens = hyp_norm.split() if lang == "en" else list(hyp_norm)

    distance = levenshtein_distance(ref_tokens, hyp_tokens)
    return distance / max(len(ref_tokens), 1)