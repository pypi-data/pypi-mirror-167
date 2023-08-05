#!/usr/bin/env python3
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import joblib
import numpy as np
from pkg_resources import resource_filename
import fire


class Regbot:
  reg_model_path = resource_filename(__name__, 'btc_model.h5') 
  model_scaler_path = resource_filename(__name__, 'btclogscaler.gz') 


  def __init__(self,*args):
  	pass



  @classmethod  
  def loadmodel(cls):
    loaded_model = joblib.load(open(f'{cls.reg_model_path}', 'rb'))
    return loaded_model


  @classmethod  
  def prepareInput(cls,opening,closing,utcdate):
    avr = closing/(opening + closing)
    bvr = opening/(opening + closing)
    utctime = utcdate.split(' ')[1][1]
    testdata = np.array([[avr,bvr,utctime]])
    scaler = joblib.load(f'{cls.model_scaler_path}')
    testdata = scaler.transform(testdata)

    return testdata


  @classmethod
  def buySignalGenerator(cls,opening,closing,utcdate):
    scalledInput = cls.prepareInput(opening,closing,utcdate)
    return np.round(np.clip(cls.loadmodel().predict(scalledInput), 0, 1) > 0)[0].astype(int)





def signal(opening, closing,utcdate):
  try:
    return Regbot.buySignalGenerator(opening,closing,utcdate)
  except Exception as e:
    print(e)


if __name__ == '__main__':
  fire.Fire(signal)
