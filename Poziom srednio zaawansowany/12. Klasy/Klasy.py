class Pracownik():

    firma = 'asprodukt.com'
    iloscPodwyzki = 1.05

    def __init__(self, imie, nazwisko, wiek, zarobki):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.zarobki = zarobki
        self.mail = f"{self.imie.lower()}.{self.nazwisko.lower()}@{self.firma}"

    def podwyzka(self):
        self.zarobki *= self.iloscPodwyzki
    
    @classmethod
    def zmienPodwyzke(cls,nowaWartosc):
        cls.iloscPodwyzki = nowaWartosc
    

pr1 = Pracownik("Kamil", "Koziol", 18, 18000)
Pracownik.podwyzka(pr1)
Pracownik.zmienPodwyzke(1.20)
print(pr1.iloscPodwyzki)
pr2 = Pracownik("PeePee",'PooPoo',69,420)
Pracownik.zmienPodwyzke(2)
pr2.zmienPodwyzke(5)
print(pr1.iloscPodwyzki,pr2.iloscPodwyzki)


