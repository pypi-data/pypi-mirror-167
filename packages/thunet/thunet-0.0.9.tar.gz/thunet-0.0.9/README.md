# THUNET: A simple deep learning framework for scientific and education purpose.
1. **Neural networks[1]**  
    * Layers / Layer-wise ops
        - Add
        - Flatten
        - Multiply
        - Softmax
        - Fully-connected/Dense
        - Sparse evolutionary connections
        - LSTM
        - Elman-style RNN
        - Max + average pooling
        - Dot-product attention
        - Embedding layer
        - Restricted Boltzmann machine (w. CD-n training)
        - 2D deconvolution (w. padding and stride)
        - 2D convolution (w. padding, dilation, and stride)
        - 1D convolution (w. padding, dilation, stride, and causality)
    * Modules
        - Bidirectional LSTM
        - ResNet-style residual blocks (identity and convolution)
        - WaveNet-style residual blocks with dilated causal convolutions
        - Transformer-style multi-headed scaled dot product attention
    * Regularizers
        - Dropout
    * Normalization
        - Batch normalization (spatial and temporal)
        - Layer normalization (spatial and temporal)
    * Optimizers
        - SGD w/ momentum
        - AdaGrad
        - RMSProp
        - Adam
    * Learning Rate Schedulers
        - Constant
        - Exponential
        - Noam/Transformer
        - Dlib scheduler
    * Weight Initializers
        - Glorot/Xavier uniform and normal
        - He/Kaiming uniform and normal
        - Standard and truncated normal
    * Losses
        - Cross entropy
        - Squared error
        - Bernoulli VAE loss
        - Wasserstein loss with gradient penalty
        - Noise contrastive estimation loss
    * Activations
        - ReLU
        - Tanh
        - Affine
        - Sigmoid
        - Leaky ReLU
        - ELU
        - SELU
        - Exponential
        - Hard Sigmoid
        - Softplus
    * Models
        - Bernoulli variational autoencoder
        - Wasserstein GAN with gradient penalty
        - word2vec encoder with skip-gram and CBOW architectures
    * Utilities
        - `col2im` (MATLAB port)
        - `im2col` (MATLAB port)
        - `conv1D`
        - `conv2D`
        - `deconv2D`
        - `minibatch`
2. **BERT** 
   * Vanilla BERT
   * Simple BERT


3. **REFERENCE**  
Our contribution is implementation of the vanilla BERT and simple BERT.  
All other codes following the licence claimed by (ddbourgin)[https://github.com/ddbourgin]  in his (Numpy_ML)![https://github.com/ddbourgin/numpy-ml]  project.


4. **Release Frequent Asked Questions**

* Q: Python2.7:    LookupError: unknown encoding: cp0  
* A: Setting environment in the shell: set PYTHONIOENCODING=UTF-8

5. **Product Release**

Supported Python versions:

| Python |
|--------|
| 2.7    |
| 3.5    |
| 3.6    |
| 3.7    |
| 3.8    |
| 3.9    |
| 3.10   |

[1] David Bourgin. Machine learning, in numpy. https://github.com/ddbourgin/numpy-ml.