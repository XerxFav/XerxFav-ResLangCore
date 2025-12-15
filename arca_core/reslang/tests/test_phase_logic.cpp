#include "../include/ternary.h"
#include <iostream>

using namespace reslang;

void test_phase_transition(TernaryValue v) {
    std::cout << "Phase transition of " << to_string(v) << " → "
              << to_string(ternary_not(v)) << "\n";
}

int main() {
    test_phase_transition(TernaryValue::True);
    test_phase_transition(TernaryValue::Unknown);
    test_phase_transition(TernaryValue::False);
    return 0;
}
