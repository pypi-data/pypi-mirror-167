import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="ApolloInterface",
    version="0.0.1",
    author="XvXiao",
    author_email="2081981735@qq.com",
    description="实现apollo命名空间下字段的增删改查的接口文件",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hts559734/ApolloInterface",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)