def read_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("File tidak ditemukan, mohon cek kembali.")
        return None

def find_text(artikel, kata):
    kata_list = artikel.lower().split()
    return kata_list.count(kata.lower())

def replace_text(artikel, kata_asli, kata_baru):
    if kata_asli in artikel:
        return artikel.replace(kata_asli, kata_baru)
    else:
        print(f"Kata '{kata_asli}' ini tidak ditemukan")
        return artikel

def sort_text(artikel):
    kata_list = artikel.lower().split()
    kata_set = set(kata_list)
    return sorted(kata_set)

file_path = "artikel.txt"

artikel = read_txt(file_path)

if artikel:
    kata_dicari = input("\nPencarian kata: ")
    jumlah_kata = find_text(artikel, kata_dicari)
    print(f"\nKata '{kata_dicari}' ini ditemukan sebanyak: {jumlah_kata}")

    kata_asli = input("\nKata yg akan diganti: ")
    kata_baru = input("Kata pengganti: ")
    artikel_baru = replace_text(artikel, kata_asli, kata_baru)
    print("\nSetelah Dilakukan Penggantian Kata")
    print(artikel_baru) 

    with open("new_artikel.txt", 'w', encoding='utf-8') as file:
        file.write(artikel_baru)
    print("\nArtikel yg sudah direplace juga dapat dibuka pada file new_artikel.txt")

    kata_terurut = sort_text(artikel)
    print("\nBerikut Kata Terurut Berdasarkan Abjad :")
    print(kata_terurut)
