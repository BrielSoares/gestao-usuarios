from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

"""
Rota Clientes
    - /clientes/ (GET) - Vai listar os clientes
    - /clientes/ (POST) - Inserir o cliente no servidor
    - /clientes/new (GET) - renderizar o formulario pra criar um cliente
    - /clientes/<id> (GET) - obter os dados de um cliente
    - /clientes/<id>/edit (GET) - renderizar um formulario pra editar um cliente
    - /clientes/<id>/update (PUT) - atualizar os dados do cliente
    - /clientes/<id>/delete (DELETE) - deleta o registro do usuario
"""

@cliente_route.route('/')
def lista_clientes():
    # listar os clientes
    pass
    return render_template('lista_clientes.html', clientes=CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    #Inserir os dados do cliente
    dados = request.json
    
    novo_usuario = {
        "id": len(CLIENTES)+1 ,
        "nome": dados['nome'],
        "email": dados['email']
    }
    
    CLIENTES.append(novo_usuario)
    return render_template('item_cliente.html', cliente=novo_usuario)    

@cliente_route.route('/new') 
def form_cliente():
    # formulario para cadastrar um cliente
    pass
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    # exibir detalhes do cliente
    pass
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    # exibir detalhes do cliente
    pass
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    # atualizar informações do cliente
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['DELETE'])
def deletar_cliente(cliente_id):
    # deletar informações do cliente
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id]
    return {'deleted':'ok'}
