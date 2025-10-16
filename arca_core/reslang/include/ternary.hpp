#pragma once

#include <boost/multiprecision/cpp_dec_float.hpp>
#include <algorithm>

namespace arca::phase {

enum class ternary_state : int {
    NEG = -1,
    ZERO = 0,
    POS = 1
};

inline ternary_state ternary_not(ternary_state s) {
    return static_cast<ternary_state>(-static_cast<int>(s));
}

inline ternary_state ternary_and(ternary_state a, ternary_state b) {
    return static_cast<ternary_state>(std::min(static_cast<int>(a), static_cast<int>(b)));
}

inline ternary_state ternary_or(ternary_state a, ternary_state b) {
    return static_cast<ternary_state>(std::max(static_cast<int>(a), static_cast<int>(b)));
}

using phase_float = boost::multiprecision::cpp_dec_float_50;

} // namespace arca::phase

