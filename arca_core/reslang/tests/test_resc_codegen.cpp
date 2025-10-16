#include "../include/resc_ast.h"
#include <iostream>

using namespace reslang;

int main() {
    auto left = std::make_shared<ASTNode>(ASTNode{ASTType::Literal, "True", {}});
    auto right = std::make_shared<ASTNode>(ASTNode{ASTType::Literal, "Unknown", {}});
    ASTNode root{ASTType::BinaryOp, "AND", {left, right}};

    std::cout << "Generated code: " << root.to_string() << "\n";
    return 0;
}
