# Copyright 2021 Google Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from . import Logger, Modifier


class ManifestVersionModifier(Modifier):
    def _mv2(self) -> None:
        self.__common()

    def _mv3(self) -> None:
        self.__common()

    def __common(self) -> None:
        Logger().log(
            "Changing manifest_version to {}".format(self.wrapper.getManifestVersion())
        )
        self.wrapper.manifest["manifest_version"] = self.wrapper.getManifestVersion()
        self.writeManifest()
