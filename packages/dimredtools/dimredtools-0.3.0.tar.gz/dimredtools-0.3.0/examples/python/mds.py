import numpy as np
from sklearn.datasets import make_swiss_roll
from dimredtools import MDS
import swiss_roll_test


# Testing MDS algorithm on the "swiss roll" dataset.
X, color = make_swiss_roll(n_samples=1000, random_state=123)
swiss_roll_test.show_swiss_roll(X, color)
swiss_roll_test.test_model(MDS(), X, color)
