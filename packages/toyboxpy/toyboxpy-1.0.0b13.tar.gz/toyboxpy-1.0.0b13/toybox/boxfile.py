# SPDX-FileCopyrightText: 2022-present toybox.py Contributors
#
# SPDX-License-Identifier: MIT

import json
import os

from toybox.dependency import Dependency


class Boxfile:
    """Read and parse a toybox config file."""

    def __init__(self, boxfile_folder):
        """Read the Boxfile for the current folder."""

        self.boxfile_path = os.path.join(boxfile_folder, 'Boxfile')
        self.dependencies = []

        self.json_content = {}
        self.json_toyboxes = None
        self.json_config = None
        self.json_installed = None
        self.was_modified = False

        if not os.path.exists(self.boxfile_path):
            # -- If we can't find it we may still create it later.
            return

        try:
            with open(self.boxfile_path, 'r') as file:
                self.json_content = json.load(file)
        except Exception as e:
            raise SyntaxError('Malformed JSON in Boxfile \'' + self.boxfile_path + '\'.\n' + str(e) + '.')

        self.was_modified = Boxfile.maybeConvertOldBoxfile(self.json_content)

        for key in self.json_content.keys():
            value = self.json_content[key]
            value_type = type(value).__name__

            if value_type == 'dict':
                if key == 'toyboxes':
                    self.json_toyboxes = value
                    continue
                elif key == 'config':
                    self.json_config = value
                    continue
                elif key == 'installed':
                    self.json_installed = value
                    continue

            raise SyntaxError('Incorrect format for Boxfile \'' + self.boxfile_path + '\'.\nMaybe you need to upgrade toybox?')

        if self.json_toyboxes is not None:
            for key in self.json_toyboxes.keys():
                self.addDependencyWithURL(key, self.json_toyboxes[key])

    def addDependencyWithURL(self, url, versions_as_string=None):
        dependency = Dependency(url)
        dependency_already_existed = False

        for dep in self.dependencies:
            if dep.url == dependency.url:
                dependency = dep
                dependency_already_existed = True
                break

        if versions_as_string is None:
            versions_as_string = dependency.git.getHeadBranch()

        dependency.replaceVersions(versions_as_string)

        if dependency_already_existed is False:
            self.dependencies.append(dependency)

        if self.json_toyboxes is None:
            self.json_toyboxes = self.json_content['toyboxes'] = {}

        self.json_toyboxes[url] = dependency.originalVersionsAsString()

        self.was_modified = True

    def removeDependencyWithURLIn(self, url, toyboxes_folder):
        dep = Dependency(url)
        url = dep.url

        url_to_remove = None
        for other_url in self.json_toyboxes.keys():
            other_dep = Dependency(other_url)
            if other_dep.url == url:
                url_to_remove = other_url
                break

        if url_to_remove is None:
            raise SyntaxError('Couldn\'t find any dependency for URL \'' + url + '\'.')

        self.json_toyboxes.pop(url_to_remove, None)

        dep.deleteFolderIn(toyboxes_folder)

        for other_dep in self.dependencies:
            if other_dep.url == url:
                self.dependencies.remove(other_dep)

        self.json_installed.pop(url, None)

        self.was_modified = True

    def setLuaImport(self, lua_import_file):
        if self.json_config is None:
            self.json_config = self.json_content['config'] = {}

        self.json_config['lua_import'] = lua_import_file

        self.was_modified = True

    def maybeInstalledVersionAsStringForDependency(self, dep):
        if self.json_installed:
            url = dep.url

            if url in self.json_installed:
                return self.json_installed[url]

        return None

    def setInstalledVersionStringForDependency(self, dep, version_as_string):
        if self.json_installed is None:
            self.json_installed = self.json_content['installed'] = {}

        self.json_installed[dep.url] = version_as_string

        self.was_modified = True

    def maybeLuaImportFile(self):
        if self.json_config and 'lua_import' in self.json_config:
            return self.json_config['lua_import']

        return None

    def saveIfModified(self):
        if self.was_modified:
            out_file = open(self.boxfile_path, 'w')
            json.dump(self.json_content, out_file, indent=4)

            out_file.close()

    @classmethod
    def maybeConvertOldBoxfile(cls, json_content):
        old_keys = {}

        for key in json_content.keys():
            value = json_content[key]

            if type(value).__name__ == 'str':
                old_keys[key] = value

        if len(old_keys) == 0:
            return False

        if 'toyboxes' not in json_content:
            toyboxes = json_content['toyboxes'] = {}
        else:
            toyboxes = json_content['toyboxes']

        for old_key in old_keys.keys():
            toyboxes[old_key] = old_keys[key]
            json_content.pop(old_key, None)

        return True
