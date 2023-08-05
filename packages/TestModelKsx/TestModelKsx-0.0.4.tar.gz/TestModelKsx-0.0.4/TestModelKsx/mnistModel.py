#import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras import Model


def say_hi():
    print("hi")

class MnistModel(Model):
    def __init__(self):
        super(MnistModel, self).__init__()
        self.flatten = Flatten()
        self.d1 = Dense(128, activation='relu')
        self.d2 = Dense(10, activation='softmax')

    def call(self, x):
        x = self.flatten(x)
        x = self.d1(x)
        y = self.d2(x)
        return y

if __name__=='__main__':
    say_hi()


