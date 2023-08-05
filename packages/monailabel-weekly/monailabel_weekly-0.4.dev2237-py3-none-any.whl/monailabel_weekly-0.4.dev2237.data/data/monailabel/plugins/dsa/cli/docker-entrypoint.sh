#!/usr/bin/env bash

# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Calling the slicer_cli_web.cli_list_entrypoint always works, but we can skip
# an extra exec if we find the path directly
POSSIBLE_PATH="$1/$1.py"
if [[ -f "$POSSIBLE_PATH" ]]; then
    python "$POSSIBLE_PATH" "${@:2}"
else
    python -m slicer_cli_web.cli_list_entrypoint "$@"
fi
