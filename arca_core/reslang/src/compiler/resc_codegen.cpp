#include "compiler/resc.h"
#include <boost/multiprecision/cpp_int.hpp>

namespace reslang::compiler {

using boost::multiprecision::uint128_t;

CodeGenerator::CodeGenerator() {}

std::vector<uint8_t> CodeGenerator::generate(const TernaryInstruction& instr) {
    std::vector<uint8_t> bytecode;

    // Простейшая фазовая кодировка
    if (instr.opcode == "migrate") {
        bytecode.push_back(0xA3); // троичный код миграции
        bytecode.push_back(static_cast<uint8_t>(instr.phase));
    } else if (instr.opcode == "activate") {
        bytecode.push_back(0xB7); // активация фазы
        bytecode.push_back(static_cast<uint8_t>(instr.phase));
    } else {
        bytecode.push_back(0x00); // неизвестная инструкция
    }

    return bytecode;
}

} // namespace reslang::compiler
