from mpmath import mp,  mpc

def fft(x, inverse=False):
    N = len(x)
    if N <= 1:
        return x
    if N % 2 > 0:
        raise ValueError("Size of x must be a power of 2")
    # Recursive calls for even and odd indices
    X_even = fft(x[0::2], inverse)
    X_odd = fft(x[1::2], inverse)
    # Compute the twiddle factors
    sign = 1 if inverse else -1
    factor = [mp.exp(sign * 2 * mp.pi * mpc(0, 1) * k / N) for k in range(N // 2)]
    # Combine the results
    combined = [X_even[k] + factor[k] * X_odd[k] for k in range(N // 2)] + \
               [X_even[k] - factor[k] * X_odd[k] for k in range(N // 2)]
    return combined

# Implement the inverse FFT function
def ifft(x):
    N = len(x)
    # Compute the inverse FFT
    X = fft(x, inverse=True)
    # Divide by N
    return [Xi / N for Xi in X]

def fft2(matrix):
    # Apply 1D FFT on each row
    fft_rows = [fft(row) for row in matrix]
    # Transpose the result to apply FFT on columns
    fft_rows_transposed = list(map(list, zip(*fft_rows)))
    # Apply 1D FFT on each column
    fft_cols = [fft(col) for col in fft_rows_transposed]
    # Transpose back to get the final result
    fft_result = list(map(list, zip(*fft_cols)))
    return fft_result

def ifft2(matrix):
    # Apply 1D IFFT on each row
    ifft_rows = [ifft(row) for row in matrix]
    # Transpose the result to apply IFFT on columns
    ifft_rows_transposed = list(map(list, zip(*ifft_rows)))
    # Apply 1D IFFT on each column
    ifft_cols = [ifft(col) for col in ifft_rows_transposed]
    # Transpose back to get the final result
    ifft_result = list(map(list, zip(*ifft_cols)))
    return ifft_result