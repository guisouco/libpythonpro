from libpythonpro_gsc.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Guilherme',
                      email='guilherme.souzacolacio@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Guilherme',
                        email='guilherme.souzacolacio@gmail.com'),
                Usuario(nome='Colacio', email='gscolacio@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
