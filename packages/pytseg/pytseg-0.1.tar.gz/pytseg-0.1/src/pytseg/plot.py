"""Plotting helper functions."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from typing import List, Union, Any
from pytseg.seg import segmentize

def plot(x: np.ndarray,
         s: Union[np.ndarray,None]=None,
         t: Union[np.ndarray,None]=None,
         l: Union[np.ndarray,None]=None,
         cmap: str='brg',
         figure_kwarg_dict: dict ={}, plot_kwarg_dict: dict={},
         new_fig_: bool=True, show_legend_: bool=False, show_fig_: bool=True) -> None:
    """
    Plot univariate time series.

    Parameters
    ----------
    x : np.ndarray
        Time series observations.
    s : Union[np.ndarray,None], optional
        Array of segment indices for ``x`` (from ``seg.cut``). If set to
        ``None``, no segments are considered. The default is ``None``.
    t : Union[np.ndarray,None], optional
        Time series time steps for each observation. If set 
        to ``None``, the default ``t = np.arange(x.size)`` is considered. The 
        default is ``None``.
    l : Union[np.ndarray,None], optional
        Array of labels for each segment in ``s``. If set to ``None``, no 
        labels are considered. The default is ``None``.
    cmap : str, optional
        Color map name for plotting different segments. The default is 
        ``'brg'``.
    figure_kwarg_dict : dict, optional
        Additional keyword arguments for the figure. The default is ``{}``.
    plot_kwarg_dict : dict, optional
        Additional keyword arguments for the plots. The default is ``{}``.
    new_fig_ : bool, optional
        Create new figure. Inteded for internal use. The default is ``True``.
    show_legend_ : bool, optional
        Show legend. Inteded for internal use. The default is ``False``.
    show_fig_ : bool, optional
        Show figure. Inteded for internal use. The default is ``True``.

    Returns
    -------
    None.
    """
    
    # preprocess
    if t is None:
        t = np.arange(x.size)
    if l is not None:
        assert s is not None
        num_labels = np.unique(l).size
        cmap_obj = cm.get_cmap(cmap)
        c = {l_: cmap_obj(l_/(num_labels-1)) for l_ in np.unique(l)}

    # plot
    if new_fig_:
        plt.figure(**figure_kwarg_dict)
    if s is not None: # segmentized
        x_seg = segmentize(x, s)
        t_seg = segmentize(t, s)
    
        # plot segments
        for idx in range(len(x_seg)):
            x_ = x_seg[idx]
            t_ = t_seg[idx]
            if idx != len(x_seg)-1:
                x_ = np.append(x_, x_seg[idx+1][0])
                t_ = np.append(t_, t_seg[idx+1][0])
            if l is not None:
                l_ = l[idx]
                c_ = c[l_]
                plt.plot(t_, x_, c=c_, **plot_kwarg_dict)
            else:
                plt.plot(t_, x_, **plot_kwarg_dict)
    else: # not segmentized
        plt.plot(t, x, **plot_kwarg_dict)
    if show_legend_:
        plt.legend()
    if show_fig_:
        plt.xlabel('t')
        plt.ylabel('x(t)')
        plt.show()
    
def plot_multi(X: np.ndarray,
               S: Union[List[np.ndarray],None]=None,
               t: Union[np.ndarray,None]=None,
               L: Union[List[np.ndarray],None]=None,
               cmap: str='brg', figure_kwarg_dict: dict={}, plot_kwarg_dict: dict={},
               label: Union[str,None]=None) -> None:
    """
    Plot multivariate time series.

    Parameters
    ----------
    X : np.ndarray
        Time series observations.
    S : Union[List[np.ndarray],None], optional
        List of segment index arrays for ``X`` (from ``seg_multi.cut_multi``). 
        If set to ``None``, no segments are considered. The default is 
        ``None``.
    t : Union[np.ndarray,None], optional
        Time series time steps for each observation. If set to ``None``, the 
        default in ``plot`` is considered. The default is ``None``.
    L : Union[List[np.ndarray],None], optional
        List of label arrays for each segment in ``S``. If set to ``None``, no 
        labels are considered. The default is ``None``.
    cmap : str, optional
        Color map name for plotting different segments. The default is 
        ``'brg'``.
    figure_kwarg_dict : dict, optional
        Additional keyword arguments for the figure. The default is ``{}``.
    plot_kwarg_dict : dict, optional
        Additional keyword arguments for the plots. The default is ``{}``.
    label : Union[str,None], optional
        Label prefix for legend. If set to ``None``, no legend is shown. The 
        default is ``None``.

    Returns
    -------
    None.
    """
    if S is None:
        S_: List[Any] = [None]*X.shape[0]
    else:
        S_ = S.copy()
    if L is None:
        L_: List[Any] = [None]*X.shape[0] 
    else:
        L_ = L.copy()
    for idx, (x, s, l) in enumerate(zip(X.T, S_, L_)):
        plot(x.T, s=s, t=t, l=l, 
             cmap=cmap,
             figure_kwarg_dict=figure_kwarg_dict,
             plot_kwarg_dict=dict(label=f'{label}{idx}' if label is not None else None, **plot_kwarg_dict),
             new_fig_=idx==0, show_legend_=idx==X.shape[1]-1 if label is not None else False,
             show_fig_=idx==X.shape[1]-1)
        