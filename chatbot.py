import openai

# API-Key
client = openai.OpenAI(api_key="") # "" <- dein eigenen API-Key einsetzen

# Hinweis zum beenden des Chatbots
print("Zum schließen des Chatbots, schreibe 'Beenden'\n")

# Initalisierung des Chatbots + Print-Befehl für Output
eingabe = None
while eingabe != "Beenden":
  eingabe = input("Eingabe: ")
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": eingabe}
    ]
  )
  print(f"Output: {response.choices[0].message.content}\n")