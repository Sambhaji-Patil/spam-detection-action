# detect_spam.py
import sys
import json
import joblib

try:
    # Load model
    model = joblib.load("spam_detector_model.pkl")

    # Process input
    comment_text = sys.argv[1]

    # Predict
    is_spam = model.predict([comment_text])[0]

    # Output result as JSON to stdout
    result = {"is_spam": bool(is_spam)}
    print(json.dumps(result))

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)  # Log the error
    print(json.dumps({"is_spam": False}))   # Default to False in case of error
    sys.exit(1) # Indicate failure
