
import os

from typing import Any, Dict

from flask import Flask

from backend.utilitites.ml import BioVec
from backend.utilitites.ml import Scaler
from backend.utilitites.ml import DimensionalReduction
from backend.utilitites.ml import Supervised


biovec: Any
scaler: Any
umap: Any
n_network: Any


clusters = {0: 'PKS', 1: 'NRPS', 2: 'RiPP'}


app = Flask(__name__)


@app.route('/')
def acceuil():
    return {'message': 'Hello World'}

@app.route('/results')
def resultat():
    return {'message': 'Results'}

@app.route('/about')
def a_propose():
    return {'message': 'About'}

@app.route('/tutorial')
def tutoriel():
    return {'message': 'tutorial'}


def analyze(seq: str):

    vector = biovec.to_vecs(seq)
    vector = scaler.transform(vector)
    vector = umap.transform(vector)

    cluster, probability = n_network.predict(vector), n_network.predict_proba(vector)

    return clusters[cluster], probability


def load_models():

    biovec = BioVec(os.path.join(os.getcwd(), 'bgc\\models\\uniprot2vec.model'))
    scaler = Scaler(os.path.join(os.getcwd(), 'bgc\\models\\Normalizer.model'))
    umap = DimensionalReduction(os.path.join(os.getcwd(), 'bgc\\models\\umap.model'))
    n_network = Supervised(os.path.join(os.getcwd(), 'bgc\\models\\nn.model'))

    return biovec, scaler, umap, n_network


if __name__ == '__main__':

    app.run(port=5000)

    biovec, scaler, umap, n_network = load_models()