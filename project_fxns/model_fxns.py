from tensorflow.keras import models, layers, Model
from tensorflow.keras import metrics 
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import regularizers
from tensorflow.keras import initializers
from tensorflow.keras import backend as K
from tensorflow.keras import Input

METRICS = ['mae']

def build_CNN(lr = 0.001, conv_filters = 16, dense_neurons = 16, dense_layers = 1, cnn_layers=1,
              conv_relu_pool_layers = 2, activity_reg = 0.001, input_channels = 4, 
              loss_str='mean_absolute_error', opt=optimizers.Adam(learning_rate=0.1), act_func='relu',
              nlats=18, nlons=45):
    
    optimizer_dict = {'RMSprop':optimizers.RMSprop(learning_rate=lr)}
    initializer = initializers.HeUniform()

    ## Define inputs ##
    stacked_input = layers.Input(shape=(nlats, nlons, input_channels), name="stacked_input")
    gmt_input = layers.Input(shape=(1,), name="gmt")
    doy_input = layers.Input(shape=(1,), name="doy")

    ## Input layer for gridded inputs ##
    x = stacked_input

    ## Convolution layers ##
    for m in range(conv_relu_pool_layers):
        for n in range(cnn_layers):
            x = layers.Conv2D(conv_filters, (3,3), 
                              activity_regularizer=regularizers.l2(activity_reg),
                              kernel_initializer=initializer)(x)
            x = layers.Activation(act_func)(x)
        x = layers.MaxPooling2D((2,2))(x)

    ## Flatten feature vector and concatenate GMT and DOY inputs to the end ##
    x = layers.Flatten()(x)
    x = layers.concatenate([x, gmt_input, doy_input])

    ## Fully-connected layers ##
    for i in range(dense_layers):
        x = layers.Dense(dense_neurons, 
                         activity_regularizer=regularizers.l2(activity_reg),
                        kernel_initializer=initializer)(x)
        x = layers.Activation(act_func)(x)

    ## Output layer ##
    tmax_pred = layers.Dense(1, activation='linear')(x) ## output layer
    
    model = Model(inputs = [stacked_input, gmt_input, doy_input],
                  outputs = [tmax_pred])
    
    model.compile(loss=loss_str, optimizer=optimizer_dict[opt], 
                  metrics=METRICS, weighted_metrics=[])
    
    return(model)

