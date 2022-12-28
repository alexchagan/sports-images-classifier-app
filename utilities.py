import tensorflow as tf

def load_image(path, image_size=(224, 224), num_channels=3, interpolation='bilinear'):
  """Load an image from a path and resize it."""
  img = tf.io.read_file(path)
  img = tf.image.decode_image(img, channels=num_channels, expand_animations=False)
  img = tf.image.resize(img, image_size, method=interpolation)
  img.set_shape((image_size[0], image_size[1], num_channels))
  return img