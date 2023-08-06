import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
        name = "extend_py",
        version = "1.0.4",
        author = "bailiyiyun",
        author_email = "995440065@qq.com",
        description = "This is a extc",	#介绍
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "https://gitee.com/bailiyiyun/extc-package",#如果自己写的，在GitHub有就写GitHub地址，或者其他地址，没有就写pypi自己的url地址
        packages = setuptools.find_packages(),
        classifiers=[
        "Programming Language :: Python :: 3",
            ],#这个文件适用的python版本，安全等等，我这里只写入了版本
        )