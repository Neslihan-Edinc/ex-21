import random  # rastgele karakter seçmek icin random modulu

def random_char():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    characters = lower + upper + digits
    return random.choice(characters)  # random.choice ile rastgele karakter seçiyoruz

def generate_random_password(length):
    password_list = []
    for _ in range(length): #range=count-1 e kadar islem yapar
        # '_' kodun daha temiz okumabilmesini sağlar
        password_list.append(random_char())  # random_char fonksiyonunu çağır
    return ''.join(password_list)  # Listeyi birleştirerek string oluştur

length = int(input("Enter a desired password length: "))
password = generate_random_password(length)  # Uzunluğu doğru yazdık
print("Generated password:", password)







