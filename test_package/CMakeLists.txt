project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

enable_testing()

add_executable(test_server test_server.cpp)
target_link_libraries(test_server ${CONAN_LIBS})
target_include_directories(test_server PRIVATE ${CONAN_INCLUDE_DIRS})
add_test(
    NAME test_server
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin
    COMMAND test_server
)
