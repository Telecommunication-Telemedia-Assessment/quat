#!/usr/bin/env python3
"""
Preparation for visualisation of high dimensial data using TSNE approach
"""
"""
    This file is part of quat.
    quat is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    quat is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with quat. If not, see <http://www.gnu.org/licenses/>.

    Author: Steve Göring
"""
import numpy as np
import pandas as pd

from sklearn.manifold import TSNE

from quat.log import *


def learn_embedding(df, dims=2):
    """
    learns an embedding based on TSNE approach with `dims` final dimensions, using all columns of `df`
    """
    X = df._get_numeric_data().values

    X_embedded = TSNE(n_components=dims).fit_transform(X)
    X_embedded.shape
    return X_embedded


if __name__ == "__main__":
    lInfo("only a lib")
