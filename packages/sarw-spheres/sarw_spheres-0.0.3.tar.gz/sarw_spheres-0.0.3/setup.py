from distutils.core import setup, Extension

sarw_spheres = Extension(
    "sarw_spheres",
    sources=["sarw_spheres.cpp"],
)

setup(
    name="sarw_spheres",
    version="0.0.3",
    description="Genrate self avoiding random walks (SARW) for spheres of given sizes.",
    ext_modules=[sarw_spheres],
    install_requires=['numpy>1.16'],
)
