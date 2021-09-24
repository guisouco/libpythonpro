import pytest as pytest

from libpythonpro_gsc.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['guilhermejogosonline30@gmail.com', 'gscolacio@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'gscolacio@gmail.com',
        'Cursos Python Pro',
        'Primeira vaga conquistada em breve, muito breve',
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'guilherme.souzacolacio']
)
def test_remetente(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'gscolacio@gmail.com',
            'Cursos Python Pro',
            'Primeira vaga conquistada em breve, muito breve',
        )
        assert remetente in resultado
