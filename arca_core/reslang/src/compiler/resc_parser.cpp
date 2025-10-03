#include <boost/spirit/home/x3.hpp>
#include <boost/fusion/include/adapt_struct.hpp>
#include "compiler/resc_parser.h"
#include <string>
#include <iostream>

namespace x3 = boost::spirit::x3;

namespace reslang::parser {

bool parse_instruction(const std::string& input, reslang::compiler::TernaryInstruction& result) {
    if (input.starts_with("migrate")) {
        result.opcode = "migrate";
        result.phase = 3;
        return true;
    }
    return false;
}

}


namespace reslang::parser {

struct TernaryInstruction {
    std::string opcode;
    int phase;
};

x3::rule<class instruction, TernaryInstruction> const instruction = "instruction";

auto const instruction_def =
    x3::lexeme[+x3::alpha] >> x3::int_;

BOOST_SPIRIT_DEFINE(instruction)

bool parse_instruction(const std::string& input, TernaryInstruction& result) {
    auto iter = input.begin();
    auto end = input.end();
    return phrase_parse(iter, end, instruction, x3::space, result);
}

} // namespace reslang::parser

BOOST_FUSION_ADAPT_STRUCT(reslang::parser::TernaryInstruction,
    opcode,
    phase
)
