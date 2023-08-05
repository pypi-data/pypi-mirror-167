'''
Author: SXQ-STUDY xiaoqiang.s@outlook.com
Date: 2022-06-19 10:22:12
LastEditors: SXQ-STUDY xiaoqiang.s@outlook.com
LastEditTime: 2022-09-12 15:48:48
FilePath: \helptrain\setup.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helptrain",
    version="0.0.6",
    author="SXQ",
    author_email="xiaoqiang.s@outlook.com",
    description="help to train your network based on pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)