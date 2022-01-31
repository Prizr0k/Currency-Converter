import requests

list_currencys = ['usd', 'eur', 'gbp', 'aud', 'chf', 'cad', 'jpy', 'mkd', 'bif', 'all', 'mur', 'ves', 'npr', 'isk', 'gip', 'gel', 'bzd', 'gnf', 'szl', 'sos', 'aed', 'php', 'ils', 'mro', 'cop', 'gyd', 'rwf', 'ern', 'wst', 'cny', 'sar', 'myr', 'kzt', 'pab', 'nad', 'syp', 'mop', 'bam', 'idr', 'tnd', 'xof', 'tjs', 'bob', 'xcd', 'mwk', 'gtq', 'kwd', 'czk', 'pgk', 'uah', 'etb', 'gmd', 'awg', 'mmk', 'mvr', 'sek', 'mad', 'ron', 'byn', 'rsd', 'bsd', 'djf', 'sll', 'kes', 'bhd', 'omr', 'rub', 'lyd', 'clp', 'fjd', 'cdf', 'mzn', 'ugx', 'bdt', 'qar', 'mxn', 'amd', 'htg', 'lrd', 'sdg', 'top', 'vuv', 'hkd', 'thb', 'xaf', 'mdl', 'uyu', 'ttd', 'lak', 'bwp', 'jod', 'bgn', 'vnd', 'uzs', 'mga', 'nio', 'cve', 'aoa', 'khr', 'nok', 'lkr', 'pln', 'pen', 'iqd', 'stn', 'xpf', 'hnl', 'scr', 'dop', 'nzd', 'hrk', 'dzd', 'ars', 'bnd', 'kmf', 'lsl', 'tzs', 'bbd', 'ang', 'pkr', 'krw', 'azn', 'crc', 'jmd', 'ssp', 'mru', 'mnt', 'brl', 'egp', 'sgd', 'zar', 'kgs', 'pyg', 'srd', 'ghs', 'cup', 'dkk', 'inr', 'try', 'twd', 'tmt', 'afn', 'sbd', 'zmw', 'yer', 'lbp', 'huf', 'ngn', 'irr', 'svc']

usd = requests.get('http://www.floatrates.com/daily/usd.json')

eur = requests.get('http://www.floatrates.com/daily/eur.json')


cash = {'usd': usd.json(), 'eur': eur.json()}
rate = 'inverseRate'

your_currency = input().lower()

while True:
    need_currency = input().lower()
    if need_currency == '':
        break
    how_mach = float(input())
    if need_currency not in list_currencys:
        print('This currency is not on the list')
        continue
    elif need_currency == your_currency:
        print(f'You received {round(how_mach, 2)} {need_currency.upper()}')
        continue
    print('Checking the cache...')
    if need_currency in cash:
        print('Oh! It is in the cache!')
        print(f'You received {round(how_mach * cash[need_currency][your_currency][rate], 2)} {need_currency.upper()}.')
    else:
        print('Sorry, but it is not in the cache!')
        x = requests.get(f'http://www.floatrates.com/daily/{need_currency}.json')
        cash[need_currency] = x.json()
        print(f'You received {round(how_mach * cash[need_currency][your_currency][rate], 2)} {need_currency.upper()}.')


