import setuptools

with open( "README.md", "r", encoding="utf-8" ) as fh:
    long_description = fh.read( )

setuptools.setup(
    name                         = "demure_captcha",
    versio                       = "0.8.1",
    author                       = "Trishkin Sergey",
    author_email                 = "grdvsng@gmail.com",
    description                  = "Simple but customize captcha generator( image + voice )",
    long_description             = long_description,
    long_description_content_type= "text/markdown",
    url                          = "https://github.com/pypa/sampleproject",
    project_urls                 = {
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={ "": "src" },
    packages=setuptools.find_packages( where="src" ),
    python_requires=">=3.8",
)