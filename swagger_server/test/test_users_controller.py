# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_user_create_post(self):
        """Test case for user_create_post

        Cria um usuário
        """
        response = self.client.open(
            '/v1/user/create',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_delete_delete(self):
        """Test case for user_delete_delete

        Deleta um usuário
        """
        response = self.client.open(
            '/v1/user/delete',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_id_get(self):
        """Test case for user_id_get

        Retorna um usuário específico
        """
        response = self.client.open(
            '/v1/user/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_read_get(self):
        """Test case for user_read_get

        Retorna todos os usuários
        """
        response = self.client.open(
            '/v1/user/read',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_update_put(self):
        """Test case for user_update_put

        Atualiza um usuário
        """
        response = self.client.open(
            '/v1/user/update',
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
