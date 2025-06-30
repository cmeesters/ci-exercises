#include "gtest/gtest.h"
#include "../src/pi_estimator.h"

TEST(PiEstimatorTest, EstimatePi) {
    double pi_estimate = estimate_pi(100000);
    ASSERT_NEAR(pi_estimate, 3.14159, 0.01); //Allow for some variation
}
