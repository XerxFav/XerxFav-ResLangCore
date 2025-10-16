#include "ternary.hpp"
#include <cassert>

using namespace arca::phase;

int main() {
    assert(ternary_not(ternary_state::NEG) == ternary_state::POS);
    assert(ternary_and(ternary_state::NEG, ternary_state::POS) == ternary_state::NEG);
    assert(ternary_or(ternary_state::NEG, ternary_state::ZERO) == ternary_state::ZERO);
    return 0;
}
