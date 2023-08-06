import setuptools
with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extract-img-txt",
    version="1.0.1",
    description="A simple text extractor from image",
    author="Iyanuoluwa Akinwumi",
    author_email="akinwumikaliyanu@gmail.com",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages=["image_extract"],
    license=":: MIT License",
    install_requires=[                                                                                                              
        'pytesseract',                                                                   
        'python-docx',
        'pillow'
        ]
)                  