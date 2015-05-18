import rawpy, matplotlib.pyplot as plt, numpy as np

path='tree.exif.dng'
raw=rawpy.imread(path)
print 'Sizes of the image:',raw.sizes
print 'Bayer pattern:\n',raw.raw_pattern
print 'Indices 0,1,2,3 in above are, in order: ',raw.color_desc
print 'camera_whitebalance',raw.camera_whitebalance
print 'daylight_whitebalance',raw.daylight_whitebalance
##note the two following methods are (y,x) - annoying!
print 'Colour of bayer pixel at 101,100:',raw.raw_color(101,100)
print 'Value of bayer pixel at 101,100:',raw.raw_value(101,100)

nx=raw.raw_image.shape[1]
ny=raw.raw_image.shape[0]
ris=raw.raw_image.astype(float)
rismax=ris.max()

#Make an rgb bayer image
rgb=np.zeros((ny,nx,3), 'float')
rgb[1::2,0::2,0]=ris[1::2,0::2]/rismax
rgb[0::2,0::2,1]=ris[0::2,0::2]/rismax
rgb[1::2,1::2,1]=ris[1::2,1::2]/rismax
rgb[0::2,1::2,2]=ris[0::2,1::2]/rismax

plt.imshow(rgb, interpolation='none')
plt.show()

#Perform a half-resolution demosaic
rgbi=np.zeros((ny/2,nx/2,3), 'float')
rgbi[::,::,0]=ris[1::2,0::2]/rismax
rgbi[::,::,1]=0.5*(ris[0::2,0::2]+ris[1::2,1::2])/rismax
rgbi[::,::,2]=ris[0::2,1::2]/rismax

#print rgbi.max()

#imgplot=plt.imshow(rgbi, interpolation='none')
#plt.show()

