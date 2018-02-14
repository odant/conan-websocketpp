#include <websocketpp/server.hpp>
#include <websocketpp/config/asio_no_tls.hpp>
#include <cstdlib>

int main(int, char**) {
    websocketpp::server<websocketpp::config::asio> server;
    return EXIT_SUCCESS;
}
