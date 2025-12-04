#include "conanqmlbug.h"
#include <vector>
#include <string>

int main() {
    conanqmlbug();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    conanqmlbug_print_vector(vec);
}
