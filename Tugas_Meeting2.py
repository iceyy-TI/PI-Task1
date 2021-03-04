while True : // ini akan menjadi perulangan berulang kali
  var1 = int(input("Berikan Variable ke-1 : ")) // ini akan meminta inputan berupa integer
  var2 = int(input("Berikan Variable ke-2 : ")) // sama seperti sebelumnya
  
  print(var1 / var2)
  
  //kita perlu membuat perintah agar perulangan di hentikan
  print("Hentikan perulangan?) 
  close = input(Ketik 'Y' pada kotak input untuk menghentikan perulangan)")
  if close == 'Y' or close == 'y':
        break
        
  // dengan ini perulangan dapat berhenti jiak user mengetikkan Y atau y



