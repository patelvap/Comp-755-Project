import tensorflow.compat.v1 as tf
tf.compat.v1.disable_v2_behavior()

def dirichlet_likelihood(weights, alpha=None):
    n_topics = weights.get_shape()[1].value
    if alpha is None:
        alpha = 1.0 / n_topics
    log_proportions = tf.nn.log_softmax(weights)
    loss = (alpha - 1.0) * log_proportions
    return tf.math.reduce_mean(loss)

# NEW
def regularization(embed, topics):
    center = embed - tf.reshape(tf.reduce_mean(embed,1),[topics,1])
    cov = tf.linalg.matmul(center, tf.transpose(center))
    tf.linalg.set_diag(cov,tf.ones((topics,)))
    reg = tf.math.log(tf.linalg.det(cov))
    return tf.math.abs(reg)
