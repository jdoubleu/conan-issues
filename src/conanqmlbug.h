#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define CONANQMLBUG_EXPORT __declspec(dllexport)
#else
  #define CONANQMLBUG_EXPORT
#endif

CONANQMLBUG_EXPORT void conanqmlbug();
CONANQMLBUG_EXPORT void conanqmlbug_print_vector(const std::vector<std::string> &strings);
