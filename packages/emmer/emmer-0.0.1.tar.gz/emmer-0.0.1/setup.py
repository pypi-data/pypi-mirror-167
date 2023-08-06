import setuptools
from setuptools import setup
import pathlib
emmer_path = pathlib.Path(__file__).parent.resolve()
long_description = (emmer_path / "README.md").read_text()


setup(name='emmer',
    version='0.0.1',
    author='Alok Bharadwaj, Maarten Joosten, Stefan T Huber, Arjen Jakobi, Reinier de Bruin',
    url='https://gitlab.tudelft.nl/aj-lab/emmer',
    description= "A python toolkit for the cryo-EM developer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='3-clause BSD',
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={'emmer': ['include/geckodriver','include/*.pickle','*.pickle', '*.pdb','*.mrc','*.cif','*.npy']},
    install_requires=['numpy>=1.19.5','scipy>=1.5.4','pandas>=1.1.5','mrcfile>=1.3.0','gemmi>=0.4.8',\
                    'pypdb>=2.0','sklearn>=0.0','pwlf>=2.0.4','tqdm>=4.62.3','more_itertools>=8.10.0',\
                    'scikit-image>=0.17.2','biopython==1.78','matplotlib==3.5.1', 'coverage','pyfiglet>=0.8.post1', 'wget>=3.2'],
    entry_points={
        'console_scripts': [
            'emmer=emmer.main:main',
        ],
    },
    zip_safe= False)

