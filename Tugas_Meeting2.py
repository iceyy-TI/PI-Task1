class Looping:   
    def __init__(self):
        pass
    def kali(var1, var2):
        return var1 * var2
  
    def bagi(var1, var2):
        return var1 / var2
  
    def jumlah(var1, var2):
        return var1 + var2
  
    def kurang(var1, var2):
        return var1 - var2

while True : # ini akan menjadi perulangan berulang kali
  var1 = int(input("Berikan Variable ke-1 : ")) # ini akan meminta inputan berupa integer
  var2 = int(input("Berikan Variable ke-2 : ")) # sama seperti sebelumnya
  
  print("Kali : ", Looping.kali(var1,var2))
  print("Bagi : ", Looping.bagi(var1,var2))
  print("Tambah : ", Looping.jumlah(var1,var2))
  print("Kurang : ", Looping.kurang(var1,var2))
  
  #kita perlu membuat perintah agar perulangan di hentikan
  print("Hentikan perulangan?") 
  close = input("Ketik 'Y' pada kotak input untuk menghentikan perulangan")
  if close == 'Y' or close == 'y':
        break
        
  # dengan ini perulangan dapat berhenti jiak user mengetikkan Y atau y

