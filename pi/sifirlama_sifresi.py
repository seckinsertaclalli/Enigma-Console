#Cihaz şifresi üretici,
#setting ekranının sağ alt taraftaki değerler ile aynı ekranın sol alttaki değerlerin farkının mutlak değerini
#aşağıdaki fonksiyona girdi olarak gönderirseniz, fonksiyonun çıktısı cihazın kendisi özgü sıfırlama şifresidir.
from sys import exit
def modify_integer(input_integer):
    str_input = str(input_integer)
    modified_list = [str(int(char) + 9) for char in str_input]
    for i in range(len(modified_list)):
        if int(modified_list[i]) > 9:
            carry, remainder = divmod(int(modified_list[i]), 10)
            modified_list[i] = str(remainder)
            if i + 1 < len(modified_list):
                modified_list[i + 1] = str(int(modified_list[i + 1]) + carry)
            else:
                modified_list.append(str(carry))
    result_string = ''.join(modified_list)
    return result_string
try:
    while True:
        sol_alt_kose=input("Settings Ekrani Sol Alt Kosedeki Degeri Giriniz: ")
        sag_alt_kose=input("Settings Ekrani Sag Alt Kosedeki Degeri Giriniz: ")
        sonuc=modify_integer(abs(int(sol_alt_kose)-int(sag_alt_kose)))
        print("Sifirlama Sifresi:",sonuc)
        key=input("Cikis icin q tekrar için 1 : ")
        if key=="q":
            exit()
        elif key == "1":
            continue
except Exception as e:
    print("Hata:",e)
    key=input("Cikis icin herhangibir tus")
    exit()
    
