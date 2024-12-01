import requests

url = "http://127.0.0.1:5000/v1/completions"
headers = {"Content-type": "application/json"}

while True:
    # Pedir al usuario el tipo de historia que quiere
    character_name1 = input("Escribe el nombre del protagonista: ")
    character_name2 = input("Escribe el nombre del coprotagonista: ")
    place = input("Escribe el nombre del lugar donde transcurre la historia: ")
    action = input("Acción que debe transcurrir: ")
    a = 1
    while a == 1:
        try:
            temperatura = float(input("Nivel de creatividad (0 a 1): "))
            if temperatura > 1 or temperatura < 0:
                print("Escribe una temperatura entre 0 y 1")
            else:
                a = 0  # Sale del bucle si la temperatura es válida
        except ValueError:
            print("Escribe una temperatura entre 0 y 1")

    # Crear un prompt que guíe a la IA a generar una historia
    prompt = f"Create a detailed and coherent story with {character_name1} as the protagonist and {character_name2} as a secondary character. The story takes place in {place} and involves {action}. Ensure the story has a clear beginning, middle, and a closed ending, and includes a title."

    body = {
        "prompt": prompt,
        "max_tokens": 500,  # Aumentar el número de tokens para una historia más larga
        "temperature": temperatura,  # Controla la creatividad
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0
    }

    # Enviar la solicitud
    response = requests.post(url=url, headers=headers, json=body)
    
    # Visualizar el resultado
    if response.status_code == 200:
        result = response.json()
        print("Historia generada:")
        print(result['choices'][0]['text'])
    else:
        print("Error:", response.status_code, response.text)
