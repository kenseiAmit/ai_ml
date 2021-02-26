import scipy.io.wavfile
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import os
#
# response = urllib.request.urlopen("http://www.thesoundarchive.com/autinpowers/smashingbaby.wav")
# print(response.info())
# filehandle = open("smashingbaby.wav", "w")
# filehandle.write(response.content())
# filehandle.close()
path = os.path.join("~", "Documents", "coding", "greatLearnings", "resources", "audio", "smashigbaby.wav")
sample_rate, data = scipy.io.wavfile.read("smashigbaby.wav")
print(data.dtype, data.shape)
plt.subplot(2,1,1)
plt.title("Original")
plt.plot(data)
plt.subplot(2,1,2)
plt.title("Quite")
plt.plot(data**2)
plt.savefig("aplot.png")
