# !/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#Author: Fernando Rodrigo Aguilar Javier
#Author email: faguilar@comunidad.unam.mx
#Detalles del codigo
#Solo es necesario cambiar el campo de la variable path para que pandas encuentre el archivo
#
##################################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%################################

from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb+srv://faguilar:Yc6LUgJzDH%407iAy@cluster0.ea7z2.mongodb.net/test?authSource=admin&replicaSet=atlas-12cjke-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
