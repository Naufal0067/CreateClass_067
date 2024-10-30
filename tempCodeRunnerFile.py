class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def menghitung_luas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"
    

persegi_p = PersegiPanjang(15,3)
print(persegi_p)
print("Keliling:", persegi_p.keliling(),"cm")
print("Luas:",persegi_p.menghitung_luas(),"cm²")