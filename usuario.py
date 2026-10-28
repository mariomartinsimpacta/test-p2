def buscar_usuario(usuario_id):
    return {
        "id": usuario_id,
        "nome": "Zoe isabek"
    }

def obter_nome(usuario_id):
    usuario = buscar_usuario(usuario_id)
    return usuario["nome"]

teste = obter_nome(1)
print(teste)