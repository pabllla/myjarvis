import requests
import pyttsx3

def google_search(query, api_key, cse_id):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}"
    response = requests.get(url)
    return response.json()

api_key = "AIzaSyDFUhb3Mr5vEIEPa9AfqO7khVO1mvp8khY"
cse_id = "731ef735025184a2c"  # Это идентификатор вашего пользовательского поиска

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def search_google(query):
    results = google_search(query, api_key, cse_id)

    # Обработка результатов
    if 'items' in results:
        speak(f"Вот результаты поиска по запросу '{query}'")
        for i, item in enumerate(results['items'], start=1):
            title = item['title']
            link = item['link']
            speak(f"{i}. {title}")
            print(f"{i}. {title} - {link}")  # Можно оставить для отображения в консоли
    else:
        speak("")

# Пример использования
query = ""
search_google(query)
