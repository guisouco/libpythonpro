from unittest.mock import Mock

import pytest as pytest

from libpythonpro_gsc.spam.enviador_de_email import Enviador
from libpythonpro_gsc.spam.main import EnviadorDeSpam
from libpythonpro_gsc.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Guilherme', email='guilherme.souzacolacio@gmail.com'),
            Usuario(nome='Colacio', email='gscolacio@gmail.com')
        ],
        [
            Usuario(nome='Guilherme', email='guilherme.souzacolacio@gmail.com')
        ]
    ]
)
def test_qde_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'guilherme.souzacolacio@gmail.com',
        'Os Novos Mutantes merece sim uma continuação',
        'A Disney, Fox e Marvel são umas bostas, Os Novos Mutantes é maravilhoso e'
        'merecem uma segunda chance :(('
    )
    assert len(usuarios) == enviador.enviar.call_count

def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Guilherme', email='guilherme.souzacolacio@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gscolacio@gmail.com',
        'Primeira vaga',
        'Objetivo conquistar a primeira vaga com o curso Python Pro'
    )
    enviador.enviar.assert_called_once_with(
        'gscolacio@gmail.com',
        'guilherme.souzacolacio@gmail.com',
        'Primeira vaga',
        'Objetivo conquistar a primeira vaga com o curso Python Pro'
    )
