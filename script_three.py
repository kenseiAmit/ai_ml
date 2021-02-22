import scipy.io.wavfile
import matplotlib.pyplot
import urllib.request
import numpy as np

response = urllib.request.urlopen("http://www.thesoundarchive.com/autinpowers/smashingbaby.wav")
print(response.info())
filehandle = open("smashingbaby.wav", "w")
filehandle.write(response.content())
filehandle.close()
sample_rate, data = scipy.io.wavfile.read("smashingbaby.wav")
print(data.dtype, data.shape)
plt.subplot(2,1,1)
plt.title("Original")
plt.plot(data)