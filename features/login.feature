# language: pt 

Funcionalidade: Login 
    Como um usuário desse sistema
    Eu quero realizar o login na minha conta
    Para poder acessar as funcionalidades

    Cenário: Login com sucesso 
        Dado que o usuário quer realizar o login
        Quando o usuário insere seu username "xavierruth" e a senha "1234"
        Então deverá realizar o login com sucesso 

    Cenário: Falha no login
        Dado que o usuário quer realizar o login
        Quando o usuário insere seu username "xavierruth" e a senha "4321"
        Então retornará uma mensagem de "Dados incorretos. Tente novamente"

    Cenário: Validação de campos obrigatórios
        Dado que o usuário quer realizar o login
        Quando o usuário insere seu username "xavierruth" e a senha " "
        Então retornará uma mensagem de "Preencha todos os campos"

