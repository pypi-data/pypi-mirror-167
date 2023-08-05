import setuptools

setuptools.setup(
    name="extract-img-txt",
    version="1.0.0",
    description="A simple text extractor from image",
    author="Iyanuoluwa Akinwumi",
    author_email="akinwumikaliyanu@gmail.com",
    packages=["image_extract"],
    license="LICENSE.txt",
    install_requires=[                                                                                                              
        'pytesseract',
        'python-docx',
        'pillow'
        ]
)