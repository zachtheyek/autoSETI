# autoSETI

This is a Transformer model, trained on the Kaggle dataset, which are dynamic spectra generated from real observations taken using the Green Bank Telescope, with some containing artificially injected signals using setigen. We refer to the former as the "haystack", and the latter as the "needles".

There are 2 files that will be of immediate interest to you: 

MNIST_auto_classifier.ipynb contains a tutorial of an autoencoder trained on the MNIST dataset. It's tasked with the standard problem of classifying handwritten digits. This notebook is meant to illustrate techniques that BL currently uses.

Kaggle_transformer.ipynb contains the Transformer trained on the Kaggle dataset. Note that currently, the model is in a highly unstable build, and should NOT be viewed as anything more than a running prototype.
