import sys
import joblib

# Load model
model = joblib.load("spam_detector_model.pkl")

# Process input
comment_text = sys.argv[1]

# Predict
is_spam = model.predict([comment_text])[0]

# Output result
with open("is_spam_output.json", "w") as f:
    f.write(f'{{"is_spam": {is_spam}}}')
print(f'Output written: {{"is_spam": {is_spam}}}')  # Add this line for debugging
