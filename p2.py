import speech_recognition as sr
from googletrans import Translator
import pyttsx3

selected_language = 'af'

def select_target_lang():
    # Language codes and names
    languages = {
        "af": "African",
        "am": "Amharic",
        "ar": "Arabic",
        "eu": "Basque",
        "bn": "Bengali",
        "en-GB": "English (UK)",
        "pt-BR": "Portuguese (Brazil)",
        "bg": "Bulgarian",
        "ca": "Catalan",
        "chr": "Cherokee",
        "hr": "Croatian",
        "cs": "Czech",
        "da": "Danish",
        "nl": "Dutch",
        "en": "English (US)",
        "et": "Estonian",
        "fil": "Filipino",
        "fi": "Finnish",
        "fr": "French",
        "de": "German",
        "el": "Greek",
        "gu": "Gujarati",
        "iw": "Hebrew",
        "hi": "Hindi",
        "hu": "Hungarian",
        "is": "Icelandic",
        "id": "Indonesian",
        "it": "Italian",
        "ja": "Japanese",
        "kn": "Kannada",
        "ko": "Korean",
        "lv": "Latvian",
        "lt": "Lithuanian",
        "ms": "Malay",
        "ml": "Malayalam",
        "mr": "Marathi",
        "no": "Norwegian",
        "pl": "Polish",
        "pt-PT": "Portuguese (Portugal)",
        "ro": "Romanian",
        "ru": "Russian",
        "sr": "Serbian",
        "zh-CN": "Chinese (PRC)",
        "sk": "Slovak",
        "sl": "Slovenian",
        "es": "Spanish",
        "sw": "Swahili",
        "sv": "Swedish",
        "ta": "Tamil",
        "te": "Telugu",
        "th": "Thai",
        "zh-TW": "Chinese (Taiwan)",
        "tr": "Turkish",
        "ur": "Urdu",
        "uk": "Ukrainian",
        "vi": "Vietnamese",
        "cy": "Welsh"
    }
    
    print("Select a language to translate to:")
    for code, name in languages.items():
        print(f"{name}: {code}")

    selected_language = input("Enter the language code: ").strip().lower()
    
    if selected_language not in languages:
        print("Invalid language code.")
        return

def translate_audio():
    recognizer = sr.Recognizer()
    translator = Translator()
    engine = pyttsx3.init()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        
        translated_text = translator.translate(text, dest=selected_language).text
        print("Translation:", translated_text)
        
        # Speak the translated text
        engine.say(translated_text)
        engine.runAndWait()
        
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    select_target_lang()
    while True:
        translate_audio()
