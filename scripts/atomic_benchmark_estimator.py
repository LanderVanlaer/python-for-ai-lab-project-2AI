import numpy as np
import time

# https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html#benchmark-and-plot-helper-functions
# def atomic_benchmark_estimator(estimator, X_test, verbose=False):
#     """Measure runtime prediction of each instance."""
#     n_instances = X_test.shape[0]
#     runtimes = np.zeros(n_instances, dtype=float)
#     for i in range(n_instances):
#         instance = X_test[[i], :]
#         start = time.time()
#         estimator.predict(instance)
#         runtimes[i] = time.time() - start
#     if verbose:
#         print(
#             "atomic_benchmark runtimes:",
#             min(runtimes),
#             np.percentile(runtimes, 50),
#             max(runtimes),
#         )
#     return runtimes

def atomic_benchmark_estimator(estimator, X_test, verbose=False, kwargs_estimator_predict=dict()):
    """Measure runtime prediction of each instance."""
    n_instances = X_test.shape[0]
    runtimes = np.zeros(n_instances, dtype=float)
    for i in range(n_instances):
        instance = X_test.iloc[[i], :]
        start = time.time()
        estimator.predict(instance, **kwargs_estimator_predict)
        runtimes[i] = time.time() - start
    if verbose:
        print(
            "atomic_benchmark runtimes:",
            min(runtimes),
            np.percentile(runtimes, 50),
            max(runtimes),
        )
    return runtimes