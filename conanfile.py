from conans import ConanFile


class WebsocketppConan(ConanFile):
    name = "websocketpp"
    version = "0.7.0"
    license = "BSD - https://github.com/zaphoyd/websocketpp/blob/master/COPYING"
    description = "WebSocket++ is a header only C++ library that implements RFC6455 The WebSocket Protocol."
    url = "https://github.com/odant/conan-websocketpp"
    exports_sources = "src/*"
    no_copy_source = True

    def package(self):
        self.copy("*.hpp", src="src/websocketpp", dst="include/webscoketpp")

    def package_id(self):
        self.info.header_only()
