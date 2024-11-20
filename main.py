from configuration import model

history = []


def start_chat():
    print("Conversa Iniciada")
    
    while True:

        user_input = input("Você: ")

        chat_session = model.start_chat(history=history)

        response = chat_session.send_message(user_input)

        model_response = response.text
        print(f"Resposta: {model_response}")
        print("")
        history.append({"role": "user", "parts": [user_input]})
        history.append({"role": "model", "parts": [model_response]})

start_chat()

