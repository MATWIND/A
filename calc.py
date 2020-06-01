# Kaluklator Multifungsi

import os

os.system('clear')
print "======================================="
print "= Created: MATWIND-OFFICIAL           ="
print "= Youtube: Telor Studio               ="
print "= Kind   : Kalkulator                 ="
print "= Github : https://github.com/MATWIND ="
print "======================================="
print " "

def lagi():
    print "============== MULAI ==============="
    a = int(input('Masukan angka pertama: '))
    b = int(input('Masukan angka kedua  : '))
    print "Anda memasukan angka :",a,"dan",b
    print "============= HASILNYA ============="
    print " "
    c = a + b
    print "[+]  ditambah     =",c
    c = a - b
    print "[-]  dikurang     =",c
    c = a * b
    print "[*]  dikali       =",c
    c = a / b
    print "[/]  dibagi       =",c
    c = a % b
    print "[%]  dibulatkan   =",c
    c = a // b
    print "[//] sisa bagi    =",c
    c = a ** b
    print "[**] dipangkatkan =",c
    print " "
    print "============= SELESAI =============="
    print " "
    print " "

if __name__ == "__main__":
    
    while(True):
        lagi()