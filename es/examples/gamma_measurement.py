"""Educational gamma estimator: one layer/head, equal-length unpadded samples.

Input contains real, post-softmax attention probabilities BEFORE dropout.
This module does not load or execute a language model.
"""
import numpy as np


def measure_gamma(attention, *, queries, sink_tokens, d_min, d_max):
    """Mean over pairs at each distance, then unweighted OLS over distances.

    attention: [independent_samples, query_position, key_position].
    queries: explicit positions, e.g. [n - 1] for last-query protocol.
    No padding, head/layer pooling, or renormalization after sink exclusion.
    """
    a = np.asarray(attention, dtype=np.float64)
    if a.ndim != 3 or a.shape[0] < 1 or a.shape[1] != a.shape[2]:
        raise ValueError("Expected [samples, n, n], with at least one sample")
    n = a.shape[-1]
    if not np.isfinite(a).all() or (a < 0).any():
        raise ValueError("Attention must be finite and non-negative")
    q = np.asarray(queries)
    if (q.ndim != 1 or q.size == 0 or not np.issubdtype(q.dtype, np.integer)
            or len(np.unique(q)) != len(q) or (q < 0).any() or (q >= n).any()):
        raise ValueError("queries must be distinct integer positions in [0, n)")
    if not (isinstance(sink_tokens, int) and 0 <= sink_tokens < n):
        raise ValueError("sink_tokens must be an integer in [0, n)")
    if not (isinstance(d_min, int) and isinstance(d_max, int)
            and 1 <= d_min <= d_max < n):
        raise ValueError("Require 1 <= d_min <= d_max < n")
    selected = a[:, q, :]
    if not np.allclose(selected.sum(axis=-1), 1.0, rtol=0, atol=2e-3):
        raise ValueError("Selected rows must be post-softmax probabilities, without dropout")
    # This example is for dense causal attention; a different mask needs a new protocol.
    for i in q:
        if (a[:, i, i + 1:] > 1e-7).any():
            raise ValueError("Future-token mass: expected a causal attention matrix")
    distances, means, counts = [], [], []
    for d in range(d_min, d_max + 1):
        valid_q = q[q - d >= sink_tokens]
        if valid_q.size:
            values = a[:, valid_q, valid_q - d]
            distances.append(d)
            means.append(values.mean())  # arithmetic mean BEFORE the logarithm
            counts.append(values.size)
    d, mean = np.asarray(distances), np.asarray(means)
    if d.size < 4 or (mean <= 0).any():
        raise ValueError("Need >=4 represented distances with positive mean; do not add epsilon")
    x, y = np.log(d), np.log(mean)
    slope, intercept = np.polyfit(x, y, 1)
    residual = y - (intercept + slope * x)
    total = np.sum((y - y.mean()) ** 2)
    r2 = float(1 - np.sum(residual ** 2) / total) if total > 1e-24 else None
    return {
        "gamma": float(-slope), "r2_log": r2,
        "distance": d.tolist(), "mean_attention": mean.tolist(),
        "pair_count": counts, "residual_log": residual.tolist(),
        "sink_mass": float(selected[:, :, :sink_tokens].sum(axis=-1).mean()),
        "protocol": {"id": "guide-distance-mean-v1", "queries": q.tolist(),
                     "sink_tokens": sink_tokens, "d_min": d_min, "d_max": d_max,
                     "samples": int(a.shape[0]), "length": int(n),
                     "pooling": "arithmetic_mean_per_distance",
                     "fit": "unweighted_OLS_log_mean_vs_log_distance"},
    }
