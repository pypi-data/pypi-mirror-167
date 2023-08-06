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

import json
import os
import shutil

from .logger import Logger
from .modifiers.ContentSecurityPolicyModifier import ContentSecurityPolicyModifier
from .modifiers.ExecuteScriptModifier import ExecuteScriptModifier
from .modifiers.HostPermissionsModifier import HostPermissionsModifier
from .modifiers.InsertCssModifier import InsertCssModifier
from .modifiers.JSActionModifier import JSActionModifier
from .modifiers.ManifestActionModifier import ManifestActionModifier
from .modifiers.ManifestVersionModifier import ManifestVersionModifier
from .modifiers.Modifier import Modifier
from .modifiers.ServiceWorkerModifier import ServiceWorkerModifier
from .modifiers.WebAccessibleResourcesModifier import WebAccessibleResourcesModifier
from .wrapper import Wrapper


class Worker:
    wrapper = None

    def work(self, source: str) -> None:
        Logger().log(source)

        # TODO: Can destination be a command line argument instead?
        destination = source + "_delete"
        if os.path.exists(destination):
            Logger().log("Overwriting already existing destination.", 1)
            # TODO: Should deletion be done by default?
            shutil.rmtree(destination)

        shutil.copytree(source, destination)
        manifest_path = destination + "/manifest.json"
        manifest = {}
        if not os.path.exists(manifest_path):
            Logger().log("Missing manifest", 0)
        else:
            if os.path.exists(manifest_path):
                with open(manifest_path) as json_file:
                    manifest = json.load(json_file)
        self.wrapper = Wrapper(destination, manifest)

        modifiers: list[Modifier] = [
            ManifestVersionModifier(self.wrapper),
            ServiceWorkerModifier(self.wrapper),
            ManifestActionModifier(self.wrapper),
            JSActionModifier(self.wrapper),
            ExecuteScriptModifier(self.wrapper),
            InsertCssModifier(self.wrapper),
            WebAccessibleResourcesModifier(self.wrapper),
            ContentSecurityPolicyModifier(self.wrapper),
            HostPermissionsModifier(self.wrapper),
        ]

        for modifier in modifiers:
            modifier.run()
