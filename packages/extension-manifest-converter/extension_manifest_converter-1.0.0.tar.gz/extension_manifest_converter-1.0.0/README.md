# Extension Manifest Converter

[![PyPI](
  https://img.shields.io/pypi/v/extension-manifest-converter?color=blue
  )](
  https://pypi.org/project/extension-manifest-converter
) [![pre-commit.ci status](
  https://results.pre-commit.ci/badge/github/eggplants/extension-manifest-converter/main.svg
  )](
  https://results.pre-commit.ci/latest/github/eggplants/extension-manifest-converter/main
)

[![Maintainability](
  https://api.codeclimate.com/v1/badges/09b8d7fd82410ad92238/maintainability
  )](
  https://codeclimate.com/github/eggplants/extension-manifest-converter/maintainability
) [![Test Coverage](
  https://api.codeclimate.com/v1/badges/09b8d7fd82410ad92238/test_coverage
  )](
  https://codeclimate.com/github/eggplants/extension-manifest-converter/test_coverage
)

[![ghcr latest](
  https://ghcr-badge.herokuapp.com/eggplants/extension-manifest-converter/latest_tag?trim=major&label=latest
) ![ghcr size](
  https://ghcr-badge.herokuapp.com/eggplants/extension-manifest-converter/size)
](
  https://github.com/eggplants/extension-manifest-converter/pkgs/container/extension-manifest-converter
)

---

Original(~2021): [GoogleChromeLabs/extension-manifest-converter](https://github.com/GoogleChromeLabs/extension-manifest-converter)

---

Extension Manifest Converter is an open source tool that helps convert existing Chrome extensions to
Manifest V3. Use it to convert an entire directory, extension zip file, or just a manifest.json
file. All expected changes are applied to manifest.json.

## Features

* Performs conversions on
  * unpacked extension directories
  * zip files containing an extension
  * manifest.json
* General manifest.json conversions
  * Updates `manifest_version` field
  * Converts between host permissions declared in `permissions` or `optional_permissions` in MV2 and
    `host_permissions` in MV3
  * Converts between a `content_security_policy` string in MV2 and `content_security_policy` object
    with`extension_pages` and `sandbox` properties in MV3
  * Converts between `background.scripts` in MV2 and background service workers
    `background.service_worker` in MV3
* Scripting API conversions
  * Converts `chrome.tabs.executeScript` in MV2 to `chrome.scripting.executeScript` in MV3. If
    necessary, also adds `scripting` to the `permissions` array in manifest.json.
  * Converts `chrome.tabs.insertCSS` in Mv2 to `chrome.scripting.insertCSS` in MV3. If necessary,
    also adds `scripting` to the `permissions` array in manifest.json.
* Action API conversions
  * Converts calls to `chrome.browserAction` and `chrome.pageAction` in MV2 into `chrome.action` in
    MV3
  * Converts `browser_action` and `page_action` manifest entries in MV2 into `action` in MV3

## Limitations

This tool aims to simplify the MV3 conversion; it does not fully automate the process. Only search
and replace changes are applied to `.js` files.

This tool does not:

* update any service worker code that relies on a DOM

## Installation

To use this tool, you'll need to set it up by following the steps below.

1. Make sure Python 3 is installed.

    ```bash
    python3 --version
    ```

    If you don't see a version number, follow your OS's guidance to install Python 3 or visit
    <https://www.python.org/downloads/> to download a recent release.

2. Install `emc` command.

    ```bash
    pip install git+https://github.com/eggplants/extension-manifest-converter
    # or
    pip install extension-manifest-converter
    ```

3. Execute the test command.

    ```bash
    emc
    ```

    The tool should log basic usage information to the console.

## Usage

* Convert a directory

    ```bash
    emc dir/path/
    ```

* Convert a manifest file

    ```bash
    emc manifest.json
    ```

* Convert a .zip file

    ```bash
    emc extension.zip
    ```

## License

[Apache 2.0](https://github.com/GoogleChromeLabs/extension-manifest-converter/blob/master/LICENSE)

This is not an official Google product.
