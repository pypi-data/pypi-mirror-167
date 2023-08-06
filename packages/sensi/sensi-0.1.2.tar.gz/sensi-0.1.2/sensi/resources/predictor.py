from typing import List

from nltk.tokenize import sent_tokenize

from ..database.query import read_log_likelihood, read_log_prior
from .processing import freqs, normalisasi
from .sentiment import predict_nbc

logprior = readLogprior()
loglikelihood = readLoglikelihood()

tr = 0


def pred_total(text: str) -> float:
    x = predict_nbc(text, logprior, loglikelihood)
    return round(x, 4)


def convert(tup: tuple, di: dict) -> dict:
    for i, (a, b) in enumerate(tup):
        di[i] = {"text": a, "freq": b}
    return di


def per_kalimat(text: str) -> list:
    kalimat = []
    x = sent_tokenize(text)

    for i in range(len(x)):
        sk = predict_nbc(x[i], logprior, loglikelihood)
        lb = "1" if sk > tr else "0"

        kalimat.append(
            {
                "kalimat": x[i],
                "skor": round(sk, 4),
                "label": lb,
                "perkata": per_kata(x[i]),
            }
        )

    return kalimat


def per_kata(text: str) -> List[str]:
    temp_norm = normalisasi(text)
    frekwensi = freqs(temp_norm)    # type: ignore

    kata = []
    dicti = {}
    kamus_freq = Convert(frekwensi, dicti)   # type: ignore

    for _, y in kamus_freq.items():
        sk = predict_nbc(y["text"], logprior, loglikelihood)
        lb = "1" if sk > tr else "0"

        kata.append(
            {
                "kata": normalisasi(y["text"])[0],
                "skor": round(sk, 4),
                "label": lb,
                "freq": y["freq"],
            }
        )

    return kata 
