import setuptools


def main() -> None:
    install_requires = ['ruamel.yaml', 'pytest']
    setuptools.setup(
        name="game",
        version="0.0.1",
        packages=setuptools.find_packages(),
        url="",
        author="",
        author_email="",
        license="",
        scripts=["bin/game.py"],
        install_requires=install_requires
    )


if __name__ == "__main__":
    main()
