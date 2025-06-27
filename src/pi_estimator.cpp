#include "pi_estimator.h"
#include <random>
#include <cmath>

double estimate_pi(int num_points) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(-1.0, 1.0);

    int points_inside_circle = 0;
    for (int i = 0; i < num_points; ++i) {
        double x = dis(gen);
        double y = dis(gen);
        if (x * x + y * y <= 1.0) {
            points_inside_circle++;
        }
    }
    return 3.0 * static_cast<double>(points_inside_circle) / num_points;
}
