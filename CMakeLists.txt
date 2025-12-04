cmake_minimum_required(VERSION 3.15)
project(conanqmlbug CXX)



add_executable(conanqmlbug src/conanqmlbug.cpp src/main.cpp)



install(TARGETS conanqmlbug DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
