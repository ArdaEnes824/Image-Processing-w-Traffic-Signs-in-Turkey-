import cv2
from ultralytics import YOLO


model = YOLO("runs/detect/teknofest_kusursuz_final/weights/best.pt")

cap = cv2.VideoCapture(0)
print("Kamera açılıyor... Çıkmak için 'q' tuşuna bas kanka!")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Kamera okunamadı!")
        break

    # Modeli çalıştır
    # conf=0.50: %50 altı ihtimalleri eler
    # iou=0.45: Aynı tabelaya üst üste 2 kutu çizmeyi engeller 
    results = model.predict(frame, conf=0.50, iou=0.45, verbose=False)

    # 3. Modelin çizdiği kutuları görüntünün üstüne yapıştır
    annotated_frame = results[0].plot()


    # O an ekranda tespit edilen tüm tabelaları bu listede toplanır
    okunan_tabelalar = []

    # Ekranda bulunan her bir kutu (tabela) için döngüye gir:
    for box in results[0].boxes:
        # Tarafından bulunan tabelanın Sınıf ID'sini (0, 1, 5 vb.) al
        class_id = int(box.cls[0].item())
        
        # O ID'nin gerçek ismini (örn: "road_work", "stop") öğren
        sinif_ismi = model.names[class_id]
        
        # Modelin bu tabeladan yüzde kaç emin olduğunu alır
        skor = int(box.conf[0].item() * 100)
        
        # Listeye ekle
        okunan_tabelalar.append(f"{sinif_ismi} (%{skor})")

    # 4. Eğer ekranda tabela gördüyse, terminale yazdır
    if len(okunan_tabelalar) > 0:
        print(f"Hedefler Tespit Edildi: {', '.join(okunan_tabelalar)}")
        

    # 5. Görüntüyü ekrana ver
    cv2.imshow("Teknofest Araci Gozu", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()