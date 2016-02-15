# -*- coding: utf-8 -*-
# #############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Michell Stuttgart
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
###############################################################################
from unittest import TestCase


class TestErroTipoIncorreto(TestCase):

    def __init__(self, nome_campo, tipo, tipo_correto):
        self.msg = u'''Campo %s deve ser %s . Tipo encontrado: %s''' % (
            nome_campo, str(tipo_correto), str(tipo))

    def __str__(self):
        return self.msg


class TestErroCampoObrigatorio(TestCase):

    def __init__(self, nome_campo):
        self.msg = u'''Campo %s é de envio obrigatorio, mas não foi
        preenchido!''' % nome_campo

    def __str__(self):
        return self.msg


class TestErroCampoNaoNumerico(TestCase):

    def __init__(self, nome_campo):
        self.msg = u'''Campo %s não é constituído apenas por números!''' % \
                   nome_campo

    def __str__(self):
        return self.msg


class TestErroCampoTamanhoIncorreto(TestCase):

    def __init__(self, nome_campo, tamanho_esperado, tamanho):
        self.msg = u'''Campo %s possui tamanho incorreto. Esperado é %d mas o
        encontrado foi %d.''' % (nome_campo, tamanho_esperado, tamanho)

    def __str__(self):
        return self.msg


class TestErroSemConexaoComInternet(TestCase):

    def __init__(self, msg):
        self.msg = u'''Falha na conexão com a Internet. %s''' % msg

    def __str__(self):
        return self.msg


class TestErroConexaoComServidor(TestCase):

    def __init__(self, msg):
        self.msg = u'''Erro de conexão com o servidor. %s''' % msg

    def __str__(self):
        return self.msg


class TestErroConexaoTimeOut(TestCase):

    def __init__(self, msg):
        self.msg = u'''Erro de timeout. %s''' % msg

    def __str__(self):
        return self.msg


class TestErroRequisicao(TestCase):

    def __init__(self, msg):
        self.msg = u'''Falha na requisição. %s''' % msg

    def __str__(self):
        return self.msg


class TestErroSSL(TestCase):

    def __init__(self, msg):
        self.msg = u'''Erro SSL. %s''' % msg

    def __str__(self):
        return self.msg


class TestErroValidacaoXML(TestCase):

    def __init__(self, msg):
        self.msg = u'''Erro durante valdação do XML. %s''' % msg

    def __str__(self):
        return self.msg