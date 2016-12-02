from PIL import Image
import PIL
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft.fftpack import fft2, ifft2, fftn, ifftn
import matplotlib.image as mpimg

def saveImage( npdata, outFileName ) :
    img = Image.fromarray( np.asarray( np.clip(npdata,0,255), dtype="uint8"), "L" )
    img.save( outFileName )

fileName = input("Insert file name(with extension): ")
img = mpimg.imread(fileName)
imgData = img[:,:,0:3]
orgWidth, orgHeight, dim = imgData.shape

#fftImg = fftn(imgData)
fftImg = np.zeros_like(imgData, "complex")
fftImg[:,:,0] = fft2(imgData[:,:,0])
fftImg[:,:,1] = fft2(imgData[:,:,1])
fftImg[:,:,2] = fft2(imgData[:,:,2])
R, G, B = input("Insert 3 numbers representing % of each color to be removed\n(eg. R, G, B seperate with colons, space not necessary):  ").split(',')
compR = int(int(R)/2)
compG = int(int(G)/2)
compB = int(int(B)/2)

width = int(orgWidth/2)
height = int(orgHeight/2)

compRW = int(orgWidth*(compR/100))
compGW = int(orgWidth*(compG/100))
compBW = int(orgWidth*(compB/100))
compRH = int(orgHeight*(compR/100))
compGH = int(orgHeight*(compG/100))
compBH = int(orgHeight*(compB/100))

#clamp these values
lowRW = width-compRW
highRW = width+compRW
lowRH = height-compRH
highRH = height+compRH

lowGW = width-compGW
highGW = width+compGW
lowGH = height-compGH
highGH = height+compGH

lowBW = width-compBW
highBW = width+compBW
lowBH = height-compBH
highBH = height+compBH
#

fftImg[lowRW:highRW,:, 0] = 0
fftImg[:,lowRH:highRH, 0] = 0
fftImg[lowGW:highGW,:, 1] = 0
fftImg[:,lowGH:highGH, 1] = 0
fftImg[lowBW:highBW,:, 2] = 0
fftImg[:,lowBH:highBH, 2] = 0

#ifftImg = ifftn(fftImg)
ifftImg = np.zeros_like(fftImg, "complex")
ifftImg[:,:,0] = ifft2(fftImg[:,:,0])
ifftImg[:,:,1] = ifft2(fftImg[:,:,1])
ifftImg[:,:,2] = ifft2(fftImg[:,:,2])
plt.figure(1)
plt.subplot(121)
plt.title('before')
plt.imshow(img)
plt.subplot(122)
plt.title(str('after - Red '+ str(G)+ '%\nGreen '+str(G)+ '%\nBlue '+str(B)+'%'))
plt.imshow(abs(ifftImg))
plt.show()

"""
plotR = np.array(img[:,:,0:3])
plotG = np.array(img[:,:,0:3])
plotB = np.array(img[:,:,0:3])
plotR[:,:,1:3]=0
plotG[:,:,0:3:2]=0
plotB[:,:,0:2]=0

plt.figure(2)
plt.subplot(221)
plt.imshow(plotR)

plt.subplot(222)
plt.imshow(plotG)

plt.subplot(223)
plt.imshow(plotB)

plt.subplot(224)
plt.imshow(imgData)
plt.show()
"""
