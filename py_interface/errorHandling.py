class MatrixInputInconsistencyError(Exception):
    """Raised when matrix rows have inconsistent column lengths."""
    pass

class LowMatrixCountError(Exception):
    """Cannot have number of matrices to be less than 2"""
    pass