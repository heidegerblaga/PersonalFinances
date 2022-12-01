import requests
import json

def pars(images):
    url = "http://ocr.asprise.com/api/v1/receipt"

    res = requests.post(url,
                        data = {
                            'api_key':'TEST',
                            'recognizer': 'auto',
                            'ref_no':'oct_python_123'
                        },
                        files = {
                            'file':open(images,'rb')

                        },
                        )


    with open("H:\Mój dysk/recipes/response.json", "w") as f:
            json.dump(json.loads(res.text),f)





