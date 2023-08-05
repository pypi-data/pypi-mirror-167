# # import setuptools

# from Alexandria import Alexandria

# method_list = [method for method in dir(Alexandria.Book) if method.startswith('__') is False]

# for i in method_list:
#     print(f'Method: {getattr(Alexandria.Book, i).__name__}()')
#     print(f'Doc: {getattr(Alexandria.Book, i).__doc__}')
#     print()

import setuptools

with open("README.md", "r", errors="ignore") as fh:
    description = fh.read()
  
setuptools.setup(
    name="EthAlexandria",
    version="0.0.5",
    author="Obiajulu_M",
    author_email="oambanefo@outlook.com",
    packages=setuptools.find_packages(),
    description="A project to decentralize and distribute literary infrastructure powered by EVM and IPFS.",
    long_description=description,
    include_package_data=True,
    long_description_content_type="text/markdown",
    url="https://github.com/ObiajuluM/Alexandria",
    license='MIT',
    python_requires='>=3.8',
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["web3", "ipfshttpclient"])
