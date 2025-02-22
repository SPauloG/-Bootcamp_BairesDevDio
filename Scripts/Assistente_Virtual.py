import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser

# Inicializar o reconhecedor de fala
recognizer = sr.Recognizer()

# Inicializar o engine de texto para fala
engine = pyttsx3.init()

def text_to_speech(text):
    """Módulo para transformação de texto em áudio"""
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    """Módulo para transformação de fala em texto"""
    with sr.Microphone() as source:
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='pt-BR')
            print("Você disse: " + text)
            return text
        except sr.UnknownValueError:
            print("Não entendi o que você disse")
            return ""
        except sr.RequestError as e:
            print("Não foi possível obter resultados; {0}".format(e))
            return ""

def search_wikipedia(query):
    """Função para pesquisar no Wikipedia"""
    wikipedia.set_lang("pt")
    try:
        result = wikipedia.summary(query, sentences=2)
        text_to_speech("Aqui está o que encontrei no Wikipedia:")
        text_to_speech(result)
    except wikipedia.exceptions.DisambiguationError:
        text_to_speech("Há múltiplos resultados para essa pesquisa. Por favor, seja mais específico.")
    except wikipedia.exceptions.PageError:
        text_to_speech("Desculpe, não encontrei nenhuma informação sobre isso no Wikipedia.")

def open_youtube():
    """Função para abrir o YouTube"""
    webbrowser.open("https://www.youtube.com")
    text_to_speech("Abrindo o YouTube")

def main():
    text_to_speech("Olá! Eu sou sua assistente virtual. Como posso ajudar?")
    
    while True:
        command = speech_to_text().lower()
        
        if "wikipedia" in command:
            text_to_speech("O que você gostaria de pesquisar no Wikipedia?")
            query = speech_to_text()
            search_wikipedia(query)
        
        elif "youtube" in command:
            open_youtube()
        
        elif "sair" in command or "encerrar" in command:
            text_to_speech("Até logo!")
            break
        
        else:
            text_to_speech("Desculpe, não entendi o comando. Pode repetir, por favor?")

if __name__ == "__main__":
    main()
