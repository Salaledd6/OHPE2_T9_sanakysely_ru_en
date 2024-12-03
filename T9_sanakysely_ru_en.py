import random
import json

def avaa_sanat(tiedostonimi:str): # avaa_sanat funktion toteutus
    tiedosto = open(tiedostonimi, "r")
    mjono = tiedosto.read()
    sanasto_dict = json.loads(mjono)
    tiedosto.close()
    return sanasto_dict

def sanakysely(sanasto:dict, kieli:str): # sanakysely funktion toteutus
    avaimet = list(sanasto.keys())
    oikeat = 0
    vaarat = 0

    for i in range(len(avaimet)):
        kysyttava_sana = random.choice(avaimet)
        vastattu_sana = input(f"Kirjoita '{kysyttava_sana}' {kieli} > ")

        if vastattu_sana == sanasto[kysyttava_sana]:
            oikeat += 1
            avaimet.remove(kysyttava_sana)
            print("Oikein meni!")
        else:
            vaarat += 1
            print("Yritä uudelleen")

    print(f"Oikeat vastaukset: {oikeat} Väärät vastaukset: {vaarat}")

def main(): # funktio main
    kielivalinta = int(input("Valitse kieli 1=ruotsi, 2=englanti >"))

    if kielivalinta == 1:
        sanasto = avaa_sanat("ruotsisanasto.json") # kutsutaan def avaa_sanat
        sanakysely(sanasto, "ruotsiksi") # kutsutaan def sanakysely
    else:
        sanasto = avaa_sanat("englantisanasto.json")
        sanakysely(sanasto, "englanniksi")

if __name__ == "__main__": #onko ohjelma käynnistetty tästä tiedostosta
    main() # kutsutaan funktio main