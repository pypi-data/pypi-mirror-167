# PyTortto

This is a pytorch style machine learning framework implemented entirely in numpy, with GPU acceleration from cupy.

Similar to the pokemon "ditto", pytortto works exactly like pytorch, although inferior in terms of speed. The purpose of this project is to understand how pytorch, or how general machine learning algorithms work under the hood. Max effort was given to correctness, calculation efficiency (like simpler Jacobian in logsoftmax, efficient implementation of convolution etc.), numerical stability (log-sum-exp used in logsigmoid, BCEWithLogitsLoss etc.), and memory efficiency (implementation of caching, view etc.).  

When compared in GPU, Tortto is around 1.5(vision transformers) ~ 3(CNNs) times slower than pytorch. It also achieves the same complexity as pytorch, which means tortto can be used to train relatively larger models such as `resnet101` and vision transformer `ViT-B/16` with same speed ratio.

Tortto implements reverse mode automatic differentiation and supports dynamic computation graph like pytorch.

**For more information, please visit its github page [here](https://github.com/samrere/pytortto)**
