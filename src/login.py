def autenticar(usuario, senha):
    if not usuario.strip() or not senha.strip():
        return "Preencha todos os campos"
    if usuario == "xavierruth" and senha == "1234":
        return "Login realizado com sucesso"
    else:
        return "Dados incorretos. Tente novamente"
