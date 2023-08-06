import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="sng_tk",
    version="1.0.5",
    author="Maicss",
    author_email="fengchen.liu@sng.com.cn",
    description="SNG development Tools Kit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab.digital-work.cn/sng_cloud",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
