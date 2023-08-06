# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, Extension
import pybind11

setup(
    packages = ["jax_triton"],
    ext_modules = [
      Extension(
        name="jax_triton.triton_kernel_call",
        sources=["lib/triton_kernel_call.cc"],
        include_dirs = [
          "/usr/local/cuda/include",
          pybind11.get_include()], 
        libraries = ["cuda"],
        library_dirs = ["/usr/local/cuda/lib64", "/usr/local/cuda/lib64/stubs"],
        )])
