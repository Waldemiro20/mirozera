from textblob import TextBlob

# Função para obter resposta simples com base em palavras-chave
def get_response(user_input):
    # Criando um objeto TextBlob para processar a entrada do usuário
    blob = TextBlob(user_input)

    # Análise de sentimento: podemos responder de acordo com o sentimento da mensagem
    sentiment = blob.sentiment.polarity

    
    if 'olá' in user_input.lower() or 'oi' in user_input.lower():
        return "Olá! Como posso ajudar você hoje?"
    elif 'como você está' in user_input.lower():
        return "Eu estou bem, obrigado por perguntar!"
    elif 'tchau' in user_input.lower():
        return "Tchau! Foi bom conversar com você!"
    elif 'sentimento' in user_input.lower():
        if sentiment > 0:
            return "Parece que você está de bom humor!"
        elif sentiment < 0:
            return "Parece que você está triste, como posso ajudar?"
        else:
            return "Estou sentindo uma vibe neutra da sua mensagem."
    elif 'corrigir' in user_input.lower():
        corrected_input = blob.correct()
        return f"Eu corrigi sua frase: {corrected_input}"
    else:
        return "Desculpe, não entendi. Pode reformular sua pergunta?"

# Função principal para interação
def chatbot():
    print("Olá! Sou seu chatbot. Digite 'tchau' para encerrar.")
    
    while True:
        user_input = input("Você: ")
        
        # Encerra a conversa se o usuário digitar 'tchau'ola
        if user_input.lower() == 'tchau':
            print("Chatbot: Tchau! Até logo!")
            break
        
        # Resposta do chatbot
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Executando o chatbot
if __name__ == "__main__":
    chatbot()