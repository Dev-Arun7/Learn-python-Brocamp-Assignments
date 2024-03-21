dict1 = {"NFLX": 4950, "TREX": 2400, "FIZZ": 1800, "XPO": 1700}
dict2 = {key: value for key, value in dict1.items() if value > 2000}

print(dict2)
