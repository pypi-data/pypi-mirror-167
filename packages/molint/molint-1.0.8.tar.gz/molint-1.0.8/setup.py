from setuptools import setup, find_packages

with open(r"molint\README.md", "r", encoding="utf-8") as f:
    readme = f.read()
setup(
    name="molint",
    version="1.0.8",
    description="扫描py文件",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="mzg",
    packages=find_packages(),
    package_data={'': ['.pylintrc', 'README.md']},
    install_requires=['pylint==2.9.5'],
    entry_points={
        'console_scripts': [  # key值为console_scripts
            'molint = molint.scan:main'  # 格式为'命令名 = 模块名:函数名'
        ]
    },
)
