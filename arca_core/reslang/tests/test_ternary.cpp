#include <iostream>
#include "ternary.h"

using namespace reslang;

int main() {
    std::cout << "¬True = " << to_string(negate(TernaryValue::True)) << "\n";
    std::cout << "True ∧ Unknown = " << to_string(conjunction(TernaryValue::True, TernaryValue::Unknown)) << "\n";
    std::cout << "False ∨ Unknown = " << to_string(disjunction(TernaryValue::False, TernaryValue::Unknown)) << "\n";
    return 0;
}
