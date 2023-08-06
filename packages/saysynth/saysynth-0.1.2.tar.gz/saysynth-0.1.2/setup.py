from setuptools import find_packages, setup

from saysynth.version import VERSION

config = {
    "name": "saysynth",
    "version": VERSION,
    "packages": find_packages(),
    "package_data": {
        "": ["*.yml"],
    },
    "install_requires": [
        "charset-normalizer",
        "click",
        "mido",
        "midi-utils",
        "pyyaml",
        "g2p_en",
        "nltk",
    ],
    "author": "Brian Abelson",
    "author_email": "hey@gltd.email",
    "description": "A synthesizer built on say",
    "url": "http://globally.ltd",
    "entry_points": {
        "console_scripts": ["saysynth=saysynth.cli:main", "sy=saysynth.cli:main"]
    },
}

setup(**config)
