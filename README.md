# Generador de Historias con IA

Este proyecto utiliza la API de Qwen_Qwen2.5-1.5B-Instruct para generar historias personalizadas basadas en las entradas del usuario. Los usuarios pueden especificar los nombres de los personajes, el lugar donde transcurre la historia, la acción principal y el nivel de creatividad deseado.

## Requisitos

- Python 3.x
- Biblioteca `requests`

1. Clona este repositorio:
    ```bash
    git clone https://github.com/Darniekop/generador-historias-ia.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd generador-historias-ia
    ```
3. Instala las dependencias necesarias:
    ```bash
    pip install requests
    ```

## Uso

Ejecuta el script principal para comenzar a generar historias:

```bash
python chat.py
```

El script pedirá al usuario que ingrese los siguientes datos:

 - Nombre del protagonista
 - Nombre del coprotagonista
 - Lugar donde transcurre la historia
 - Acción principal de la historia
 - Nivel de creatividad (0 a 1)
 - El script enviará estos datos a la API de OpenAI y mostrará la historia generada en la consola.

### Ejemplo:

 - Escribe el nombre del protagonista: Dario
 - Escribe el nombre del coprotagonista: David
 - Escribe el nombre del lugar donde transcurre la historia: Lake
 - Acción que debe transcurrir: Fight
 - Nivel de creatividad (0 a 1): 0.8


<img width="795" alt="Captura de pantalla 2024-12-01 200715" src="https://github.com/user-attachments/assets/022510b8-ff76-49a3-8654-21f7820ddc26">


# Realización del proyecto

## Instalación

1. Instalar el servidor de Text Generation WebUI
Clona el repositorio de Text Generation WebUI:

  ```bash
  git clone https://github.com/oobabooga/text-generation-webui
  cd text-generation-webui
  ```

Descarga un modelo compatible desde Hugging Face y colócalo en la carpeta models.
En este caso estamos usando el modelo ```Qwen_Qwen2.5-1.5B-Instruct```, que es el que mejor ha funcionado se ha intentado realizar el proyecto con otros modelos como ```EleutherAI_gpt-neo-1.3B``` o ```meta-llama_Llama-3.2-1B``` pero los resultados han sido muy poco acertados o directamente no ha sido posible ejecutar este modelo por permisos o tiempo de espera.

## Realizamos el script en chat.py

Creamos un script que pida al usuario los siguientes datos:
 - Nombre del personaje principal
 - Nombre del personaje secundario
 - Lugar donde transcurre el relato
 - Una acción importante que debe acontecer en la historia

 Otro punto importante que dejamos modificar al usuario es la temperatura (de 0 a 1), esta característica influye en lo creativa que será nuestra historia, a continuanción vamos a ver las diferencias entre una historia muy creativa y otra nada creativa.

### Historia con temperatura = 1

<img width="793" alt="Captura de pantalla 2024-12-01 202200" src="https://github.com/user-attachments/assets/73b744cb-025a-4a32-a3cf-10a5809b1b68">

### Historia con temperatura = 0

<img width="794" alt="Captura de pantalla 2024-12-01 202856" src="https://github.com/user-attachments/assets/41f647cd-daa5-4b44-8878-eb75d41b2ff8">

# Conclusiones

EL modelo utilizado consigue buenos resultados aunque tiene algunos problemas tras varios intentos y la velocidad de ejecución no es la más rápida. Sería conveniente usar nuevos modelos más pesado y complejos para poder conseguir historias con más sentido y mejor narradas.
