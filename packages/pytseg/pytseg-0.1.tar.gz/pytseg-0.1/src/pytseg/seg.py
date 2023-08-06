"""Toolbox for univariate time series segmentation."""
import numpy as np
from scipy import special
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.base import TransformerMixin
from typing import List, Tuple, Union, Callable, Any

def normalize(x: np.ndarray, t: Union[np.ndarray,None],
              scaler: TransformerMixin=MinMaxScaler()) -> Tuple[np.ndarray, np.ndarray]:  
    """
    Normalize a time series: evenly spaced and rescaled data.
    
    Parameters
    ----------
    x : np.ndarray
        Time series observations. Array of shape ``(n_observations,)``.
    t : Union[np.ndarray,None]
        Time series time steps for each observation. Array of shape 
        ``(n_observations,)``. If set to ``None``, the default 
        ``t = np.arange(x.size)`` is considered.
    scaler : sklearn.base.TransformerMixin
        Rescaler for ``x``. The default is ``MinMaxScaler()``.

    Returns
    -------
    X : np.ndarray
        Normalized and evenly spaced time series observations.
    t : np.ndarray
        Evenly spaced time series time steps.
    """
    
    # verify
    if t is None:
        t = np.arange(x.size)
    else:
        assert x.size==t.size
      
    # make evenly spaced
    if np.any(np.diff(t)!=np.diff(t)[0]):
        t_tf = np.linspace(np.min(t), np.max(t), t.size)
        x_tf = np.interp(t, t_tf, x)
        x, t = np.asarray(x_tf), np.asarray(t_tf)
    
    # rescale
    x = scaler.fit_transform(x.reshape(-1,1)).ravel()
    
    # return results
    return x, t
   
def cut(x: np.ndarray, alpha: float=.95, l0: float=3) -> np.ndarray:
    """
    Cut a univariate time series into a set of distinguishable segments. This 
    algorithm closely follows "Heuristic segmentation of a nonstationary time 
    series", Fukuda et al. (2004).

    Parameters
    ----------
    x : np.ndarray
        Time series observations to cut. Array of shape ``(n_observations,)``.
    alpha : float, optional
        Significance Threshold. The default is .95.
    l0 : float, optional
        Minimum segment length, has to be 3 or more. The default is 3.

    Returns
    -------
    s : np.ndarray
        Array of segment indices for ``x``.
    """
    
    # verify
    splits = np.array([], dtype=np.int64)
    N = x.size
    min_size = max(int(l0),3) # set size to 3 or more, otherwise var = 0 so that sd = 0 and thus st = nan
    if N <= 2*min_size+1: # check if time series length is sufficient for segmentation
        return splits

    # build st array
    st = np.empty(N-2*min_size+1)
    for idx in range(min_size,N-min_size+1):
        l = x[:idx]
        r = x[idx:]
        n_l = l.size
        n_r = r.size
        mu_l = np.mean(l)
        mu_r = np.mean(r)
        var_l = np.var(l)
        var_r = np.var(r)    
        sd = np.sqrt(((n_l-1)*var_l+(n_r-1)*var_r)/(n_l+n_r-2))*np.sqrt(1/n_l+1/n_r)
        if sd > 0:
            st[idx-min_size] = np.abs((mu_l-mu_r)/sd)
        else:
            st[idx-min_size] = 0

    # approximate significance
    st_idx = np.argmax(st)
    stm = st[st_idx]
    nu = N-2
    beta_x = nu/(nu+stm**2)
    eta = 4.19*np.log(N)-11.54
    delta = .4
    P = (1-special.betainc(delta*nu,delta,beta_x))**eta
    
    # perform recursive cutting
    cut_idx = int(st_idx + min_size)
    cut_decision = P >= alpha
    if cut_decision:
        splits = np.append(splits, [cut_idx])
        if cut_idx >= min_size: # left sub-series
            splits = np.append(splits, cut(x[:cut_idx], alpha, l0))
        if cut_idx <= N-min_size: # right sub-series
            splits = np.append(splits, cut(x[cut_idx:], alpha, l0)+cut_idx)
    s = np.sort(splits)
    return s

def segmentize(a: np.ndarray, s: np.ndarray) -> List[np.ndarray]:
    """
    Get list of array segments from segment indices.

    Parameters
    ----------
    a : np.ndarray
        Array to segment.
    s : np.ndarray
        Array of segment indices for ``a`` (from ``cut``).

    Returns
    -------
    a_seg : np.ndarray
        List of array segments.
    """
    
    concat: Any = ([0], s, [a.size])
    steps: np.ndarray = np.concatenate(concat)
    a_seg = [a[steps[idx]:steps[idx+1]] for idx in range(len(steps)-1)]
    return a_seg
        
def segment_stationarity(x: np.ndarray, s: np.ndarray, threshold: float=.01) -> np.ndarray:
    """
    Identify stationarity for a segmented univariate time series.

    Parameters
    ----------
    x : np.ndarray
        Time series observations.
    s : np.ndarray
        Array of segment indices for ``x`` (from ``cut``).
    threshold : float, optional
        Stationarity threshold: stationarity is identified if the standard 
        deviation of a segment is smaller than (or equal to) 
        ``threshold * std``, where ``std`` is the standard deviation of the 
        whole time series. The default is .01.

    Returns
    -------
    labels : np.ndarray
        Array of labels (``True``: stationary or ``False``: non-stationary).
    """
    
    x_seg = segmentize(x, s)
    std = np.std(x)
    labels = np.array([np.std(x_) <= threshold * std for x_ in x_seg]).astype(bool)
    return labels
 
def segment_clustering(x: np.ndarray, s: np.ndarray,
                       n_clusters: int=2, random_state: Union[int,np.random.mtrand.RandomState]=0,
                       kmeans_kwarg_dict: dict={},
                       feature_maps: List[Callable[[np.ndarray], float]]=[np.mean, np.std],
                       feature_scaler: TransformerMixin=StandardScaler()) -> np.ndarray:
    """
    Perform clustization for a segmented univariate time series using 
    ``sklearn.cluster.KMeans``.

    Parameters
    ----------
    x : np.ndarray
        Time series observations.
    s : np.ndarray
        Array of segment indices for ``x`` (from ``cut``).
    n_clusters : int, optional
        Number of clusters to consider. The default is 2.
    random_state : Union[int,np.random.mtrand.RandomState], optional
        Random seed (or state) of the clustering algorithm. The default is 0.
    kmeans_kwarg_dict : dict, optional
        Optional keyword arguments for ``KMeans``. The default is ``{}``.
    feature_maps : List[Callable[[np.ndarray], float]], optional
        Feature maps: each segment is mapped to a float. The default is 
        ``[np.mean, np.std]``.
    feature_scaler : sklearn.base.TransformerMixin, optional
        Rescaler for all features. The default is ``StandardScaler()``.

    Returns
    -------
    labels : np.ndarray
        Array of labels (cluster index).

    """
    x_seg = segmentize(x, s)
    f_seg = np.array([[feature_map(x_) for feature_map in feature_maps] for x_ in x_seg])
    if feature_scaler is not None:
        f_seg = feature_scaler.fit_transform(f_seg)
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, **kmeans_kwarg_dict).fit(f_seg)
    return np.asarray(kmeans.labels_)
