class Gempa:
    # properti
    lok = ""
    skl = 0

    # konstruktor
    def __init__(self, lokasi, skala):
        self.lok = lokasi
        self.skl = skala

    # method
    def dampak(self):
        if self.skl <= 2 :
            return "tidak berasa"
        elif self.skl >= 2 and self.skl <= 4:
            return "retak-retak"
        elif self.skl >= 2 and self.skl <= 6:
            return "bangunan roboh"
        elif self.skl >= 6:
            return "bangunan roboh dan berpotensi tsunami"
        
    def cetak(self):
        print(
            '\n==========================',
            '\nLokasi gempa :', self.lok,
            '\nSkala gempa :', self.skl)
        