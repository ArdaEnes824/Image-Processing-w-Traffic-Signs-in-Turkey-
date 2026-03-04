from ultralytics import YOLO
import os

def main():
    #AYARLAR 
    #VERİ SETİNİN HARİTASI 
    yaml_dosyasi = "dataset/teknofest_final_dataset/data.yaml"

    #model ismi
    proje_ismi = "teknofest_kusursuz_final"


    #BAŞLANGIÇ KONTROLLERİ

    #Dosya yolunu tam yola çevirme (hata payını azaltması için)
    yaml_path = os.path.abspath(yaml_dosyasi)

    print(f"\n--- EĞİTİM BAŞLIYOR ---")
    print(f"Hedef Veri Seti: {yaml_path}")
    print("Model: YOLOv8 Nano\n") 

    model = YOLO('yolov8n.pt')

    model.train(
        data=yaml_path,   
        epochs=100,       
        imgsz=640,        
        batch=6,         
        name=proje_ismi,  
        device=0,         
        patience= 10,
        workers=0,
        fliplr=0.0,  
        flipud=0.0  
    )

    print("\n---EĞİTİM BİTTİ, MODEL DIŞARI AKTARILIYOR ---")
    succes = model.export(format = 'onnx', opset=11)
    print(f"ONNX Dönüşümü: {succes}")
    print(f"Artık 'runs/detect/{proje_ismi}/weights/best.pt' dosyasını alabilirsin!")
if __name__ == '__main__':
    main()