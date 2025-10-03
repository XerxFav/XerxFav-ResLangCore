#pragma once

#include <string>
#include <vector>
#include <cstdint>  // ✅ Добавлено для uint8_t

namespace reslang::compiler {

struct TernaryInstruction {
    std::string opcode;
    int phase;
};

class CodeGenerator {
public:
    CodeGenerator();
    std::vector<uint8_t> generate(const TernaryInstruction& instr);
};

} // namespace reslang::compiler
