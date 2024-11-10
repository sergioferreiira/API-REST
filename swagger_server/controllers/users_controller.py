import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def user_create_post():  # noqa: E501
    """Cria um usuário

    Este endpoint cria um usuário # noqa: E501


    :rtype: User
    """
    return 'do some magic!'


def user_delete_delete():  # noqa: E501
    """Deleta um usuário

    Este endpoint deleta um usuário # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def user_id_get(id):  # noqa: E501
    """Retorna um usuário específico

    Este endpoint retorna apenas um usuário pelo ID # noqa: E501

    :param id: ID do usuário
    :type id: int

    :rtype: User
    """
    return 'do some magic!'


def user_read_get():  # noqa: E501
    """Retorna todos os usuários

    Este endpoint retorna todos os usuários cadastrados no sistema # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def user_update_put():  # noqa: E501
    """Atualiza um usuário

    Este endpoint atualiza os dados de um usuário # noqa: E501


    :rtype: User
    """
    return 'do some magic!'
