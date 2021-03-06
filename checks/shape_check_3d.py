import numpy as np

ip_shape = (10, 8, 5, 4, 20)
batch, d, w, h, c = ip_shape
ip = np.ones(ip_shape, dtype='float32')

# 3D conv

xx_ones = np.ones([batch, h], dtype='int32')
xx_ones = np.expand_dims(xx_ones, axis=-1)
print('xx expand dims', xx_ones.shape)

xx_range = np.tile(np.expand_dims(np.arange(0, w), axis=0),
                   [batch, 1])
print('xx range', xx_range.shape)
xx_range = np.expand_dims(xx_range, axis=1)
print('xx range expand dims', xx_range.shape)

xx_channels = np.matmul(xx_ones, xx_range)
print('xx channels', xx_channels.shape)
xx_channels = np.expand_dims(xx_channels, axis=-1)
xx_channels = np.transpose(xx_channels, [0, 2, 1, 3])
print('xx channels expand dims', xx_channels.shape, )

xx_channels = np.expand_dims(xx_channels, axis=1)
xx_channels = np.tile(xx_channels,
                      [1, d, 1, 1, 1])
print('xx channels final', xx_channels.shape)

print()

yy_ones = np.ones([batch, w], dtype='int32')
yy_ones = np.expand_dims(yy_ones, axis=1)
print('yy expand dims', yy_ones.shape)

yy_range = np.tile(np.expand_dims(np.arange(0, h), axis=0),
                   [batch, 1])
print('yy range', yy_range.shape)
yy_range = np.expand_dims(yy_range, axis=-1)
print('yy range expand dims', yy_range.shape)

yy_channels = np.matmul(yy_range, yy_ones)
print('yy channels', yy_channels.shape)
yy_channels = np.expand_dims(yy_channels, axis=-1)
yy_channels = np.transpose(yy_channels, [0, 2, 1, 3])
print('yy channels expand dims', yy_channels.shape)

yy_channels = np.expand_dims(yy_channels, axis=1)
yy_channels = np.tile(yy_channels,
                      [1, d, 1, 1, 1])
print('yy channels final', yy_channels.shape)

print()

zz_range = np.tile(np.expand_dims(np.arange(0, d), axis=0),
                   [batch, 1])
print('zz range', zz_range.shape)
zz_range = np.expand_dims(zz_range, axis=-1)
zz_range = np.expand_dims(zz_range, axis=-1)

print('zz range expand dims', zz_range.shape)

zz_channels = np.tile(zz_range,
                      [1, 1, w, h])
print('zz channels', zz_channels.shape)
zz_channels = np.expand_dims(zz_channels, axis=-1)
print('zz channels expand dims', zz_channels.shape)

final = np.concatenate([ip, zz_channels, xx_channels, yy_channels], axis=-1)

print("final", final.shape)
print(final[0])
