import telebot

CHAVE_API = '6789925207:AAGWEl8dbtY3-C-EO3-g9gJQURvYQozIuaI'

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["Parafuso"])
def parafuso(mensagem):
    bot.send_message(mensagem.chat.id, "Pedido de parafuso realizado com sucesso!")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Digite o nome do item que você deseja pedir:    
"""
    if mensagem.text.lower() == 'parafuso':
        parafuso(mensagem)
    bot.send_message(mensagem.chat.id, texto)


def handle_messages(mensagem):
    if mensagem.text.lower() == 'parafuso':
        parafuso(mensagem)
    else:
        bot.reply_to(mensagem, "Mensagem recebida!")

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    texto = """
    Digite o nome do item que você deseja verificar se há em estoque:    
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    texto = """
    Digite o nome do item que você deseja verificar o status do pedido:    
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["opcao4"])
def opcao4(mensagem):
    texto = """
    Aqui está a lista de itens disponíveis:
    - /Parafuso
    - Prego
    - Chave de fenda
    - Martelo
    - Alicate
    - Chave inglesa
    - Serrote
    - Trena

"""
    bot.send_message(mensagem.chat.id, texto)

def verify(msg):
    return True

@bot.message_handler(func=verify)
def answer(msg):

    texto = """
    Olá, eu sou o Bot do grupo BBB, o que você gostaria de fazer?
Escolha uma opção para continuar (Clique no item):

/opcao1 Fazer o pedido de um item
/opcao2 Verificar se há um item em estoque
/opcao3 Verificar o status de um pedido
/opcao4 Visualizar a lista de itens
"""

    bot.reply_to(msg, texto)



bot.polling()
