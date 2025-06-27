#include <iostream>
#include <string>
#include <cstdlib> // For atoi
#include "pi_estimator.h"

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <number_of_points>" << std::endl;
        return 1;
    }

    int num_points = std::atoi(argv[1]);
    if (num_points <= 0) {
        std::cerr << "Error: Number of points must be a positive integer." << std::endl;
        return 1;
    }

    double pi_estimate = estimate_pi(num_points);
    std::cout << "Estimated value of PI: " << pi_estimate << std::endl;

    return 0;
}
