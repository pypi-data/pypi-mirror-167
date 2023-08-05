import itertools

import numpy as np


# TODO: this doesn't actually support arbitrary arrays, only shape (N,)
def correlation(x, y):
    """Compute Pearson correlation coefficient for arrays x and y.

    Note that this is just a wrapper for `np.corrcoef`.
    TODO: this doesn't actually support arbitrary arrays, only shape (N,)

    Parameters
    ----------
    x, y : np.ndarray
        Arrays must have the same shape. Most commonly, these will be a
        model output (prediction) and a recorded response (target).

    Returns
    -------
    float
    
    """
    return np.corrcoef(x, y)[0,1]


def noise_corrected_r(prediction, single_trial_responses, n_pairs=None,
                      trial_axis=0, channel_axis=-1):
    """Compute noise-corrected correlation coefficient for a model prediction.

    Noise is determined by measuring single-trial correlations in the recorded
    response. Based on method in Hsu and Theusnissen (2004), Network.

    Parameters
    ----------
    prediction : np.ndarray.
        Typically the output of `Model.predict`.
    single_trial_responses : np.ndarray.
        Recorded neural response, as a single array with shape
        (Trials, Time, Neurons).
    n_pairs : int or None; optional.
        Number of random single trial pairs to test. If None, test all pairs.
    trial_axis : int; default=0.
        Axis to concatenate for arrays in `single_trial_responses`.
        For example, if `trial_axis=0` and
        `single_trial_responses = [array(shape=(1, 50)), array(shape=(1, 50))]`
        then `all_trials = array(2, 50)`.
    channel_axis : int; default=-1.
        Axis for multiple responses. For example,
        if `single_trial_responses = array(shape=(10, 1000, 50))` representing
        responses of 50 neurons to 10 trials of 1000 time units each, then use
        `channel_axis = 2` to compute this metric for each of the 50 neurons.

    Returns
    -------
    corrected_rs : ndarray.
        One value per channel.
        
    """

    n_channels = single_trial_responses.shape[channel_axis]
    
    corrected_rs = []
    for i in range(n_channels):
        one_channel_pred = np.take(prediction, indices=[i],
                                   axis=channel_axis).squeeze()
        one_channel_resp = np.take(single_trial_responses, indices=[i],
                                   axis=channel_axis)
        trial_pair_r = _paired_single_trial_r(one_channel_resp, n_pairs=n_pairs,
                                              trial_axis=trial_axis)
        trial_pred_r = _single_trial_r(one_channel_pred, one_channel_resp,
                                       trial_axis=trial_axis)
        corrected_r= np.mean(trial_pred_r)/np.sqrt(trial_pair_r)
        corrected_rs.append(corrected_r)
    
    return np.array(corrected_rs)
    
def _paired_single_trial_r(trials, n_pairs=1000, trial_axis=0, limit=0.01):
    """Compute mean correlation of pairs of single trials.

    Internal for `noise_corrected_r`.

    Parameters
    ----------
    trials : ndarray
        Single trial responses concatenated along `trial_axis`.
    n_pairs : int or None; optional.
    trial_axis : int; default=0.
    limit : float
        Minimum value to return, to prevent `noise_corrected_r` from
        blowing up.

    Returns
    -------
    mean_pairwise_correlation : float

    """

    if trials.shape[0] == 1:
        # Only 1 repetition
        raise ValueError("`single_trial_responses` must contain more than 1 "
                         "trial to compute `noise_corrected_r`.")

    n_repetitions = trials.shape[trial_axis]
    # Get all pairs of indices into trial axis,
    # then randomly shuffle the pairs
    pairs = list(itertools.combinations(range(n_repetitions), 2))[:n_pairs]
    np.random.shuffle(pairs)

    # Compute correlation of each pair of responses,
    pairwise_correlations = []
    for i, j in pairs:
        rep1 = np.take(trials, indices=[i], axis=trial_axis).squeeze()
        rep2 = np.take(trials, indices=[j], axis=trial_axis).squeeze()
        pairwise_correlations.append(np.corrcoef(rep1, rep2)[0, 1])
                
    # Hard limit on single-trial correlation to prevent explosion
    # TODO: better logic for this
    mean_pairwise_correlation = np.mean(pairwise_correlations)
    if mean_pairwise_correlation < limit:
        mean_pairwise_correlation = limit

    return mean_pairwise_correlation

def _single_trial_r(prediction, trials, trial_axis=0):
    """Compute mean correlation between prediction and single trial responses.
    
    Internal for `noise_corrected_r`.

    Parameters
    ----------
    prediction : ndarray
    trials : ndarray
        Single trial responses concatenated along `trial_axis`.
    trial_axis : int; default=0.

    Returns
    -------
    mean_trial_correlation : float
    
    """

    n_repetitions = trials.shape[trial_axis]
    trial_correlations = []
    for i in range(n_repetitions):
        single_trial = np.take(trials, indices=[i], axis=trial_axis).squeeze()
        trial_correlations.append(np.corrcoef(prediction, single_trial)[0, 1])

    return np.mean(trial_correlations)
