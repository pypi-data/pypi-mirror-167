import setuptools

setuptools.setup(
    name="cxo_relay",
    version="1.0.5",
    author="Beastly418",
    description="Python based CLI for running a Cargo X Relayer.",
    url="https://github.com/Beastly418/CargoXPythonRelayerCLI",
    install_requires=['web3', 'requests'],
    packages=setuptools.find_packages(where='src'),
    package_dir={"": "src"},
    keywords=['Cargo X', 'Relayer','web3', 'CXO'],
    entry_points={
        'console_scripts': [
            'cxo_relay = pkg.CXORelayer:main'
        ]
    },
    python_requires='>=3.6',
)
