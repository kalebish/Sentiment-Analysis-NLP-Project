import joblib
import pandas as pd

# Save the model
joblib.dump(model, 'sentiment_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

# Load the model for deployment
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict_sentiment(review):
    cleaned_review = preprocess_text(review)
    features = vectorizer.transform([cleaned_review]).toarray()
    prediction = model.predict(features)
    return prediction[0]

# Example usage
print(predict_sentiment("This product is great!"))
