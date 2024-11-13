from ultralytics import YOLO

a = YOLO(r'C:\Users\intern.rd\OneDrive - BIZE PROJE GELISTIRME A.S\Desktop\Projects\models\best_600_24_10.pt')

# Export the model
a.export(format="onnx")
