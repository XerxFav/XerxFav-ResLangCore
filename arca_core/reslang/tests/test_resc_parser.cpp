#include <iostream>
#include "compiler/resc_parser.h"

int main() 

  {
    reslang::compiler::TernaryInstruction instr;
    if (reslang::parser::parse_instruction("migrate 3", instr)) {
        std::cout << "Opcode: " << instr.opcode << ", Phase: " << instr.phase << "\n";}
     

    else 
    {
        std::cerr << "Parse failed.\n";
    }

         }