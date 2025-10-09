"""Build and test scripts for the CI exercises project."""

import subprocess
import os
import sys
from pathlib import Path


def build_cpp():
    """Build the C++ project using CMake."""
    build_dir = Path("build")
    build_dir.mkdir(exist_ok=True)

    # Configure
    result = subprocess.run(
        ["cmake", "-S", ".", "-B", "build"], capture_output=True, text=True
    )

    if result.returncode != 0:
        print("CMake configuration failed:")
        print(result.stderr)
        sys.exit(1)

    # Build
    result = subprocess.run(
        ["cmake", "--build", "build"], capture_output=True, text=True
    )

    if result.returncode != 0:
        print("CMake build failed:")
        print(result.stderr)
        sys.exit(1)

    print("C++ build completed successfully!")


def test_cpp():
    """Build and run C++ tests."""
    build_cpp()

    # Run C++ tests
    test_executable = Path("build/pi_estimator_tests")
    if not test_executable.exists():
        print("C++ test executable not found. Build may have failed.")
        sys.exit(1)

    result = subprocess.run(
        [str(test_executable)], capture_output=True, text=True
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        print("C++ tests failed!")
        sys.exit(1)

    print("C++ tests passed!")


def test_all():
    """Run both Python and C++ tests."""
    print("Running Python tests...")
    result = subprocess.run(
        ["pytest", "tests/", "-v", "--cov=src", "--cov-report=term-missing"],
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    if result.stderr:
        print(result.stderr)

    python_success = result.returncode == 0

    print("\nRunning C++ tests...")
    try:
        test_cpp()
        cpp_success = True
    except SystemExit:
        cpp_success = False

    if python_success and cpp_success:
        print("\n✅ All tests passed!")
    else:
        failed = []
        if not python_success:
            failed.append("Python")
        if not cpp_success:
            failed.append("C++")
        print(f"\n❌ {', '.join(failed)} tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "build":
            build_cpp()
        elif sys.argv[1] == "test-cpp":
            test_cpp()
        elif sys.argv[1] == "test-all":
            test_all()
