import base64
import re

def is_base64_encoded(text):
    base64_pattern = r'^[A-Za-z0-9+/=]+\Z'
    return bool(re.fullmatch(base64_pattern, text))

def detect_encrypted_text(text):
    try:
        if is_base64_encoded(text):
            base64.b64decode(text)
            return "✅ النص يبدو أنه مشفّر بـ Base64."
        else:
            return "ℹ️ النص لا يبدو مشفرًا بـ Base64."
    except Exception:
        return "⚠️ لم يتم التعرف على نوع التشفير أو فشل في التحليل."

if __name__ == "__main__":
    input_text = input("🔍 أدخل النص لتحليله: ")
    result = detect_encrypted_text(input_text)
    print(result)
