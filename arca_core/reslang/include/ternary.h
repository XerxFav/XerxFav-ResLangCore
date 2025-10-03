#pragma once

namespace reslang {

enum class TernaryValue { False = -1, Unknown = 0, True = 1 };

TernaryValue negate(TernaryValue v);
TernaryValue conjunction(TernaryValue a, TernaryValue b);
TernaryValue disjunction(TernaryValue a, TernaryValue b);
const char* to_string(TernaryValue v);

}
