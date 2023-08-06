"""Toolbox for multivariate time series segmentation."""
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.base import TransformerMixin
from typing import List, Tuple, Union, Callable
from pytseg.seg import cut, segmentize, segment_stationarity

def normalize_multi(X: np.ndarray, t: Union[np.ndarray,None],
                    scaler: TransformerMixin=MinMaxScaler()) -> Tuple[np.ndarray, np.ndarray]:      
    """
    Normalize a multivariate time series: evenly spaced and rescaled data.

    Parameters
    ----------
    X : np.ndarray
        Time series observations. Array of shape 
        ``(n_observations, n_series)``.
    t : Union[np.ndarray,None]
        Time series time steps for each observation. Array of shape 
        ``(n_observations,)``. If set to ``None``, the default 
        ``t = np.arange(X.shape[0])`` is considered.
    scaler : sklearn.base.TransformerMixin
        Rescaler for ``X``. The default is ``MinMaxScaler()``.

    Returns
    -------
    X : np.ndarray
        Normalized and evenly spaced time series observations.
    t : np.ndarray
        Evenly spaced time series time steps.
    """
    
    # verify
    if t is None:
        t = np.arange(X.shape[0])
    else:
        assert X.shape[0]==t.size
      
    # make evenly spaced
    if np.any(np.diff(t)!=np.diff(t)[0]):
        t_tf = np.linspace(np.min(t), np.max(t), t.size)
        X_tf = np.array([np.interp(t, t_tf, x.T) for x in X.T])
        X, t = np.asarray(X_tf), np.asarray(t_tf)
    
    # rescale
    X = scaler.fit_transform(X)
    
    # return results
    return X, t

def cut_multi(X: np.ndarray, alpha: float=.95, l0: float=3) -> List[np.ndarray]:      
    """
    Cut a multivariate time series, see ``seg.cut``.

    Parameters
    ----------
    X : np.ndarray
        Time series observations to cut. Array of shape 
        ``(n_observations, n_series)``.
    alpha : float, optional
        Significance Threshold. The default is .95.
    l0 : float, optional
        Minimum segment length, has to be 3 or more. The default is 3.

    Returns
    -------
    S : List[np.ndarray]
        List of arrays of segment indices for ``X``.

    """
    
    S = [cut(x.T, alpha, l0) for x in X.T]
    return S

def segmentize_multi(A: np.ndarray, S: List[np.ndarray]) -> List[List[np.ndarray]]:    
    """
    Get list of array segments from segment index list, see ``seg.segmentize``.

    Parameters
    ----------
    A : np.ndarray
        Arrays to segment: (n_arrays, n_elements).
    S : List[np.ndarray]
        List of arrays of segment indices for ``A`` (from ``cut_multi``).

    Returns
    -------
    A_seg : List[List[np.ndarray]]
        List of array segments (as list of results from ``seg.segmentize``).
    """
    
    A_seg = [segmentize(a, s) for a,s in zip(A, S)]
    return A_seg   

def joint_labels_multi(t: np.ndarray, S: List[np.ndarray],
                       labels_multi: List[np.ndarray],
                       joint_label_fun: Callable[[list],float]) -> Tuple[np.ndarray,np.ndarray]:
    """
    Join labels/segments from multiple time series into one label/segment 
    series.

    Parameters
    ----------
    t : np.ndarray
        Time series time steps for each observation.
    S : List[np.ndarray]
        List of arrays of segment indices for ``t`` (from ``cut_multi``).
    labels_multi : List[np.ndarray]
        List of label arrays.
    joint_label_fun : Callable[[list],float]
        Function to join labels from multiple observations into one joint
        label.

    Returns
    -------
    s : np.ndarray
         Array of segment indices for ``t``.
    l : np.ndarray
        Array of labels for ``t``.
    """
    # TODO: more efficient implementation
 
    T_seg = [segmentize(t, s) for s in S]
    T_range = [np.array([[np.min(t), np.max(t)] for t in t_seg]) for t_seg in T_seg]    
    
    # build label
    labels = np.empty(t.size)
    for idx in range(t.size):
        labels_idx = []
        for s_idx in range(len(labels_multi)):
            for r_idx, r in enumerate(T_range[s_idx]):
                if r[0] <= idx and r[1] >= idx:
                    break
            labels_idx.append(labels_multi[s_idx][r_idx])
        labels[idx] = joint_label_fun(labels_idx)
        
    # extract segments and labels
    current_label = None
    s: list = []
    l: list = []
    for idx in range(labels.size):
        l_ = labels[idx]
        if current_label is None:
            current_label = l_
        elif l_ != current_label:
            s.append(idx)
            l.append(current_label)
            current_label = l_
        elif idx == labels.size-1:
            l.append(current_label)
    s_ = np.array(s).astype(int)
    l_ = np.array(l)
            
    return s_, l_

def segment_stationarity_multi(X: np.ndarray,
                               S: List[np.ndarray],
                               t: Union[np.ndarray,None]=None,
                               threshold: float=.025) -> Tuple[np.ndarray,np.ndarray]:
    """
    Identify stationarity for a segmented multivariate time series.

    Parameters
    ----------
    X : np.ndarray
        Time series observations to cut. Array of shape 
        ``(n_observations, n_series)``.
    S : List[np.ndarray]
        List of arrays of segment indices for ``X`` (from ``cut_multi``).
    t : Union[np.ndarray,None], optional
        Time series time steps for each observation. Array of shape 
        ``(n_observations,)``. If set to ``None``, the default 
        ``t = np.arange(X.shape[0])`` is considered. The default is ``None``.
    threshold : float, optional
        Stationarity threshold, see ``seg.segment_stationarity``. The default 
        is .025.

    Returns
    -------
    s : np.ndarray
         Array of segment indices for ``t``.
    l : np.ndarray
        Array of labels for ``t``.
    """
    
    if t is None:
        t = np.arange(X.shape[0])
        
    labels_multi = [segment_stationarity(x.T, s, threshold) for x,s in zip(X.T,S)]
    
    s, l = joint_labels_multi(t, S, labels_multi, joint_label_fun=np.all)
    l = l.astype(bool)
            
    return s, l
        