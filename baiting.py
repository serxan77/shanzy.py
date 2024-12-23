import os

def create_bait_file():
    # Yalançı faylın adı və növü
    bait_file = "malicious_software.exe"
    
    # Faylın yaradılması (sadəcə nümunə məqsədli)
    with open(bait_file, 'w') as file:
        file.write("Malicious content inside!")

    print(f"Yalançı fayl yaradıldı: {bait_file}")

# İstifadə:
create_bait_file()
