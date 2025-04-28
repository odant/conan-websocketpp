from conan import ConanFile, tools
import os

class WebsocketppConan(ConanFile):
    name = "websocketpp"
    version = "0.8.1+10"
    license = "BSD - https://github.com/zaphoyd/websocketpp/blob/master/COPYING"
    description = "WebSocket++ is a header only C++ library that implements RFC6455 The WebSocket Protocol."
    url = "https://github.com/odant/conan-websocketpp"
    exports_sources = "src/*", "Findwebsocketpp.cmake", "odant.patch", "fix_std_c++20_build.patch"
    no_copy_source = True
    package_type = "header-library"

    def requirements(self):
        self.requires("boost/[>=1.70.0]@%s/testing" % self.user)

    def source(self):
        tools.files.patch(self, patch_file="odant.patch")
        tools.files.patch(self, patch_file="fix_std_c++20_build.patch")

    def package(self):
        tools.files.copy(self, "Findwebsocketpp.cmake", src=self.export_sources_folder, dst=self.package_folder)
        tools.files.copy(self, "*.hpp", src=os.path.join(self.source_folder, "src", "websocketpp"), dst=os.path.join(self.package_folder, "include", "websocketpp"), keep_path=True)

    def package_id(self):
        self.info.clear()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "both")
        self.cpp_info.set_property("cmake_file_name", "websocketpp")
        self.cpp_info.set_property("cmake_target_name", "websocketpp::websocketpp")
        self.cpp_info.requires = ["boost::headers"]
