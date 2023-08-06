#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="pixqrcodegen",
    version="0.2",
    author="Alex Pinheiro",
    url="https://github.com/Alexsussa/pixqrcodegen",
    packages=['pixqrcodegen'],
    description="Gera a Payload do PIX e o QR Code",
    python_requires=">= 3.6",
    install_requires=['crcmod', 'qrcode', 'pillow'],
    license='MIT',
    keywords=['qrcode', 'payload', 'qrcode-generator', 'pix', 'pix-payload-generator'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent'
        ]
)
