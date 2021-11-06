import tensorflow
from tensorflow import keras
import check
import numpy as np
import tensorflow_addons

model = keras.models.load_model('predict_model3.h5')
time_data,price=check.predict_window(30)
time_data=np.array(time_data)
time_data=time_data.reshape(1,9,30)

predict_price=model.predict(time_data)[0][0]
print('明日のGPBUSDの価格は:',predict_price,'と予測します')

if price+0.002<predict_price:
    if price+0.01<predict_price:
        print('大きく価格が上昇すると予測します')
    else:
        print('価格は上昇すると予測します')
elif price-0.002<=predict_price<=price+0.002:
    print('価格の変化は少ないと予測します')

else:
    if price-0.01>predict_price:
        print('大きく価格は下がると予測します')
    else:
        print('価格は下がると予測します')
    