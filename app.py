# app.py - İlk Kod Versiyonu

def karsilama_mesaji(kullanici_adi):
    return f"Merhaba {kullanici_adi}, Git öğrenmeye hoş geldin!"

if __name__ == "__main__":
    kullanici = "Ahmet"
    print(karsilama_mesaji(kullanici))
