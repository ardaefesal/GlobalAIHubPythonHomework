print("Welcome to the game!")


print("Harfleri küçük harfle yazmalısın")
name=input("Plese enter your name:")

print(f"Hello {name}!")


kelime=["w e l c o m e"] 
import random as rnd
game=rnd.choice(kelime)
game=game.split(" ")
count=0
denemehakki=5
ayniharf=[]
letter=""


while True:

    letter=input("Harf giriniz:")
    if(letter in ayniharf):
        print("Daha önce bu harfi girdiniz")
        pass
    else:
        for a in range(0,len(game)):
            if letter==game[a]:
                ayniharf.append(letter)
                cnt=len(game)-1
                print(f" {letter} harfini buldun.Sırada {cnt} harf kaldı")
                count+=1
                while True:
                    try:
                        game.remove(letter)
                    except ValueError:
                        break
                break
        if(denemehakki <1):
            print("Game Over,Please Try Again")
            break

        if(count==0):
            denemehakki-=1
            print(f"Deneme hakkın {denemehakki} kaldı ")
        if(count>0 and denemehakki>0):
            count=0
        if(len(game)==0):
            print("Bravo,kazandın!")
            print("Kelimemiz:",kelime)
            break