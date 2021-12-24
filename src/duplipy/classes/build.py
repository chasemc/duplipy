import pkg_resources
import json

#  safe_version   safe_name   resource_string  resource_listdir resource_filename

# TODO: replace OS python code with builtin?: get_build_platform  get_distribution  get_platform

# https://kiwidamien.github.io/making-a-python-package-vi-including-data-files.html


class Electron:
    def __init__(self, *args, **kwargs):
        self.package_json = None


class PackageJson:
    def __init__(self, *args, **kwargs):
        self.final_package_json = None
        # Load the template json file
        stream = pkg_resources.resource_stream("duplipy", "data/template/package.json")
        self.package_json_template = json.load(stream)
        self.build_options = {
            "appId": "com.<<app_name>>",
            "files": ["app/**/*", "node_modules/**/*", "package.json"],
            "directories": {"buildResources": "resources"},
            "publish": null,
            "asar": false,
        }
        self.scripts = {
            "postinstall": "electron-builder install-app-deps",
            "preunit": "webpack --config=build/webpack.unit.config.js --env=test --display=none",
            "unit": "electron-mocha temp/specs.js --renderer --require source-map-support/register",
            "pree2e": "webpack --config=build/webpack.app.config.js --env=test --display=none && webpack --config=build/webpack.e2e.config.js --env=test --display=none",
            "e2e": "mocha temp/e2e.js --require source-map-support/register",
            "test": "npm run unit && npm run e2e",
            "start": "node build/start.js",
            "release": "npm test && webpack --config=build/webpack.app.config.js --env=production && electron-builder",
        }

    def create_package_json(
        self,
        app_name: str = "MyApp",
        description: str = "description",
        semantic_version: str = "0.0.0",
        app_root_path: str = None,
        repository: str = "",
        author: str = "",
        copyright_year: str = "",
        copyright_name: str = "",
        website: str = "",
        license: str = "",
        deps: str = None,
    ):
        1 + 1

    def app_name(self, app_name: str = "MyApp"):
        self.package_json_template["name"] = app_name

    def product_name(self, product_name: str = "MyApp"):
        self.package_json_template["productName"] = product_name

    def description(self, description: str = "description"):
        self.package_json_template["description"] = description

    def version(self, version: str = "version"):
        self.package_json_template["version"] = version

    def private(self, private: str = True):
        self.package_json_template["private"] = private

    def author(self, author: str = "author"):
        self.package_json_template["author"] = author

    def copyright(self, copyright: str = "copyright"):
        self.package_json_template["copyright"] = copyright

    def license(self, license: str = "license"):
        self.package_json_template["license"] = license

    def homepage(self, license: str = "homepage"):
        self.package_json_template["homepage"] = license

    def main(self, main: str = "main"):
        self.package_json_template["main"] = main

    def build(self):
        self.package_json_template["build"] = self.build_options

    def scripts(self):
        self.package_json_template["scripts"] = self.scripts
