# Goa-Monument-Prediction-Project


### Problem Statement:

Goa is a major tourist destination which pulls thousands of tourists every year. Goa is known for its beautiful beaches and hospitality. There are a number of monuments and landmarks depicting the cultural, history and development of Goa. Due to high inflow of domestic as well as international tourists, the manpower required to guide the tourist on these landmark is not sufficient and sometimes lack in the information that need to be given and highlighted to the tourist. 

Hence there must be a mobile application which renders information about the monument or landmark just by taking their live pictures as inputs. In other word, the application should allow the user to click a photograph and based on the picture it should display information about the monument/landmark. 


![Basilica_of_Bom_Jesus_-_Old_Goa](https://user-images.githubusercontent.com/34116562/72215966-9445c180-3540-11ea-9d09-97b193d42eb5.jpg)

### Flask Application:

#### Website: https://goaml-265511.appspot.com/ (Deployed on Google Cloud Platform)

#### GitHub: https://github.com/prateeksawhney97/Flask-Application-for-Goa-Monuments-Prediction

### Monuments Included:

1. Ajoba Temple Goa
2. Shanta Durga Temple
3. Fort Aguada
4. Our Lady of the Immaculate Conception Church, Goa
5. Viceroys Arch, Goa

### Model Architecture Used:



| Layer         		|     Output Shape	        					| Param |
|:---------------------:|:---------------------------------------------:|:---------------------------------------------:| 
| Convolution Layer 1   	| (None, 118, 126, 24 	|  1824 |
| Convolution Layer 2	    | (None, 57, 61, 36)    									|  21636 |
| Convolution Layer 3		| (None, 27, 29, 48) |      43248 									|
| Convolution Layer 4				| (None, 25, 27, 64)      |  		27712							|
|	Convolution Layer 5					|		(None, 23, 25, 64)			|					36928		|
| Dropout Layer 1              |     (None, 23, 25, 64)   |   0    |
| Flatten Layer 1              |        (None, 36800)  |  0    |
|	Dense Layer 1				|		(None, 100)		|		3680100	|
| Dense Layer 2		| (None, 50)     |   	5050								|
|	Dense Layer 3				|		(None, 10)						|   510  |
| Dense Layer 4		| (None, 5)   |     				55			|

- Total params: 3,817,063
- Trainable params: 3,817,063
- Non-trainable params: 0


##### Accuracy:  0.9940
##### Validation Accuracy: 0.7381
