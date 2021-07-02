import os
from distutils.util import strtobool
import tensorflow.keras as keras

__all__ = [
    'keras', 'utils', 'activations', 'applications', 'backend', 'datasets',
    'layers', 'preprocessing', 'wrappers', 'callbacks', 'constraints', 'initializers',
    'metrics', 'models', 'losses', 'optimizers', 'regularizers', 'TF_KERAS',
]

TF_KERAS = strtobool(os.environ.get('TF_KERAS', '0'))

if TF_KERAS:
    import tensorflow as tf
    keras = tf.keras
else:
    import tensorflow.keras as keras

import tensorflow
utils = tensorflow.keras.utils
activations = tensorflow.keras.activations
applications = tensorflow.keras.applications
backend = tensorflow.keras.backend
datasets = tensorflow.keras.datasets
layers = tensorflow.keras.layers
preprocessing = tensorflow.keras.preprocessing
wrappers =tensorflow.keras.wrappers
callbacks = tensorflow.keras.callbacks
constraints = tensorflow.keras.constraints
initializers = tensorflow.keras.initializers
metrics = tensorflow.keras.metrics
models = tensorflow.keras.models
losses = tensorflow.keras.losses
optimizers = tensorflow.keras.optimizers
regularizers = tensorflow.keras.regularizers
