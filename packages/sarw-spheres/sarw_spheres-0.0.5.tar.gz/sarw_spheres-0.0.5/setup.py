from distutils.core import setup, Extension

sarw_spheres = Extension(
    "sarw_spheres",
    sources=["sarw_spheres.cpp"],
)

with open('README.md') as f:
    long_description = f.read()

setup(
    name="sarw_spheres",
    version="0.0.5",
    
    url='https://github.com/RadostW/sarw_spheres',
    author='Radost Waszkiewicz',
    author_email='radost.waszkiewicz@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    project_urls = {
      'Documentation': 'https://github.com/RadostW/sarw_spheres',
      'Source': 'https://github.com/RadostW/sarw_spheres'
    },
    license='MIT',
    
    description="Genrate self avoiding random walks (SARW) for spheres of given sizes.",
    ext_modules=[sarw_spheres],
    install_requires=['numpy>1.16'],
)
