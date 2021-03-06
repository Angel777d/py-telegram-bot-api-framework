import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="py-telegram-bot-api-framework",
    version="0.0.2",
    description="Telegram bot framework over py-telegram-bot-api",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Angel777d/py-telegram-bot-api-framework",
    author="Angelovich",
    author_email="angel777da@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["py_telegram_bot_api_framework", ],
    include_package_data=True,
    install_requires=["py_telegram_bot_api", ],
)
