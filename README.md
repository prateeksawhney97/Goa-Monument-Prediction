# Goa-Monument-Prediction-Project


### Problem Statement:

Goa is a major tourist destination which pulls thousands of tourists every year. Goa is known for its beautiful beaches and hospitality. There are a number of monuments and landmarks depicting the cultural, history and development of Goa. Due to high inflow of domestic as well as international tourists, the manpower required to guide the tourist on these landmark is not sufficient and sometimes lack in the information that need to be given and highlighted to the tourist. 

Hence there must be a mobile application which renders information about the monument or landmark just by taking their live pictures as inputs. In other word, the application should allow the user to click a photograph and based on the picture it should display information about the monument/landmark. 

### Monuments Included:

1. Ajoba Temple Goa
2. Shanta Durga Temple
3. Fort Aguada
4. Our Lady of the Immaculate Conception Church, Goa
5. Viceroys Arch, Goa

### Model Architecture Used:

Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 118, 126, 24)      1824      
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 57, 61, 36)        21636     
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 27, 29, 48)        43248     
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 25, 27, 64)        27712     
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 23, 25, 64)        36928     
_________________________________________________________________
dropout_1 (Dropout)          (None, 23, 25, 64)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 36800)             0         
_________________________________________________________________
dense_1 (Dense)              (None, 100)               3680100   
_________________________________________________________________
dense_2 (Dense)              (None, 50)                5050      
_________________________________________________________________
dense_3 (Dense)              (None, 10)                510       
_________________________________________________________________
dense_4 (Dense)              (None, 5)                 55        
=================================================================
Total params: 3,817,063
Trainable params: 3,817,063
Non-trainable params: 0
