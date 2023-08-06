"""Extract principal FFT components for features generation"""

# Module imports
import torch
import numpy as np


class PFT:
    """Extract principal FFT components for features generation"""
    def __init__(self, n_components, use_torch=True, norm="ortho"):
        self.n_components = n_components
        self.original_size = 0
        self.idx = None
        self.use_torch = use_torch
        self.norm = norm

    def fit(self, X):
        """Fit data (find the n top components of the FT)"""

        # Selects the correct library
        lib = torch if self.use_torch else np

        # Extracts top N components from the Fourier Transformation
        Xfft = lib.fft.rfft(X, norm=self.norm)
        self.original_size = Xfft.shape[1]
        Xabs = lib.abs(Xfft)

        if self.use_torch:
            Xabs_norm = Xabs / Xabs.max(axis=1)[0].unsqueeze(1)
        else:
            Xabs_norm = Xabs / Xabs.max(axis=1).reshape(-1, 1)

        Xabs_norm = lib.sum(Xabs_norm, 0)

        if self.use_torch:
            self.idx = torch.argsort(Xabs_norm, descending=True)[:self.n_components]
        else:
            self.idx = np.flip(np.argsort(Xabs_norm))[:self.n_components]

        return self

    def rfft(self, freq):
        """Reconstructs the real Fourier transform for frequency values"""
        assert self.idx is not None, "PrincipalFFT instance not fitted"
        lib = torch if self.use_torch else np


        rfft = lib.zeros((freq.shape[0], self.original_size), dtype=lib.complex64)
        rfft[:, self.idx] = freq

        return rfft

    def ifit(self, freq, t):
        """Returns the transient signal from principal Fourier coefficients"""
        assert self.idx is not None, "PrincipalFFT instance not fitted"
        lib = torch if self.use_torch else np

        rfft = self.rfft(freq)

        return  lib.fft.irfft(rfft, len(t), norm=self.norm)

    def transform(self, X):
        """Transform data"""
        assert self.idx is not None, "PrincipalFFT instance not fitted"
        lib = torch if self.use_torch else np
        return lib.fft.rfft(X, norm=self.norm)[:, self.idx]
