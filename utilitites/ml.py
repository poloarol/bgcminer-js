"""
    Provides Machine Learning models for analysis

    Implements the following algorithms;

        Scaler                : Normalizer
        NLP                   : BioVec (ProtVec)
        Dimensional Reduction : Unifold Manifold Approximation & Projection
        Supervised Learning   : Multi-Layer Perceptron

"""


import joblib

from typing import List
from dataclasses import dataclass

@dataclass
class Scaler(object):

    model_path: str

    def __post_init__(self):
        self.model = joblib.load(self.model_path)
    
    def get_model(self):

        return self.model

@dataclass
class BioVec(object):

    model_path: str

    def __post_init__(self):
        self.model = joblib.load(self.model_path)
    
    def get_model(self):

        return self.model


@dataclass
class DimensionalReduction(object):

    model_path: str

    def __post_init__(self):
        self.model = joblib.load(self.model_path)
    
    def get_model(self):

        return self.model

@dataclass
class Supervised(object):
    
    model_path: str

    def __post_init__(self):
        self.model = joblib.load(self.model)

    def get_model(self):

        return self.model

