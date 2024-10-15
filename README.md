# ArbFFT
ArbFFT: Arbitrary Precision Fast Fourier Transform in Python


[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

ArbFFT is a Python package that provides arbitrary precision Fast Fourier Transform (FFT) and inverse FFT (IFFT) computations. Leveraging the `mpmath` library for multiple-precision floating-point arithmetic, ArbFFT allows you to perform FFTs with precision far beyond standard double-precision floats. This is particularly useful in applications requiring high numerical accuracy.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Getting Started](#getting-started)
  - [Setting Precision](#setting-precision)
  - [FFT and IFFT](#fft-and-ifft)
  - [2D FFT and IFFT](#2d-fft-and-ifft)
- [Usage Examples](#usage-examples)
  - [1D FFT Example](#1d-fft-example)
  - [2D FFT Example](#2d-fft-example)
- [API Reference](#api-reference)
  - [`fft`](#fft)
  - [`ifft`](#ifft)
  - [`fft2`](#fft2)
  - [`ifft2`](#ifft2)
- [Performance Considerations](#performance-considerations)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Arbitrary Precision:** Perform FFT and IFFT computations with user-defined precision.
- **1D and 2D Transforms:** Support for both one-dimensional and two-dimensional FFTs and IFFTs.
- **Complex Number Support:** Handles complex-valued inputs for comprehensive spectral analysis.
- **Easy Integration:** Designed to work seamlessly with NumPy arrays and the `mpmath` library.
- **Open Source:** Licensed under the MIT License, encouraging community contributions.

## Installation

ArbFFT requires Python 3.6 or higher and depends on the `mpmath` library for arbitrary precision arithmetic.

1. **Clone ArbFFT:**

   Clone the repository or download the source code:

   ```bash
   git clone https://github.com/jakharkaran/arbfft.git
   ```

2. **Install ArbFFT:**

   Navigate to the directory and install the package:

   ```bash
   pip install -e ./
   ```

## Getting Started

### Setting Precision

Before performing computations, set the desired precision using `mpmath`:

```python
from mpmath import mp
mp.dps = 50  # Set precision to 50 decimal places
```

### FFT, IFFT for 2D and FFT2, IFFT2 for 2D transforms

Import the ArbFFT functions:

```python
from arbfft import fft, ifft, fft2, ifft2
```


## Usage Examples

### 1D FFT Example

```python
from mpmath import mp, mpc
from arbfft import fft, ifft

# Set precision
mp.dps = 30  # 30 decimal places

# Create sample data
data = [mpc(mp.sin(i), mp.cos(i)) for i in range(8)]

# Perform FFT
fft_result = fft(data)

# Perform IFFT
ifft_result = ifft(fft_result)

# Display results
print("FFT Result:")
for value in fft_result:
    print(value)

print("\nRecovered Data after IFFT:")
for value in ifft_result:
    print(value)
```

### 2D FFT Example

```python
from mpmath import mp, mpc
from arbfft import fft2, ifft2

# Set precision
mp.dps = 30  # 30 decimal places

# Create 2D sample data (e.g., 4x4 matrix)
data = [[mpc(mp.sin(i + j), mp.cos(i + j)) for j in range(4)] for i in range(4)]

# Perform 2D FFT
fft2_result = fft2(data)

# Perform 2D IFFT
ifft2_result = ifft2(fft2_result)

# Display results
print("2D FFT Result:")
for row in fft2_result:
    print(row)

print("\nRecovered Data after 2D IFFT:")
for row in ifft2_result:
    print(row)
```

## API Reference

### `fft`

```python
fft(x, inverse=False)
```

Performs the one-dimensional FFT on a list of `mpmath` complex numbers.

- **Parameters:**
  - `x`: List of `mpmath.mpc` complex numbers. The length of the list must be a power of two.
  - `inverse` (optional): Boolean flag to perform the inverse FFT. Default is `False`.

- **Returns:**
  - List of `mpmath.mpc` complex numbers representing the FFT of the input.

### `ifft`

```python
ifft(x)
```

Performs the one-dimensional inverse FFT on a list of `mpmath` complex numbers.

- **Parameters:**
  - `x`: List of `mpmath.mpc` complex numbers. The length of the list must be a power of two.

- **Returns:**
  - List of `mpmath.mpc` complex numbers representing the inverse FFT of the input.

### `fft2`

```python
fft2(matrix)
```

Performs the two-dimensional FFT on a matrix (list of lists) of `mpmath` complex numbers.

- **Parameters:**
  - `matrix`: 2D list (list of lists) of `mpmath.mpc` complex numbers. Both dimensions must be powers of two.

- **Returns:**
  - 2D list of `mpmath.mpc` complex numbers representing the 2D FFT of the input.

### `ifft2`

```python
ifft2(matrix)
```

Performs the two-dimensional inverse FFT on a matrix (list of lists) of `mpmath` complex numbers.

- **Parameters:**
  - `matrix`: 2D list (list of lists) of `mpmath.mpc` complex numbers. Both dimensions must be powers of two.

- **Returns:**
  - 2D list of `mpmath.mpc` complex numbers representing the 2D inverse FFT of the input.

## Performance Considerations

- **Speed vs. Precision:** Higher precision (`mp.dps`) will result in longer computation times.
- **Recursive Implementation:** The current implementation uses recursive algorithms (Cooley–Tukey FFT algorithm), which may hit recursion limits for large data sizes.
- **Optimization:** For larger datasets, consider implementing iterative versions or optimizing the code further.

## Contributing

Contributions are welcome! If you have ideas for improvements or have found bugs, please open an issue or submit a pull request.

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -am 'Add your feature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

