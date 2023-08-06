"""Data helper functions."""
import numpy as np
from typing import Tuple, Union

def test_fun(t: Union[np.ndarray,None]=None,
             λ0: float=1,
             λ1: float=1, λ2: float=1/10, λ3: float=1/150, λ4: float=1, λ5: float=1/100,
             λ6: float=1/250, λ7: float=-1, λ8: float=1/100, λ9: float=3000, λ10: float=1/500,
             λ11: float=5000, λ12: float=1/1000, λ13: float=1, λ14: float=0, λ15: float=0) -> Tuple[np.ndarray,np.ndarray]:
    """
    Create univariate test time series.

    Parameters
    ----------
    t : np.ndarray, optional
        Time series time steps for each observation. Array of shape 
        ``(n_observations,)``. If set to ``None``, the default 
        ``t = np.arange(7000)`` is considered.
    λ0 : float, optional
        Test function parameter. The default is 1.
    λ1 : float, optional
        Test function parameter. The default is 1.
    λ2 : float, optional
        Test function parameter. The default is 1/10.
    λ3 : float, optional
        Test function parameter. The default is 1/150.
    λ4 : float, optional
        Test function parameter. The default is 1.
    λ5 : float, optional
        Test function parameter. The default is 1/100.
    λ6 : float, optional
        Test function parameter. The default is 1/250.
    λ7 : float, optional
        Test function parameter. The default is -1.
    λ8 : float, optional
        Test function parameter. The default is 1/100.
    λ9 : float, optional
        Test function parameter. The default is 3000.
    λ10 : float, optional
        Test function parameter. The default is 1/500.
    λ11 : float, optional
        Test function parameter. The default is 5000.
    λ12 : float, optional
        Test function parameter. The default is 1/1000.
    λ13 : float, optional
        Test function parameter. The default is 1.
    λ14 : float, optional
        Test function parameter. The default is 0.
    λ15 : float, optional
        Test function parameter. The default is 0.

    Returns
    -------
    x : np.ndarray
        Time series observations. Array of shape ``(n_observations,)``.
        
    t : np.ndarray
        Time series time steps for each observation. Array of shape 
        ``(n_observations,)``.        
    """
    if t is None:
        t = np.arange(7000)
    x = λ0 * (λ1 * np.sin(t*λ2) * np.exp(-t*λ3) + λ4 * np.cos(t*λ5) * np.exp(-t*λ6) + λ7 * np.sin(t*λ8) * np.exp(-(t-λ9)**2*λ10**2) + (t-λ11)*λ12 * np.heaviside(t-λ11, λ13) + λ14*t + np.sign(λ15)*λ15**2*t**2)
    return x, t
