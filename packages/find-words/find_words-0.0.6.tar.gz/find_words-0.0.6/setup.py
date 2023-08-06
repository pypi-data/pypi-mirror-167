import setuptools

setuptools.setup(
    name="find_words", # Replace with your own username
    version="0.0.6",
    author="김병주",
    author_email="atker14@gmail.com",
    description="텍스트 파일에서 키워드 찾는 함수",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)