from setuptools import find_packages, setup

setup(
    name = 'HangmanLibrary',         # How you named your package folder (MyLib)
    packages = find_packages(['HangmanLibrary']),   # Chose the same as "name"
    version = '0.3.0',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    author = 'CitrusBoy',                   # Type in your name
    download_url = 'https://github.com/GuiOliv/HangmanLibrary/archive/refs/tags/0.3.0.tar.gz',    # I explain this later on
)
