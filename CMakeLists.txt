cmake_minimum_required(VERSION 3.10)
project(PiEstimator)

set(CMAKE_CXX_STANDARD 14) # or higher

# Include Google Test
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.17.0.zip
  DOWNLOAD_EXTRACT_TIMESTAMP true
)
FetchContent_MakeAvailable(googletest)

add_executable(pi_estimator src/pi_estimator.cpp src/main.cpp) # Include main.cpp
add_executable(pi_estimator_tests tests/test_pi_estimator.cpp src/pi_estimator.cpp)

target_link_libraries(pi_estimator_tests gtest gtest_main)

# Enable testing
enable_testing()

# Add tests
add_test(NAME pi_estimator_unit_tests COMMAND pi_estimator_tests)

# Set test properties
set_tests_properties(pi_estimator_unit_tests PROPERTIES
    TIMEOUT 30
    WILL_FAIL FALSE
)


# Add custom clean target that removes all build files including CMake cache
add_custom_target(clean-all
    COMMAND ${CMAKE_COMMAND} -E remove_directory ${CMAKE_BINARY_DIR}/CMakeFiles
    COMMAND ${CMAKE_COMMAND} -E remove ${CMAKE_BINARY_DIR}/CMakeCache.txt
    COMMAND ${CMAKE_COMMAND} -E remove ${CMAKE_BINARY_DIR}/cmake_install.cmake
    COMMAND ${CMAKE_COMMAND} -E remove ${CMAKE_BINARY_DIR}/Makefile
    COMMAND ${CMAKE_COMMAND} -E remove ${CMAKE_BINARY_DIR}/pi_estimator
    COMMAND ${CMAKE_COMMAND} -E remove ${CMAKE_BINARY_DIR}/pi_estimator_tests
    COMMAND ${CMAKE_COMMAND} -E remove_directory ${CMAKE_BINARY_DIR}/_deps
    COMMENT "Removing all build files and CMake cache"
)
