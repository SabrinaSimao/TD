# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:27:41 2016

@author: sabri
"""

"""Projeto final de DesSoft da Engenharia 1C
    Tower Defense"""
    
class Tower():
    def __init__(self, alcance, reload, dano, imagem, nome):
        self.alcance = alcance
        self.reload = reload
        self.dano = dano
        self.imagem = imagem
        self.nome = nome


canhao = Tower(5, 5, 5, canhao_image, "canhao")

