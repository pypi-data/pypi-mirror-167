# -*- coding: utf-8 -*-

import numpy as np

def ndvi(raster):
  bands = raster.shape[0]
  max = raster[0]
  min = raster[0]
  for i in range (bands):
    max = np.maximum(raster[i], max)
    min = np.minimum(raster[i], min)
  return (max + min) / (max-min)

