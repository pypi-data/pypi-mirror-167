"""
Class extending functionality of :obj:`gwpy.timeseries.timeseries.TimeSeries` from GWpy.

Artem Basalaev <artem[dot]basalaev[at]physik.uni-hamburg.de>,
Christian Darsow-Fromm <cdarsowf[at]physnet.uni-hamburg.de>,
Abhinav Patra <patraa1[at]cardiff.ac.uk>
Octavio Vega <ovega84@mitDOTedu>
"""
from warnings import warn
import numpy as np
import gwpy.timeseries
from gwpy.signal import spectral


from spicypy.signal.spectral import daniell

spectral.register_method(daniell)


class TimeSeries(gwpy.timeseries.TimeSeries):
    """
    Class to model signals (time series)

    """

    def csd(self, other, fftlength=None, overlap=None, window="hann", **kwargs):
        """Calculate the CSD `FrequencySeries` for two `TimeSeries`
        Parameters
        ----------
        other : `TimeSeries`
            the second `TimeSeries` in this CSD calculation
        fftlength : `float`
            number of seconds in single FFT. Default behavior:
            * For Daniell averaging method: user-specified value ignored, calculated by the algorithm
            * For other averaging methods: defaults to a single FFT covering the full duration (NOTE:
            this default value does not make sense for most real applications!)
        overlap : `float`, optional
            number of seconds of overlap between FFTs, defaults to the
            recommended overlap for the given window (if given), or 0
        window : `str`, `numpy.ndarray`, optional
            window function to apply to timeseries prior to FFT,
            see :func:`scipy.signal.get_window` for details on acceptable
            formats
        Returns
        -------
        csd :  `~gwpy.frequencyseries.FrequencySeries`
            a data series containing the CSD.
        """

        method_func = spectral.csd
        method = kwargs.pop("method", None)
        if method == "daniell":
            method_func = daniell
        elif method is None:
            # using default GWpy method; in that case, default fftlength will may also be used
            # inform the user of dangers
            if fftlength is None:
                warn(
                    "No 'fftlength' specified, note that in this case single FFT covering whole time series is used"
                )
        else:
            raise NotImplementedError(
                "Only Daniell averaging method is currently implemented in addition to default"
            )

        return spectral.psd(
            (self, other),
            method_func,
            fftlength=fftlength,
            overlap=overlap,
            window=window,
            **kwargs
        )

    def coherence(self, other, fftlength=None, overlap=None, window="hann", **kwargs):
        """Calculate the frequency-coherence between this `TimeSeries`
        and another.
        Parameters
        ----------
        other : `TimeSeries`
            `TimeSeries` signal to calculate coherence with
        fftlength : `float`, optional
            number of seconds in single FFT. Default behavior:
            * For Daniell averaging method: user-specified value ignored, calculated by the algorithm
            * For other averaging methods: defaults to a single FFT covering the full duration (NOTE:
            this default value does not make sense for most real applications!)
        overlap : `float`, optional
            number of seconds of overlap between FFTs, defaults to the
            recommended overlap for the given window (if given), or 0
        window : `str`, `numpy.ndarray`, optional
            window function to apply to timeseries prior to FFT,
            see :func:`scipy.signal.get_window` for details on acceptable
            formats
        **kwargs
            any other keyword arguments accepted by
            :func:`matplotlib.mlab.cohere` except ``NFFT``, ``window``,
            and ``noverlap`` which are superceded by the above keyword
            arguments
        Returns
        -------
        coherence : `~gwpy.frequencyseries.FrequencySeries`
            the coherence `FrequencySeries` of this `TimeSeries`
            with the other
        Notes
        -----
        If `self` and `other` have difference
        :attr:`TimeSeries.sample_rate` values, the higher sampled
        `TimeSeries` will be down-sampled to match the lower.
        See also
        --------
        scipy.signal.coherence
            for details of the coherence calculator
        """

        method = kwargs.pop("method", None)

        if method == "daniell":
            csd = spectral.psd(
                (self, other),
                method_func=daniell,
                fftlength=fftlength,
                overlap=overlap,
                window=window,
                **kwargs
            )
            psd1 = spectral.psd(
                self,
                method_func=daniell,
                fftlength=fftlength,
                overlap=overlap,
                window=window,
                **kwargs
            )
            psd2 = spectral.psd(
                other,
                method_func=daniell,
                fftlength=fftlength,
                overlap=overlap,
                window=window,
                **kwargs
            )
            return np.abs(csd) ** 2 / psd1 / psd2
        elif method is None:
            # using default GWpy method; in that case, default fftlength will may also be used
            # inform the user of dangers
            if fftlength is None:
                warn(
                    "No 'fftlength' specified, note that in this case single FFT covering whole time series is used"
                )

            return spectral.psd(
                (self, other),
                spectral.coherence,
                fftlength=fftlength,
                overlap=overlap,
                window=window,
                **kwargs
            )
        else:
            raise NotImplementedError(
                "Only Daniell averaging method is currently implemented in addition to default"
            )
