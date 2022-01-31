import requests
s = "inverseRate"


r = requests.get(f'http://www.floatrates.com/daily/usd.json')
ans_usd = r.json()
r = requests.get(f'http://www.floatrates.com/daily/eur.json')
ans_eur = r.json()
cash = {"usd": ans_usd, "eur": ans_eur}
print(cash["usd"]["eur"]['rate'])
