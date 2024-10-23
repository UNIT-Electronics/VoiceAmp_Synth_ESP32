import pyttsx3

def synthesize_voice(text, file_name):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.save_to_file(text, file_name)
    engine.runAndWait()
    print(f"Archivo de audio guardado como: {file_name}")

synthesize_voice("Hello World test 1 2 3 4 5 6", "file.wav")
