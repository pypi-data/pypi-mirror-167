from distutils.core import setup
setup(
    name = 'fintonic_ocr_handler',
    packages = ['fintonic_ocr_handler'],
    version = '0.6',
    license ='MIT',
    description = 'Librería para procesar errores del ocr',
    author = 'fintonic',
    author_email = 'raulperez@fintonic.com',
    url = 'https://www.fintonic.mx/',
    # download_url = '',
    keywords = ['fintonic', 'error', 'handler', 'extraction', 'ocr'],   # Keywords that define your package best
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)