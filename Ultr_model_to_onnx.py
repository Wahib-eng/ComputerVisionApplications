from ultralytics import YOLO

model = YOLO(r'C:\Users\intern.rd\OneDrive - BIZE PROJE GELISTIRME A.S\Desktop\Projects\models\best_600_24_10.pt')

# Export the model
model.export(format="onnx") #could be converted to tflite (tensorflow lite) or any extention

