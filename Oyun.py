import random
class Warrior():
    Health=100
    damage=random.randint(1,20)
class Beast():
    Health=200
    damage=random.randint(1,10)
i=0
def oyna(oyuncununcanı,rakibincanı):
    kalancan1=rakibincanı
    kalancan2=oyuncununcanı
    while True:
        print("\n\n\n")
        print("""Kalan canlar
                        sizin canınız {}
                        Rakibin cani {}
                        """.format(kalancan2, kalancan1))
        print("Saldırıyorsunuz")
        saldır=input("Saldırınızı yapmak icin herhangi bir tusa basın:")
        damage1 = random.randint(5, 20)
        print("Vurduğunuz hasar {}".format(damage1))
        kalancan1-=damage1
        print("Rakibin sırası")
        savun=input("Savunmak icin herhangi bir tusa basın:")
        damage2 = random.randint(1, 10)
        print("Yenilen hasar {}".format(damage2))
        kalancan2-=damage2
        if kalancan1>kalancan2:
            if kalancan2 <= 0:
                print("Kaybettiniz.")
                break
            elif kalancan1<=0:
                print("Kaznadınız.")
                break
        elif kalancan2>kalancan1:
            if kalancan1 <= 0:
                print("Kazandiniz.")

                break
            elif kalancan2<=0:
                print("Kaybettiniz.")
                break
while 1:
    print("""
    Oyuna hosgeldiniz 
    Oyuna baslamak icin 1'e
    Oyundan cıkmak icin 0'a basınız
    """)
    secim = int(input("Seciminizi yapın:"))
    if secim==1:
        oyna(Warrior.Health,Beast.Health)
        break
    elif secim==0:
        break
    else:
        print("yanlıs tuslama yaptınız yeniden secin:")


