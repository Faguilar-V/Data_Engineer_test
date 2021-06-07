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
    path = '../data/company.csv'
    df = pd.read_csv(path)
    # id field
    id = [i[:24] for i in df.id]
    com_id = [i[:24] for i in df.company_id]
    df['amount'] = df.amount.astype('float32')
    for i in df[df.amount >= 1e16].index:
        d = df.iloc[i].to_dict()
        d['amount'] = 0
        df.iloc[i] = d.values()
    amount = [round(float(i), 2) for i in df.amount]
    df['id'] = id
    df['company_id'] = com_id
    df['amount'] = amount
    df.to_csv('../data/company_transform.csv', header=True, index=False, encoding="utf-8")
