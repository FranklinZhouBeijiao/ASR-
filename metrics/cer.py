from .levenshtein import levenshtein_distance
from preprocessing.text_normalizer import normalize_text

def calculate_cer(ref: str, hyp: str, lang: str = "en") -> float:
    ref_norm = normalize_text(ref, lang)
    hyp_norm = normalize_text(hyp, lang)
    distance = levenshtein_distance(ref_norm, hyp_norm)
    return distance / max(len(ref_norm), 1)