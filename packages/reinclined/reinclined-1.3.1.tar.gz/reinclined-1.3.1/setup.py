from setuptools import setup, find_packages


def readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


requires = [
    'pytest',
    'pytest-xdist',
    'pytest-parallel',
    'altwalker',
    'selenium<4.0.0',
    'Appium-Python-Client',
    'numpy',
    'langdetect',
    'lxml',
    'bs4',
    'pyautogui',
    'pyperclip',
    'pypeln',
    'mitmproxy'
]


setup(
    name="reinclined",
    version="1.3.1",
    author="Denis Kiruku",
    author_email="denniskiruku@gmail.com",
    description="Tools for UI automation using model based testing ... cloned form https://github.com/rakutentech/ui-automation-tools-mbt with few window adaptation.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/kirukudenis/ui-automation-tools-mbt.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requires
)
