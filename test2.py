from pprint import pprint
from Questgen import main
qg = main.QGen()
payload = {
            "input_text": "Sachin Tendulkar is a former international cricketer from India and a former captain of the Inidan National team . He is widely regraded as one of the greatest batsmen in the history of cricket."
        }

output = qg.predict_mcq(payload)
pprint(output)