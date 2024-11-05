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
    print(f"Error: {e}", file=sys.stderr)  # Print errors to stderr
    # Handle the error as needed (e.g., exit with a non-zero code)
    sys.exit(1)
