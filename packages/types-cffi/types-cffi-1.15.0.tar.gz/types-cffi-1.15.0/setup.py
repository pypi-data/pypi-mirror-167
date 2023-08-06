from setuptools import setup

name = "types-cffi"
description = "Typing stubs for cffi"
long_description = '''
## Typing stubs for cffi

This is a PEP 561 type stub package for the `cffi` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `cffi`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/cffi. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `205901e2fd607e212bd1c036939860a56efc8061`.
'''.lstrip()

setup(name=name,
      version="1.15.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/cffi.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['_cffi_backend-stubs', 'cffi-stubs'],
      package_data={'_cffi_backend-stubs': ['__init__.pyi', 'METADATA.toml'], 'cffi-stubs': ['__init__.pyi', 'api.pyi', 'backend_ctypes.pyi', 'cffi_opcode.pyi', 'commontypes.pyi', 'cparser.pyi', 'error.pyi', 'ffiplatform.pyi', 'lock.pyi', 'model.pyi', 'pkgconfig.pyi', 'recompiler.pyi', 'setuptools_ext.pyi', 'vengine_cpy.pyi', 'vengine_gen.pyi', 'verifier.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
