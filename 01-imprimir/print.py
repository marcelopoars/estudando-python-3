# Imprimindo um STRING
print ("Imprimindo na tela.")

# Imprimir um VARIAVEL
# Criada variavel chamada nome_usuario
# Variavel nome_usuario recebe o nome "marcelopoars"
nome_usuario = "marcelopoars"
# Mostra na tela o conteudo da variavel
print (nome_usuario)

# Imprimindo VARIAVEL + STRING
print ("Seja bem-vindo", nome_usuario,"!")

# Imprimindo utilizando o FORMAT
nome_usuario = "Marcelo Pereira"
senha = 21212121
# Forma mais recomendada para IMPRIMIR NA TELA
print("Olá {}! Sua senha é: {}" .format(nome_usuario, senha))

# Imprimir utilizando um DICIONARIO
# Criamos um dicionario chamado: dados_do_usuarios
dados_do_usuarios = {
"nome_usuario" : "João da Silva",
"user_name" : "joaosilva",
"senha" : 232323
}
# Imprime o conteudo do meu dicionario ("dados_do_usuarios")
print("Olá {nome_usuario}! Seu User Name é: {user_name} e sua senha é {senha}" .format(**dados_do_usuarios))
