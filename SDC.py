import joblib

# Load model
model = joblib.load("SDC_pipeline.pkl")

print("========Security Description Classifier========")
print("Type 'exit' to quit.\n")

while True:
    desc = input("Enter eyewitness description: ")
    if desc.lower() in ["exit", "quit", "q"]:
        print("Thankyou...")
        break
    
    pred = model.predict([desc])[0]
    print(f"Predicted Priority: {pred}\n")
