import requests
import openai

OPENAI_API_KEY = "your_openai_api_key_here"

def get_website_data(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.text if response.status_code == 200 else None

def analyze_traffic(html_content):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Analyze website traffic patterns based on HTML content."},
                  {"role": "user", "content": html_content}]
    )
    return response["choices"][0]["message"]["content"].strip()

if __name__ == "__main__":
    url = input("Enter website URL: ")
    html_content = get_website_data(url)
    if html_content:
        analysis = analyze_traffic(html_content)
        print("AI Traffic Analysis:", analysis)
    else:
        print("Failed to fetch website data.")