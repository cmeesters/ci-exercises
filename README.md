# CI Exercises

Continuous Integration exercises with C++ and Python components.

## Description

This project contains exercises for learning Continuous Integration (CI) practices with both C++ and Python code. It includes:

- C++ code with Google Test framework for testing
- Python code with pytest for testing
- Poetry for Python dependency management
- CMake for C++ build system

## Dependencies

### Using Conda (Recommended for complete environment)

```bash
conda env create -f environment.yml
conda activate ci-exercises
```

### Using Poetry (Python dependencies only)

```bash
poetry install
```

## Building and Testing

Building and testing is part of the exercise and not described here.

## Project Structure

```
├── CMakeLists.txt          # C++ build configuration
├── pyproject.toml          # Python project configuration
├── environment.yml         # Conda environment specification
├── src/                    # Source code
│   ├── converter.py        # Python module
│   ├── main.cpp            # C++ main file
│   ├── pi_estimator.cpp    # C++ implementation
│   └── pi_estimator.h      # C++ header
└── tests/                  # Test files
    ├── test_converter.py   # Python tests
    └── test_pi_estimator.cpp # C++ tests
```

## Author

cmeesters
