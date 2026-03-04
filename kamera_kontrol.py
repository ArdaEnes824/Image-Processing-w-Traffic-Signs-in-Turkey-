import cv2

def test_camera():
    print("--- KAMERA TARAMASI BAŞLIYOR ---")

    
    print("Deneme 1: Kamera Index 0 deneniyor...")
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened() or not cap.read()[0]:
        print(" Index 0 başarısız. Index 1 deneniyor...")
        cap.release()
        
        
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        
        if not cap.isOpened() or not cap.read()[0]:
            print("Index 1 de başarısız!")
            print("\nÇÖZÜM ÖNERİLERİ:")
            print("1. Başlat > 'Kamera Gizlilik Ayarları' > Masaüstü uygulamalarına izin ver.")
            print("2. Başka bir uygulama (Zoom, Discord) kamerayı kullanıyor mu?")
            return
        else:
            print("✅ BAŞARILI: Kamera Index 1'de bulundu!")
            secilen_index = 1
    else:
        print("✅ BAŞARILI: Kamera Index 0'da bulundu!")
        secilen_index = 0

    
    print(f"\nKamera açılıyor... (Index: {secilen_index})")
    print("Çıkmak için 'q' tuşuna bas.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Görüntü koptu!")
            break

        cv2.imshow(f"Kamera Test (Index {secilen_index})", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    test_camera()