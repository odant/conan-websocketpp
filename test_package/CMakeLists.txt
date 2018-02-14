project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(websocketpp REQUIRED)
find_package(Boost REQUIRED COMPONENTS
    system
)
find_package(Threads REQUIRED)

enable_testing()

add_executable(test_server test_server.cpp)
target_link_libraries(test_server
    websocketpp::websocketpp
    Boost::disable_autolinking
    Boost::system
    Threads::Threads
)
set_target_properties(test_server
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_server
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/bin
    COMMAND test_server
)
