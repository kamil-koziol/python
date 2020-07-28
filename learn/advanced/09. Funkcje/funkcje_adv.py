def buyMe(prefix, what, *args, **kwargs):
    print(prefix, what, " i ".join(args))
    print(kwargs)


buyMe("we kup", 'auto', 'ziombel', 'mamo', 'tato',
      sklep="Mercedes", kiedy="Jak najszybciej")

products = ['mleko', 'chleb', 'ciabata']
parametry = {'cena': 'tanio', "czas": "na herbate"}

buyMe("Kup", "gazetę", *products, **parametry)