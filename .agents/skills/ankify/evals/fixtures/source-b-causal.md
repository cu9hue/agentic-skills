# Reading notes: He et al. 2015, "Deep Residual Learning for Image Recognition"

Plain deep networks got *worse* with depth — a 56-layer net had higher training
error than a 20-layer one. That is not overfitting, since training error rose
too. The paper calls this the degradation problem: solvers struggle to make a
stack of nonlinear layers approximate the identity, even though an identity
mapping would let a deeper net match a shallower one exactly.

The fix reframes what a block must learn. Instead of fitting a target mapping
H(x) directly, a block fits the residual F(x) = H(x) - x, and the output is
F(x) + x via a skip connection. If the useful thing to do is nothing, the solver
only has to push F toward zero, which is easy. Figure 3 in the paper shows the
plain and residual architectures side by side; Figure 4 plots training curves
for both at 18 and 34 layers.

The skip path also changes gradient flow. Because the identity branch has a
derivative of 1, gradients reach early layers without being multiplied through
every intervening weight matrix, so they neither vanish nor explode as fast.

Identity shortcuts are parameter-free, which matters for the comparison: the
residual net has the same parameter count and roughly the same FLOPs as the
plain net it is compared against, so the gain cannot be attributed to capacity.
ResNet-152 reached 3.57% top-5 error on ImageNet and won ILSVRC 2015.

When dimensions change across a block, the paper tests a projection shortcut
(a 1x1 convolution) versus zero-padding the identity. Projections help slightly,
but the authors keep identity shortcuts as the default because the gain does not
justify the added parameters.
