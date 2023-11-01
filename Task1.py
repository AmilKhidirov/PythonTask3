daxil_edin = int(input("""Daxil Edin:
Vurma (1) , Çıxma 2() , Toplama (3) , Bölmə (4)
"""))


reqem1 = int(input('Reqem daxil edin: '))
reqem2 = int(input('Reqem daxil edin: '))





def acts():

    if daxil_edin == 1:
        cavab = reqem1 * reqem2
        print(cavab)

    elif daxil_edin == 2:
        cavab = reqem1 - reqem2
        print(cavab)

    elif daxil_edin == 3:
        cavab = reqem1 + reqem2
        print(cavab)

    elif daxil_edin == 4:
        try:
            print(reqem1 / reqem2)
        except ZeroDivisionError:
            print('0-a bölmə yoxdur!')






acts()