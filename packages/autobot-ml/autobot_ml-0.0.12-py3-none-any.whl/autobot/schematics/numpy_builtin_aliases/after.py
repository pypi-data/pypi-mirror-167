"""...without NumPy's deprecated aliases (so int instead of np.int)."""


def f() -> None:
    a = np.array(dtype=int)
    b = np.dtype(str)
    c = np.dtype(object)
    d = float(123)
