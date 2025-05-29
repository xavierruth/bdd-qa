from behave import given, when, then 
from src.login import autenticar

@given('que o usuário quer realizar o login')
def step_impl(context):
    pass  

@when('o usuário insere seu username "{usuario}" e a senha "{senha}"')
def step_impl(context, usuario, senha):
    context.resultado = autenticar(usuario, senha)

@then('deverá realizar o login com sucesso')
def step_impl(context):
    assert context.resultado == "Login realizado com sucesso"

@then('retornará uma mensagem de "Dados incorretos. Tente novamente"')
def step_impl(context):
    assert context.resultado == "Dados incorretos. Tente novamente"

@then('retornará uma mensagem de "Preencha todos os campos"')
def step_impl(context):
    assert context.resultado == "Preencha todos os campos"
 