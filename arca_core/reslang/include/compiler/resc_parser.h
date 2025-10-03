#pragma once
#include <string>
#include "compiler/resc.h"
#include "resc.h"  // ✅ Это даст доступ к TernaryInstruction

namespace reslang::parser {
    bool parse_instruction(const std::string& input, reslang::compiler::TernaryInstruction& result);
}
