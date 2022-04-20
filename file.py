import os
import time
import sys
import smtplib
from datetime import datetime

IncarterMenu = """


██╗███╗   ██╗ ██████╗ █████╗ ██████╗ ████████╗███████╗██████╗ 
██║████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║██╔██╗ ██║██║     ███████║██████╔╝   ██║   █████╗  ██████╔╝
██║██║╚██╗██║██║     ██╔══██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
██║██║ ╚████║╚██████╗██║  ██║██║  ██║   ██║   ███████╗██║  ██║
╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                              
 - 1 - PARA YATIRMA   
 - 2 - PARA ÇEKME
 - 3 - PARA GONDERME
 - 4 - HESAP HAREKETLERİ
 - 5 - HESAP BİLGİLERİ
 - 0 - KART İADE

"""
paraYatir = """
        
        +]+]+] PARA YATIR [+[+[+

    - 1 - Kendi Hesabıma
    - 2 - Farklı Hesap
    - 3 - Ana Menü
    - 4 - İptal
"""
ParagonderMenu = """

    +]+]+] Gönderim Tipi +[+[+[+
        
       - 1 - Iban
       - 2 - Hesap No
       - 3 - İptal

"""
paraCekMenu = """


        +]+]+] PARA CEKME MENUSU [+[+[+
                                  
       - 1 -    : 20
       - 2 -    : 50
       - 3 -    : 100
       - 4 -    : 200
       - 5 -    : 500
       - 0 -   : Custom

"""
class IncarterBank:
    PASSWORD = 1234
    denemeHakki= 0
    BAKIYE = 0
    kart_Sahibi = "İbrahim Ulusal"
    kart_iban = "TR 12 5636 6762 7872 7872 42"
    kart_hesap_no  = "2367 6732 67236 8723"
    fast_komisyon = 1.80
    def __init__(self):
        try:
            while True:
                
                self.password = int(input('Password : '))
                if len(str(self.password)) < 4 or len(str(self.password)) > 4:
                    print('Şifreniz 4 Haneli Olmalıdır.')
                    continue
                if self.password != self.PASSWORD :
                    self.denemeHakki +=1
                    print(f'Kalan Hakkınız : {4 - self.denemeHakki}')
                    if self.denemeHakki == 4:
                        print("Kartınız Bloke Oluyor",end="")
                        for i in range(3):
                            print('.',end="")
                            time.sleep(2)
                        sys.exit()
                        break
                else:
                    try:
                        print(IncarterMenu)
                        while True:
                            self.menu = int(input('Lütfen Yapmak İstediğiniz İşlemi Seçin : '))
                            if len(str(self.menu)) > 1:
                                print('Böyle Bir Menü Seçeneği Yok .')
                                continue
                            if self.menu == 0:
                                # print('Lütfen Kartınızı Unutmayın !')
                                # print('Çıkış Yapılıyor',end="")
                                # for i in range(3):
                                #     print('.',end="")
                                #     time.sleep(2)
                                self.Exit()
                            elif self.menu == 1:
                                self.ParaYatir()
                                break
                            elif self.menu == 2:
                                self.ParaCek()
                            elif self.menu == 3:
                                self.ParaGonder()
                            elif self.menu == 4:
                                self.HesapHareketleri()
                            else:
                                self.HesapBilgileri()
                        break
                    except ValueError:
                        print('Bu Alan Boş Bırakılamaz ve Metinsel İfade Girilemez..')
                        print('Lütfen Programı Tekrar Çalıştırın')
                    except KeyboardInterrupt:
                        print('CTRL + C Tespit Edildi...')
                        time.sleep(2)
                        sys.exit()
                    except Exception as e:
                        print(f'Bilinmeyen Bir Hata Oluştu.\nHata Türü : {e}')
                        time.sleep(2)
                        sys.exit()
        except ValueError:
            print('Bu Alan Boş Bırakılamaz ve Metinsel İfade Girilemez..')
            print('Lütfen Programı Tekrar Çalıştırın')
        except KeyboardInterrupt:
            print('CTRL + C Tespit Edildi...')
            time.sleep(2)
            sys.exit()
        except Exception as e:
            print(f'Bilinmeyen Bir Hata Oluştu.\nHata Türü : {e}')
            time.sleep(2)
            sys.exit()
    def ParaCek(self):
        try:
            print(paraCekMenu)
            print(f'Bakiye : {self.BAKIYE}')
            
            while True:
                self.paraCek = int(input('Çekmek İstediğiniz Miktarı Gİriniz : '))
                if self.paraCek< 0 :
                    print('Lütfen Sıfırdan Büyük Bir DEğer Giriniz....')
                    continue
                if self.paraCek  == 1:
                    self.BAKIYE -= 20
                elif self.paraCek == 2:
                    self.BAKIYE -= 50
                elif self.paraCek == 3:
                    self.BAKIYE -= 100
                elif self.paraCek == 4:
                    self.BAKIYE -= 200
                elif self.paraCek == 5:
                    self.BAKIYE -= 500
                else:
                    try:
                        while True:    
                            self.Miktar = int(input('Çekmek İstediğiniz Miktaru Giriniz : '))
                            if self.Miktar < 0:
                                print('Lütfen 0 dan Büyük Bİr Değer Giriniz : ')
                                continue
                            if self.Miktar > self.BAKIYE:
                                print('Yetersiz Bakiye...')
                                break
                            else:
                                self.BAKIYE -= self.Miktar
                    except ValueError:
                        print('Bu Alan Boş Bırakılamaz ve Metinsel İfade Girilemez..')
                        print('Lütfen Programı Tekrar Çalıştırın')
                    except KeyboardInterrupt:
                        print('CTRL + C Tespit Edildi...')
                        time.sleep(2)
                        sys.exit()
                    except Exception as e:
                        print(f'Bilinmeyen Bir Hata Oluştu.\nHata Türü : {e}')
                        time.sleep(2)
                        sys.exit()
                break
        except ValueError:
            print('Bu Alan Boş Bırakılamaz ve Metinsel İfade Girilemez..')
            print('Lütfen Programı Tekrar Çalıştırın')
        except KeyboardInterrupt:
            print('CTRL + C Tespit Edildi...')
            time.sleep(2)
            sys.exit()
        except Exception as e:
            print(f'Bilinmeyen Bir Hata Oluştu.\nHata Türü : {e}')
            time.sleep(2)
            sys.exit()
    def ParaYatir(self):
        try:
            print(paraYatir)
            while True:
                self.ParaYatirMenuItem = int(input('İşleminizi Seçiniz : '))
                if self.ParaYatirMenuItem < 0 or self.ParaYatirMenuItem > 4:
                    print('Böyle Bir İşlem Numarası Yok Lüften Doğru Giriniz...')
                    continue
                if self.ParaYatirMenuItem == 1:
                    try:
                        while True:
                            self.kendiHesapYatir = int(input('Yatırılacak Miktarı Giriniz : '))
                            if self.kendiHesapYatir < 0:
                                self.EkraniTemizle()
                                print('Lütfen Sıfırdan Büyük Bir Miktar Yatırınız ...')
                                continue
                            else:
                                self.BAKIYE += self.kendiHesapYatir
                                print(self.BAKIYE)
                                break
                    except ValueError:
                        print('Bu Alan Boş Bırakılamaz ve Metinsel İfade Girilemez..')
                        print('Lütfen Programı Tekrar Çalıştırın')
                    except KeyboardInterrupt:
                        print('CTRL + C Tespit Edildi...')
                        time.sleep(2)
                        sys.exit()
                    except Exception as e:
                        print(f'Bilinmeyen Bir Hata Oluştu.\nHata Türü : {e}')
                        time.sleep(2)
                        sys.exit()
             
                elif self.ParaYatirMenuItem == 2:
                    self.EkraniTemizle()
                    try:
                        
                        while True:
                            self.AliciIsim = str(input('Alıcı İsim Soyisim : '))
                            print(ParagonderMenu)
                            self.gonderimtipi = int(input('Gönderim Tipini Seçiniz : '))
                            if self.gonderimtipi < 0 or self.gonderimtipi > 3:
                                print('Yanlış Değer Girdiniz ...')
                                continue
                            if self.gonderimtipi == 1:
                                break
                            elif self.gonderimtipi == 2:
                                pass
                            else:
                                pass
                    except Exception as e:
                        print(f'Error type : {e}')
                        time.sleep(2)
                        sys.exit()
                    except ValueError:
                        print('Bu alan Boş Bırakılamaz ve Metinsel İfade Girilemez.')
                    except KeyboardInterrupt:
                        print('CTRL + C Tespit Edildi')
                        self.Exit()
                elif self.ParaYatirMenuItem == 3:
                    self.__init__()
                else:
                    self.Exit()
        except ValueError:
            print('Bu Alan Boş Bırakılamaz ve Metinsel İfade Girilemez..')
            print('Lütfen Programı Tekrar Çalıştırın')
        except KeyboardInterrupt:
            print('CTRL + C Tespit Edildi...')
            time.sleep(2)
            sys.exit()
        except Exception as e:
            print(f'Bilinmeyen Bir Hata Oluştu.\nHata Türü : {e}')
            time.sleep(2)
            sys.exit()
    def HesapBilgileri(self):
        hesap_bilgi = f"""
        
            Kart Sahibi : {self.kart_Sahibi}
            Iban No     : {self.kart_iban}
            Hesap No    : {self.kart_hesap_no}
            Bakiye      : {self.BAKIYE}
        """
        print(hesap_bilgi)
    def ParaGonder(self):
        pass
    def HesapHareketleri(self):
        pass
    def EkraniTemizle(self):
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        else:
            pass
    def DekontMailSend(self):
        try:    
            self.mailServerConnect = smtplib.SMTP()
            self.mailServerConnect.ehlo()
            self.mailServerConnect.starttls()
            self.mailServerConnect.login(None, None)
            self.mailServerConnect.sendmail(None, None, None)
            self.mailServerConnect.close()
        except Exception as e:
            print(f'Bir Hata Oluştu \n Hata Türü : {e}')
            time.sleep(2)
            sys.exit()
    def Exit(self):
        string = "Çıkış Yapılıyor"
        list = []
        for x in string:
         list.append(x)
        
        while True:
            for x in range(len(list)):
             old = list[x]
             list[x] = old.upper()
             final = "".join(list)
             sys.stdout.write('\r')
             sys.stdout.write(final)
             sys.stdout.flush()
             list[x] = old
             time.sleep(0.1)
            time.sleep(1)
            self.EkraniTemizle()
            print('\n\nLütfen Kartınızı Almayı Unutmayınız!')
            sys.exit()
            break
    def dekont(self):
        dekont_file = f'''
<!doctype html>
<html lang="tr" dir="ltr">
	<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta name="description" content="" />
	<meta name="author" content="http://bootstraptaste.com" />
	<meta charset="utf-8">
    <link rel="stylesheet" href="css/style.css"/>
		<title>Incarter Bank</title>
	
	<head>
	<body>
		<main>
			
			<header>
				<h1>INCARTER BANK</h1>
			</header>
			<section id="content">
				<div class="box">
				
					<p>ŞUBE KODU       : </p>
					<p>IBAN		       : {self.kart_iban}</p>
					<p>HESAP NUMARASI  : {self.kart_hesap_no}</p>
					<p>VERGİ DAİRESİ   : </p>
					<p>VERGİ KİMLİK NO : </p>
					<p>İŞLEM TARİHİ    : {datetime.now()}</p>
					<p>VALÖR	       : </p>
					<p>İŞLEM YERİ      : {os.name()}</p>
				</div>
				<div class="box">

					<p>SAYIN</p>
					<p>{self.kart_Sahibi}</p>					
					<p>BELEDİYE EVLERİ MAHALLESİ 
					ŞEHİT ENDER MEHLİ SOKAK NO : 2</p>
				</div>
				<div id="contentFooter">

					<p>İBRAHİM ULUSAL</p>
					<p>Fast Mesaj Kodu : </p>	
					<p>Gönderen        : {self.kart_Sahibi} </p>
					<p>Alan Banka      : </p>
					<p>Alıcı Hesap     : </p>
					<p>İşlem Tutarı    : </p>
					<p>Komisyon        : </p>
					<p>Toplam Masraf   : </p>
				</div>
				<p>Hesabınızdan {self.Miktar} TL Çekilmiştir.
				   Tarih
				</p>
				<p>Taraflar arasında tüm uyuşmazlıklarda,Bankanın defter kayıtları ve belgeleri,
					müstenitli olsun olmasın,kesin ve aksi ileri sürülemez delil niteliğindedir.
					
					www.incarterbank.com
				</p>				
			</section>
			<footer>
				<p>&copy; 2021 Tüm Hakları Saklıdır.</p>
			</footer>
		</main>
	</body>
</html>

'''

if __name__ == '__main__':
    Incarter = IncarterBank()









