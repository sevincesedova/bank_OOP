class Bank():
    def __init__(self, hesab_nomresi, balans, sifre):
        self.hesab_nomresi=hesab_nomresi
        self.balans=balans
        self.sifre=sifre

    def balans_gosterme(self):
        if len(self.sifre)==4:
            return f"hesab nomresi: {self.hesab_nomresi} \nbalans: {self.balans}"
        else:
            return "sifreni duzgun daxil edin!"
        
    def balans_artirma(self, mebleq):
        self.balans+=mebleq
        return f" balansiniz {mebleq} azn artirildi. \n yeni balans: {self.balans}"
    
    def balans_cixart(self,mebleq):
        if self.balans>=mebleq:
            self.balans-=mebleq
            return f"balansinizdan {mebleq} azn cixarildi \n yeni balans: {self.balans}"
        else:
            return f"balansinizda kifayet qeder pul yoxdur"

class Kredit(Bank):
    def __init__(self, hesab_nomresi, balans, sifre):
        super().__init__(hesab_nomresi, balans, sifre)
    def kredit_vermek(self, mebleq):
        self.balans+=mebleq
        return f"{mebleq} azn kredit goturdunuz \n yeni balans: {self.balans}"
    def kredit_odemek(self,mebleq):
        ayliq_odenis=mebleq/12
        if self.balans >= ayliq_odenis:
            self.balans -= ayliq_odenis
            return f" balansinizdan {ayliq_odenis} AZN ayliq kredit ödənişi həyata keçirildi. Yeni balans: {self.balans} AZN."
        else:
            return "Balansınızda kifayət qədər pul yoxdur."

sifre_nomresi=input(" giris etmek ucun sifrenizi daxil edin: ")
bank_hesab=Bank(1234567891234567,2000,sifre_nomresi)
print(bank_hesab.balans_gosterme())

if len(bank_hesab.sifre)==4: 
    secim=int(input("hansi emeliyyati secmek isteyirsiniz? \nbalans artirmaq ucun 1 yazin \nbalans cixartmaq ucun 2 yazin \nkredit goturmek isteyirsinizse 3 yazin \nkredit odemek isteyirsinizse 4 yazin \nsecim: "))
    if secim==1:
        artirilan_balans=float(input("mebleği daxil edin: "))
        print(bank_hesab.balans_artirma(artirilan_balans))
    elif secim==2:
       cixarilan_balans=float(input("mebleği daxil edin: "))
       print(bank_hesab.balans_cixart(cixarilan_balans))
    elif secim == 3:
        kredit_cekmek_miqdari = float(input("Çəkmək istədiyiniz kredit miqdarını daxil edin: "))
        kredit_hesabı = Kredit(bank_hesab.hesab_nomresi, bank_hesab.balans, bank_hesab.sifre)
        print(kredit_hesabı.kredit_vermek(kredit_cekmek_miqdari))

    elif secim == 4:
        odeme_miqdarı = float(input("goturulen kredit miqdarını daxil edin: "))
        kredit_hesabı = Kredit(bank_hesab.hesab_nomresi, bank_hesab.balans, bank_hesab.sifre)
        print(kredit_hesabı.kredit_odemek(odeme_miqdarı))
    else:
        print("duzgun secim edin: ")
else:
    print(bank_hesab.balans_gosterme())

