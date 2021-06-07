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

import pandas as pd
import hashlib
import random
import numpy as np

def null_ids(df, col): # failure to implement the verification process of doesn't repeat the hash
    for i in df[df[col].notnull() == False][col].index:
        var = "new entry %s" % (random.random())
        hash = hashlib.sha1(var.encode("UTF-8")).hexdigest()
        d = df.iloc[i].to_dict()
        d[col] = hash
        df.iloc[i] = d.values()
    return df

if __name__ == '__main__':
    path = 'data/data_prueba_tecnica_.csv'
    df = pd.read_csv(path)
    # df.head()
    #df['paid_at'] = df['paid_at'].astype('datetime64[ns]')
    #df['created_at'] = df['created_at'].astype('datetime64[ns]')
    print(df.info())
    # for id
    df = null_ids(df, col='id')
    # for company id
    name = df[['name']]
    com_id = df[['company_id']]
    for c in df.name.unique()[-3:]:
        name.replace(c, 'MiPasajefy', inplace=True)
    df['name'] = name
    df['company_id'] = com_id

    com_name = df[df.company_id.notna() == False].name.values[0]
    c_id = df[df.name == com_name].company_id.iloc[0]
    com_id.replace(np.nan, c_id, inplace=True)
    df['company_id'] = com_id

    for c in df.company_id.unique()[-1:]:
        com_name = df[df.company_id == c].name.values[0]
        c_id = df[df.name == com_name].company_id.iloc[0]
        com_id.replace(c, c_id, inplace=True)
    df['company_id'] = com_id

    df.to_csv('data/company.csv', header=True, index=False, encoding="utf-8")
