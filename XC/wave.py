from scipy.io.wavfile import read
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal, stats

def plotXC(signals):
    print(signals)
    assert False
    plt.plot(correlate, label="correlate")
    plt.legend(loc='upper center')
    plt.show()


if __name__ == "__main__":
    original = read("oblivion.wav")
    original_z = stats.zscore(np.array(original[1], dtype=float))
    sample = read("oblivion.cut.wav")
    sample_z = stats.zscore(np.array(sample[1], dtype=float))

    noise_s = np.random.normal(0, 1, sample_z.shape)

    correlate = signal.correlate(original_z, sample_z + noise_s, mode="full", method="fft")
    X_axis = np.arange(sample_z)
    signals = [
        {'name': 'original', 'x': X_axis, 'y': original_z, 'color': 'r'},
        {'name': 'sample', 'x': X_axis, 'y': noise_z, 'color': 'b'},
    ]

    fig, ax = plt.subplots()
    for signal in signals:
        ax.plot(signal['x'], signal['y'],
                color=signal['color'],
                label=signal['name'])

    assert False
    plotXC(signals)
