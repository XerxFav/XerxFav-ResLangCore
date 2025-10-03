#include "ternary.h"

namespace reslang {

TernaryValue negate(TernaryValue v) {
    switch (v) {
        case TernaryValue::True: return TernaryValue::False;
        case TernaryValue::False: return TernaryValue::True;
        default: return TernaryValue::Unknown;
    }
}

TernaryValue conjunction(TernaryValue a, TernaryValue b) {
    if (a == TernaryValue::False || b == TernaryValue::False) return TernaryValue::False;
    if (a == TernaryValue::Unknown || b == TernaryValue::Unknown) return TernaryValue::Unknown;
    return TernaryValue::True;
}

TernaryValue disjunction(TernaryValue a, TernaryValue b) {
    if (a == TernaryValue::True || b == TernaryValue::True) return TernaryValue::True;
    if (a == TernaryValue::Unknown || b == TernaryValue::Unknown) return TernaryValue::Unknown;
    return TernaryValue::False;
}

const char* to_string(TernaryValue v) {
    switch (v) {
        case TernaryValue::True: return "True";
        case TernaryValue::False: return "False";
        default: return "Unknown";
    }
}

}
