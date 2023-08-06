from time import time
from collections import OrderedDict

import numpy as np

from thunet.neural_nets.utils import minibatch
from thunet.neural_nets.activations import ReLU, Affine, Sigmoid
from thunet.neural_nets.layers import LayerNorm1D
from thunet.neural_nets.layers import  FullyConnected
from thunet.neural_nets.modules import MultiHeadedAttentionModule
from thunet.neural_nets.modules import MultiHeadedAttentionModule_new
from thunet.neural_nets.losses import SquaredError

from thunet.neural_nets.layers import Embedding


class BERT(object):
    def __init__(
        self,
        vocab_size=21128,
        seq_len=512,
        latent_dim=64,
        n_heads=12,
        feature=768,
        batchsize = 30,
        act=ReLU(),

        optimizer="Adam(lr=0.001)",
        init="glorot_uniform",
    ):
        """
        A variational autoencoder (VAE) with 2D convolutional encoder and Bernoulli
        input and output units.
        Notes
        -----
        The VAE architecture is
        .. code-block:: text
                            |-- t_mean ----|
            X -> [Encoder] -|              |--> [Sampler] -> [Decoder] -> X_recon
                            |-- t_log_var -|
        where ``[Encoder]`` is
        .. code-block:: text
            Conv1 -> ReLU -> MaxPool1 -> Conv2 -> ReLU ->
                MaxPool2 -> Flatten -> FC1 -> ReLU -> FC2
        ``[Decoder]`` is
        .. code-block:: text
            FC1 -> FC2 -> Sigmoid
        and ``[Sampler]`` draws a sample from the distribution
        .. math::
            \mathcal{N}(\\text{t_mean}, \exp \left\{\\text{t_log_var}\\right\} I)
        using the reparameterization trick.
        Parameters
        ----------
        T : int
            The dimension of the variational parameter `t`. Default is 5.
        enc_conv1_pad : int
            The padding for the first convolutional layer of the encoder. Default is 0.
        enc_conv1_stride : int
            The stride for the first convolutional layer of the encoder. Default is 1.
        enc_conv1_out_ch : int
            The number of output channels for the first convolutional layer of
            the encoder. Default is 32.
        enc_conv1_kernel_shape : tuple
            The number of rows and columns in each filter of the first
            convolutional layer of the encoder. Default is (5, 5).
        enc_pool1_kernel_shape : tuple
            The number of rows and columns in the receptive field of the first
            max pool layer of the encoder. Default is (2, 3).
        enc_pool1_stride : int
            The stride for the first MaxPool layer of the encoder. Default is
            2.
        enc_conv2_pad : int
            The padding for the second convolutional layer of the encoder.
            Default is 0.
        enc_conv2_out_ch : int
            The number of output channels for the second convolutional layer of
            the encoder. Default is 64.
        enc_conv2_kernel_shape : tuple
            The number of rows and columns in each filter of the second
            convolutional layer of the encoder. Default is (5, 5).
        enc_conv2_stride : int
            The stride for the second convolutional layer of the encoder.
            Default is 1.
        enc_pool2_stride : int
            The stride for the second MaxPool layer of the encoder. Default is
            1.
        enc_pool2_kernel_shape : tuple
            The number of rows and columns in the receptive field of the second
            max pool layer of the encoder. Default is (2, 3).
        latent_dim : int
            The dimension of the output for the first FC layer of the encoder.
            Default is 256.
        optimizer : str or :doc:`Optimizer <numpy_ml.neural_nets.optimizers>` object or None
            The optimization strategy to use when performing gradient updates.
            If None, use the :class:`~numpy_ml.neural_nets.optimizers.SGD`
            optimizer with default parameters. Default is "RMSProp(lr=0.0001)".
        init : str
            The weight initialization strategy. Valid entries are
            {'glorot_normal', 'glorot_uniform', 'he_normal', 'he_uniform',
            'std_normal', 'trunc_normal'}. Default is 'glorot_uniform'.
        """

        self.loss = SquaredError()
        self.optimizer = optimizer
        self.init = init
        self.trainable = True

        self.latent_dim = latent_dim
        self.vocab_size = vocab_size
        self.seq_len = seq_len
        self.n_heads = n_heads
        self.feature = feature
        self.act = act
        self.batchsize = batchsize

        self._init_params()

    def _init_params(self):
        # self._build_encoder()
        self._build_multihead()
        self._build_wk()
        self._build_wq()
        self._build_wv()
        self._build_Layernorm1d1()
        self._build_Layernorm1d2()
        self._build_FC1()
        self._build_FC2()

    def _build_multihead(self):
        self.multihead = OrderedDict()
        self.multihead['multihead'] = MultiHeadedAttentionModule_new(
            n_heads=self.n_heads,
            dropout_p=0,
            optimizer=self.optimizer,
        )
    def _build_FC1(self):
        self.FC1 = OrderedDict()
        self.FC1['FC1'] = FullyConnected(
            n_out=self.n_heads * self.latent_dim,
            optimizer=self.optimizer
        )
    # w1 * relu(w2 * x + b2) + b1
    def _build_FC2(self):
        self.FC2 = OrderedDict()
        self.FC2['FC2'] = FullyConnected(
            n_out=self.n_heads * self.latent_dim * 4,
            act_fn=ReLU(),
            optimizer=self.optimizer
        )
    def _build_Layernorm1d1(self):
        self.Layernorm1d1 = OrderedDict()
        self.Layernorm1d1['Layernorm1d1'] = LayerNorm1D(
            optimizer=self.optimizer
        )
    def _build_Layernorm1d2(self):
        self.Layernorm1d2 = OrderedDict()
        self.Layernorm1d2['Layernorm1d2'] = LayerNorm1D(
            optimizer=self.optimizer
        )

    def _build_wk(self):
        self.wk = OrderedDict()
        self.wk['wk'] = FullyConnected(
            n_out=self.feature , optimizer=self.optimizer
                                       )
    def _build_wq(self):
        self.wq = OrderedDict()
        self.wq['wq'] = FullyConnected(
            n_out=self.feature , optimizer=self.optimizer
                                       )
    def _build_wv(self):
        self.wv = OrderedDict()
        self.wv['wv'] = FullyConnected(
            n_out= self.feature ,optimizer=self.optimizer
                                       )

    @property
    def parameters(self):
        return {
            "components": {
                "wv": {k: v.parameters for k, v in self.wv.items()},
                "wq": {k: v.parameters for k, v in self.wq.items()},
                "wk": {k: v.parameters for k, v in self.wk.items()},
                "Layernorm1d2": {k: v.parameters for k, v in self.Layernorm1d2.items()},
                "Layernorm1d1": {k: v.parameters for k, v in self.Layernorm1d1.items()},
                "FC2": {k: v.parameters for k, v in self.FC2.items()},
                "FC1": {k: v.parameters for k, v in self.FC1.items()},
                "multihead": {k: v.parameters for k, v in self.multihead.items()},
                # "encoder": {k: v.parameters for k, v in self.encoder.items()},
            }
        }

    @property
    def hyperparameters(self):
        return {
            "layer": "BERT",
            "init": self.init,
            "loss": str(self.loss),
            "optimizer": self.optimizer,

            "batchsize":self.batchsize,
            "vocab_size": self.vocab_size,
            "seq_len": self.seq_len,
            "latent_dim": self.latent_dim,
            "n_heads": self.n_heads,
            "feature": self.feature,
            "act": self.act,
            # "encoder_ids": list(self.encoder.keys()),
            "multihead_ids":list(self.multihead.keys()),
            "FC1_ids": list(self.FC1.keys()),
            "FC2_ids": list(self.FC2.keys()),
            "Layernorm1d1_ids": list(self.Layernorm1d1.keys()),
            "Layernorm1d2_ids": list(self.Layernorm1d2.keys()),
            "wk_ids": list(self.wk.keys()),
            "wq_ids": list(self.wq.keys()),
            "wv_ids": list(self.wv.keys()),
            "components": {
                # "encoder": {k: v.hyperparameters for k, v in self.encoder.items()},
                "multihead": {k: v.hyperparameters for k, v in self.multihead.items()},
                "FC1": {k: v.hyperparameters for k, v in self.FC1.items()},
                "FC2": {k: v.hyperparameters for k, v in self.FC2.items()},
                "Layernorm1d1": {k: v.hyperparameters for k, v in self.Layernorm1d1.items()},
                "Layernorm1d2": {k: v.hyperparameters for k, v in self.Layernorm1d2.items()},
                "wk": {k: v.hyperparameters for k, v in self.wk.items()},
                "wq": {k: v.hyperparameters for k, v in self.wq.items()},
                "wv": {k: v.hyperparameters for k, v in self.wv.items()},
            },
        }

    @property
    def gradients(self):
        return {
            "components": {
                "wv": {k: v.gradients for k, v in self.wv.items()},
                "wq": {k: v.gradients for k, v in self.wq.items()},
                "wk": {k: v.gradients for k, v in self.wk.items()},
                "Layernorm1d2": {k: v.gradients for k, v in self.Layernorm1d2.items()},
                "Layernorm1d1": {k: v.gradients for k, v in self.Layernorm1d1.items()},
                "FC2": {k: v.gradients for k, v in self.FC2.items()},
                "FC1": {k: v.gradients for k, v in self.FC1.items()},
                "multihead":{k: v.gradients for k, v in self.multihead.items()},
                # "encoder": {k: v.gradients for k, v in self.encoder.items()},
            }
        }


    def forward(self, X):
        K = self.wk['wk'].forward(X)
        Q = self.wq['wq'].forward(X)
        V = self.wv['wv'].forward(X)

        y_pred = (self.multihead['multihead'].forward(Q, K, V)).reshape(-1, self.feature)
        add_ln = self.Layernorm1d2['Layernorm1d2'].forward(y_pred + X)

        aulayer = self.FC2['FC2'].forward(add_ln)
        auout = self.FC1['FC1'].forward(aulayer)
        output = self.Layernorm1d1['Layernorm1d1'].forward(auout + add_ln)

        # for k, v in self.encoder.items():
        #     out = v.forward(out)
        return output

    def backward(self, X, y_pred, y_real):
        """VAE backward pass"""
        # E = self.encoder

        # compute gradients through the VAE loss
        # dY_pred= self.loss.grad(
        #     X_train.reshape(n_ex, -1), X_recon
        # )

        # dEncoder_FC4_out = E["FC5"].backward(dY_pred)
        # dX = E["FC4"].backward(dEncoder_FC4_out)

        dY_pred = self.loss.grad(
            y_real, y_pred, X, self.act
        )
        dpreddout1 = self.Layernorm1d1['Layernorm1d1'].backward(dY_pred)
        self.Layernorm1d1['Layernorm1d1'].update(dY_pred)

        dout1dzhongjian = self.FC1['FC1'].backward(dpreddout1[0])
        self.FC1['FC1'].update(dY_pred)
        dzhongjiandout2 = self.FC2['FC2'].backward(dout1dzhongjian[0])
        self.FC2['FC2'].update(dY_pred)

        add1 = np.ones_like(dzhongjiandout2[0])
        dout1dout2 = self.Layernorm1d2['Layernorm1d2'].backward([add1 + dzhongjiandout2[0]])
        self.Layernorm1d2['Layernorm1d2'].update(dY_pred)
        dLdQ, dLdK, dLdV = self.multihead['multihead'].backward(dout1dout2[0])
        self.multihead['multihead'].update(cur_loss = dY_pred)


        dkdX = self.wk['wk'].backward(dLdK[0])
        self.wk['wk'].update(dY_pred)
        dqdX = self.wq['wq'].backward(dLdQ[0])
        self.wq['wq'].update(dY_pred)
        dvdX = self.wv['wv'].backward(dLdV[0])
        self.wv['wv'].update(dY_pred)
        add2 = np.ones_like(dkdX)


        dout2dXk = dkdX + add2
        dout2dXq = dqdX + add2
        dout2dXv = dvdX + add2

        return dout2dXk,dout2dXq,dout2dXv

    def fit(self, X_train, n_epochs=1200, verbose=True):
        """
        Fit the VAE to a training dataset.
        Parameters
        ----------
        X_train : :py:class:`ndarray <numpy.ndarray>` of shape `(n_ex, in_rows, in_cols, in_ch)`
            The input volume
        n_epochs : int
            The maximum number of training epochs to run. Default is 20.
        batchsize : int
            The desired number of examples in each training batch. Default is 128.
        verbose : bool
            Print batch information during training. Default is True.
        """
        self.verbose = verbose
        self.n_epochs = n_epochs

        # self, self.in_cols, self.in_ch = X_train.shape
        # self.N = self.in_rows * self.in_cols * self.in_ch

        prev_loss = np.inf

        for i in range(n_epochs):
            loss, estart = 0.0, time()
            batch_generator, nb = minibatch(X_train, self.batchsize, shuffle=True)

            # TODO: parallelize inner loop
            for j, b_ix in enumerate(batch_generator):
                bsize, bstart = len(b_ix), time() #

                X_batch = X_train[b_ix[j]]
                y_real_batch = np.ones_like(self.forward(X_batch))

                y_pred_batch = self.forward(X_batch)
                batch_loss = self.loss(y_pred_batch, y_real_batch)
                self.backward(X_batch, y_pred_batch , y_real_batch)

                loss += batch_loss

                if self.verbose:
                    fstr = "\t[Batch {}/{}] Train loss: {:.3f} ({:.1f}s/batch)"
                    print(fstr.format(j + 1, nb, batch_loss, time() - bstart))

            loss /= nb
            fstr = "[Epoch {}] Avg. loss: {:.3f}  Delta: {:.3f} ({:.2f}m/epoch)"
            print(fstr.format(i + 1, loss, prev_loss - loss, (time() - estart) / 60.0))
            prev_loss = loss

from thunet.neural_nets.utils.testing import (
    random_one_hot_matrix,
    random_stochastic_matrix,
    random_tensor,
)

bert = BERT()
x_train = random_tensor((30, 512, 768), standardize=True)
# y_real_batch = np.ones_like(x_train[0])
bert.fit(x_train)



