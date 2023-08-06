<p align=center>Framework analisis sentiment teks Bahasa Indonesia, menggunakan Klasifikasi Naive-Bayes</p>

## Dependensi

```python
sastrawi nltk numpy pandas sqlalchemy
```

## Instalasai
Belum ada setup.py, install secara manual.
1. copy isi repository kedalam directory proyek anda
1. gunakan fungsi-fungsi yang diinginkan dengan meng-impor fungsi-2 tsb.

## Penggunaan
- Contoh penerapan dapat dilihat pada directory 'apis' pada repository [flask-sk](https://github.com/GazDuckington/flask-sk)

- Contoh sederhana:
  ```python
  from database.query import read_log_likelihood, read_log_prior
  from resources.sentiment import predict_nbc
  
  logprior = read_log_prior()
  loglikelihood = read_log_likelihood()
  text = "contoh text yang ingin di analisis."
  
  print(predict_nbc(text, logprior, loglikelihood))
  ```
baca ```resources/predictor.py``` untuk berbagai contoh lainnya.
