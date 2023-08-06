from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="sentSlack",  # Required
    version="1.0.1",  # Required
    description="A sample Python project",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/pypa/sampleproject",  # Optional
    author="Alejandro Matallana",  # Optional
    author_email="alejandro.matallana@escala24x7.com",  # Optional
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="sample, setuptools, development",  # Optional
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <4",
    install_requires=["peppercorn"],  # Optional
    data_files=[("my_data", ["data/data_file"])],  # Optional
    entry_points={  # Optional
        "console_scripts": [
            "sample=sample:main",
        ],
    },
)


# import json
# from os import path
# from setuptools import setup, find_packages
# from sys import version_info

# VERSION = "1.0.0"
# CURR_PATH = "{}{}".format(path.abspath(path.dirname(__file__)), "/")


# def path_format(file_path=None, file_name=None, is_abspath=False, ignore_raises=False):
#     """
#     Get path joined checking before if path and filepath exist,
#      if not, raise an Exception
#      if ignore_raise it's enabled, then file_path must include '/' at end lane
#     """
#     path_formatted = "{}{}".format(file_path, file_name)
#     if ignore_raises:
#         return path_formatted
#     if file_path is None or not path.exists(file_path):
#         raise IOError("Path '{}' doesn't exists".format(file_path))
#     if file_name is None or not path.exists(path_formatted):
#         raise IOError("File '{}{}' doesn't exists".format(file_path, file_name))
#     if is_abspath:
#         return path.abspath(path.join(file_path, file_name))
#     else:
#         return path.join(file_path, file_name)


# def read_file(
#     is_json=False,
#     file_path=None,
#     encoding="utf-8",
#     is_encoding=True,
#     ignore_raises=False,
# ):
#     """Returns file object from file_path,
#        compatible with all py versions
#     optionals:
#       can be use to return dict from json path
#       can modify encoding used to obtain file
#     """
#     text = None
#     try:
#         if file_path is None:
#             raise Exception("File path received it's None")
#         if version_info.major >= 3:
#             if not is_encoding:
#                 encoding = None
#             with open(file_path, encoding=encoding) as buff:
#                 text = buff.read()
#         if version_info.major <= 2:
#             with open(file_path) as buff:
#                 if is_encoding:
#                     text = buff.read().decode(encoding)
#                 else:
#                     text = buff.read()
#         if is_json:
#             return json.loads(text)
#     except Exception as err:
#         if not ignore_raises:
#             raise Exception(err)
#     return text


# def read(file_name=None, is_encoding=True, ignore_raises=False):
#     """Read file"""
#     if file_name is None:
#         raise Exception("File name not provided")
#     if ignore_raises:
#         try:
#             return read_file(
#                 is_encoding=is_encoding,
#                 file_path=path_format(
#                     file_path=CURR_PATH,
#                     file_name=file_name,
#                     ignore_raises=ignore_raises,
#                 ),
#             )
#         except Exception:
#             return "NOTFOUND"
#     return read_file(
#         is_encoding=is_encoding,
#         file_path=path_format(
#             file_path=CURR_PATH, file_name=file_name, ignore_raises=ignore_raises
#         ),
#     )


# setup(
#     name="send_msg_slack",
#     version=VERSION,
#     packages=find_packages(),
#     description="function generic for sent message to Slack",
#     license=read("LICENSE", is_encoding=False, ignore_raises=True),
#     author="Alejandro Matallana",
#     author_email="alejandro.matallana@escala24x7.com",
#     long_description=read("README.rst"),
#     url="https://github.com/pypa/sampleproject",
#     keywords=["slack", "send", "message", "msg"],
#     entry_points={
#         "console_scripts": ["send_msg_slack=send_msg_slack.send_msg_slack:main"],
#     },
#     classifiers=[
#         "Development Status :: 4 - Beta",
#         "Intended Audience :: Developers",
#         "Topic :: Software Development :: Build Tools",
#         "Programming Language :: Python :: 2.7",
#         "Programming Language :: Python :: 3.4",
#         "Programming Language :: Python :: 3.5",
#         "Programming Language :: Python :: 3.6",
#         "Programming Language :: Python :: 3.7",
#     ],
# )
