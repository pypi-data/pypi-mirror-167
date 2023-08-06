# Principal Fourier Transformation (PFT)

~~An implementation~~ A complete overhaul of https://github.com/eloquentarduino/principal-fft for pytorch.

Extracts the principal Fourier Transform Components.
That is, for a set of signal data, PFT will extract the top N components for the whole dataset.

TL;DR: Principal Component Analysis (PCA) for Fourier Space.

## Installation

With pip...
```
pip install pft
```

## Usage

```python
# Lets say you've a dataset of transient signal data
# For now, lets construct our own dataset with a single signal.

# The signal will be a composite of many sine functions
num_steps = 100 # Number of temporal steps
num_coefs = 100 # Number of sine functions that make up our composite signal
coefs = torch.rand(num_coefs) * torch.linspace(0, 1, num_steps)
freqs = torch.rand(num_coefs) * 2 * torch.pi

# Don't forgot the leading dimension!
# pft expects the data to have the shape (num_of_data_samples, num_of_time_steps)
signal = torch.zeros((1, num_steps)) 
for i, coef in enumerate(coefs):
	signal += coef * torch.sin(freqs[i] * t)

# Now lets extract 10 prinicipal Fourier coefficients
import pft

num_pfc = 10 # Number of principal Fourier coefficients
pfa = pft.PFT( # pfa = Principal Fourier Analysis
	num_pfc,
	use_torch=True, # Change to False to use numpy backend. Default is True.
	norm="ortho",	# Forward and Inverse Foureir Transform normalisation. Defaults to "ortho".
) 
pfa.fit(signal) # Calculates the prinicipal Fourier coefficients indexes.
pfc = pfa.transform(signal) # Gets the principal Fourier coefficients for this set of signals.

# The indexes of the prinicipal Fourier coefficients are stored internally.
# To get from the principal Fourier coefficients back to the transient signal
# do the following:

reconstructed_signal = pfa.ifit(pfc)
```
