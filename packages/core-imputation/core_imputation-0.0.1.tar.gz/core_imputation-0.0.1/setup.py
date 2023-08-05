import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="core_imputation",                
    version="0.0.1",                     
    author="Pablo Mejía",                    
    description="imputation core for indices collected by central banks",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      
    python_requires='>=3.6',               
    py_modules=["core"],             
    package_dir={'':'core/src'},     
    install_requires=[]                     
)