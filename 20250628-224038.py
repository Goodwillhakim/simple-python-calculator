Tanya =input("Cek Bilangan,Kalkulator, Atau Keluar A/B/C").upper()
if Tanya not in ('A' and 'B' and 'C') :
    print ("Masukan Pilihan Yang Benar")
if Tanya == 'C' :
    print("Silakan Pencet Enter Untuk Keluar")
if Tanya == 'A' :
  Bilangan = int(input("Masukan Angka Bulat "))
  if Bilangan % 2 == 0 :
    print("Genap")
  else :
    print ("Ganjil")
    
if Tanya == 'B' :   
  Angka_1=float(input("Masukan Angka Pertama "))
  Operator=input("Masukan Operator (+,-,*,/,) ")
  Angka_2=float(input("Masukan Angka Kedua "))
  
  if Operator not in ("+","-","*","/") :
      print ("Tolong Masukan Operator Yang Benar") 

  if Operator == '+' :
      hasil = Angka_1 + Angka_2
      print (f" {Angka_1} + {Angka_2} {"="} {hasil}")
  if Operator == '-' :
      hasil = Angka_1 - Angka_2
      print (f" {Angka_1} - {Angka_2} {"="} {hasil}")
  if Operator == '*' :
      hasil = Angka_1 * Angka_2
      print (f" {Angka_1} * {Angka_2} {"="} {hasil}")
  if Operator == '/' :
      hasil = Angka_1 / Angka_2
      print (f" {Angka_1} / {Angka_2} {"="} {hasil}")
      
    
    