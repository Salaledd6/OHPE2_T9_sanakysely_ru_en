import T9_sanakysely_ru_en

def main():
    print("Tämä alkaa T9_main tiedostosta")
    print("Ruotsin sanojen kysely")

    sanat = T9_sanakysely_ru_en.avaa_sanat("ruotsisanasto.json")
    T9_sanakysely_ru_en.sanakysely(sanat, "ruattiksi")

if __name__=="__main__":
    main()