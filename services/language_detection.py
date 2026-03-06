from langdetect import detect

def detect_language(text):
    lang = detect(text)

    if lang == "hi":
        return "Hindi"
    elif lang == "ta":
        return "Tamil"
    else:
        return "English"