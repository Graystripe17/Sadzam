# Sadzam

A slow version of the Shazam algorithm implemented in Python. Work in progress.

## Why

This algorithm is extremely elegant in my opinion. 
It starts with the simple question "How do you search audio?"
But it must also handle noise, use a short sample, and be lightning fast.
The algorithm solves these through filtering, windowing, and FFTs.

Importantly, it doesn't use neural nets or "machine learning".

### How it works

1. Read in audio file
2. Convert from stereo to mono
3. Low pass filter (butterworth)
4. Downsample
5. Hanning window in 0.1s intervals 
6. FFT and sort into (logarithmic) bins *IN PROGRESS*
7. Save "loudest" frequencies into spectrogram
8. Create ordering of points
9. For each "target" point, calc distance from neighboring cluster
10. Save as keys in dict pointing to songID

## Running the tests

pytest

## Acknowledgments

* https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf
* http://coding-geek.com/how-shazam-works/
* Lots and lots of wikipedia
