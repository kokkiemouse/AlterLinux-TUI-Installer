from setuptools import setup,find_packages
setup(
    name="archlinux_tui_installer",
    version="0.0.0.1",
    description="setup archlinux with tui",
    author="FascodeNetwork",
    install_requires=["pythondialog"],
    packages=find_packages(),
    entry_points={
        "console_scripts":[
            "archlinux_tui_installer=archlinux_tui_installer.archlinux_tui_installer:main"
        ]
    }
)