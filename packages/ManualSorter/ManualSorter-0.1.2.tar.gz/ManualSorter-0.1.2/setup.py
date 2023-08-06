from setuptools import setup

setup(
    name="ManualSorter",
    version='0.1.2',
    description='Basic TUI tool to reorder a list on the clipboard',
    url='https://github.com/TeddyWoodburn/ManualSorter',
    author='Teddy Woodburn',
    author_email='113065068+TeddyWoodburn@users.noreply.github.com',
    license='unlicense',
    packages=['mansort'],
    install_requires=['pyperclip', 'windows-curses; sys_platform == "Windows"'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Programming Language :: Python',
    ]

)