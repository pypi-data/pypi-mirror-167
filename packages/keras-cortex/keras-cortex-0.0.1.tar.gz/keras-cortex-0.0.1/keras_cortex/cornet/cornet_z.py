import tensorflow as tf

from keras_cortex.cornet.util import Identity


class CORBlockZ(tf.keras.Model):

    def __init__(self, in_channels, out_channels, kernel_size=3, stride=1, name=None):
        super().__init__(name=name)
        self.conv = tf.keras.layers.Conv2D(out_channels, kernel_size=kernel_size, strides=stride,
                                           kernel_initializer=tf.keras.initializers.GlorotUniform(),
                                           bias_initializer=tf.keras.initializers.Constant(0))
        self.nonlin = tf.keras.layers.ReLU()
        self.pool = tf.keras.layers.MaxPool2D(pool_size=3, strides=2)
        self.out = Identity()  # for an easy access to this block's output

        self.kernel_size = kernel_size

    def call(self, x, **kwargs):
        x = tf.keras.layers.ZeroPadding2D((self.kernel_size, self.kernel_size))(x)
        x = self.conv(x)
        x = self.nonlin(x)
        x = tf.keras.layers.ZeroPadding2D((1, 1))(x)
        x = self.pool(x)
        x = self.out(x)  # for an easy access to this block's output

        return x


def CORNetZ():
    model = tf.keras.Sequential([
        CORBlockZ(3, 64, kernel_size=7, stride=2, name='V1'),
        CORBlockZ(64, 128, name='V2'),
        CORBlockZ(128, 256, name='V4'),
        CORBlockZ(256, 512, name='IT'),
        tf.keras.Sequential([
            tf.keras.layers.AvgPool2D(1, name='avgpool'),
            tf.keras.layers.Flatten(name='flatten'),
            tf.keras.layers.Dense(10, name='linear',
                                  kernel_initializer=tf.keras.initializers.GlorotUniform(),
                                  bias_initializer=tf.keras.initializers.Constant(0)),
            Identity(name='output')
        ], name='decoder')
    ])

    return model
