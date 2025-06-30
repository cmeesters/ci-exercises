cmake_minimum_required(VERSION 3.10)
project(PiEstimator)

set(CMAKE_CXX_STANDARD 14) # or higher

# Include Google Test
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.17.0.zip
)
FetchContent_MakeAvailable(googletest)

add_executable(pi_estimator src/pi_estimator.cpp src/main.cpp) # Include main.cpp
add_executable(pi_estimator_tests tests/test_pi_estimator.cpp src/pi_estimator.cpp)

target_link_libraries(pi_estimator_tests gtest gtest_main)
