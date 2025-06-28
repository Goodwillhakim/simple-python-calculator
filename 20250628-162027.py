print("=" *32)
print("Kalkulator Sederhana Multifungsi")
print("=" *32)

angka_1= float(input("Masukan Angka 1 = "))
operator= input("operator (+,-,*,/) : ")
angka_2= float(input("Masukan Angka 2 = "))

if operator not in ["+","-","*","/"] :
   print("Tolong masukan operator yang benar")

if operator == "/" :
   hasil = angka_1 / angka_2
   print(f" {angka_1} / {angka_2}  {"="}  {hasil}")
 
if operator == "*" :
   hasil = angka_1 * angka_2
   print(f" {angka_1} * {angka_2}  {"="}  {hasil}")
 
if operator == "+" :
   hasil = angka_1 + angka_2
   print(f" {angka_1} + {angka_2}  {"="}  {hasil}")

if operator == "-" :
   hasil = angka_1 - angka_2
   print(f" {angka_1} - {angka_2}  {"="}  {hasil}")
    
