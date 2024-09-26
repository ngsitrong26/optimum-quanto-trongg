from setuptools import setup, find_packages

setup(
    name="optimum-quanto",
    version="0.2.5",  
    author="David Corvoysier",
    author_email="",
    description="A pytorch quantization backend for optimum.",
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    url="https://github.com/ngsitrong26/optimum-quanto-trongg",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Đảm bảo Python yêu cầu
    install_requires=[
        "torch",
        "numpy",
        "safetensors",
        "ninja"
    ],
)
