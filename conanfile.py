from conans import ConanFile, tools


class WebsocketppConan(ConanFile):
    name = "websocketpp"
    version = "0.8.1+6"
    license = "BSD - https://github.com/zaphoyd/websocketpp/blob/master/COPYING"
    description = "WebSocket++ is a header only C++ library that implements RFC6455 The WebSocket Protocol."
    url = "https://github.com/odant/conan-websocketpp"
    exports_sources = "src/*", "Findwebsocketpp.cmake", "odant.patch"
    no_copy_source = True

    def requirements(self):
        self.requires("boost/[>=1.70.0]@%s/testing" % self.user)

    def source(self):
        tools.patch(patch_file="odant.patch")

    def package(self):
        self.copy("Findwebsocketpp.cmake", src=".", dst=".")
        self.copy("*.hpp", src="src/websocketpp", dst="include/websocketpp", keep_path=True)

    def package_id(self):
        self.info.header_only()
