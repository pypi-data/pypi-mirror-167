<p align=center>Framework analisis sentiment teks Bahasa Indonesia, menggunakan Klasifikasi Naive-Bayes</p>

## Dependensi

```python
sastrawi nltk numpy pandas sqlalchemy
```

## Instalasai
```bash
pip install sensi
```

## Penggunaan
- Contoh penerapan dapat dilihat pada directory 'apis' pada repository [flask-sk](https://github.com/GazDuckington/flask-sk)

- Contoh sederhana:
  ```python
  from sensi.database.query import read_log_likelihood, read_log_prior
  from sensi.resources.sentiment import predict_nbc
  
  logprior = read_log_prior()
  loglikelihood = read_log_likelihood()
  text = "contoh text yang ingin di analisis."
  
  print(predict_nbc(text, logprior, loglikelihood))
  ```
- Baca ```resources/predictor.py``` untuk berbagai contoh lainnya.
