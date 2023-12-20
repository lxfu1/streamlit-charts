import io
import os
import sys
from shutil import rmtree
from setuptools import Command, find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

class UploadCommand(Command):
    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        print("✨✨ {0}".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
            rmtree(os.path.join(here, "build"))
            rmtree(os.path.join(here, "{0}.egg-info".format("streamlit_charts")))
        except OSError:
            pass

        self.status("Building Source and Wheel distribution…")
        os.system("{0} setup.py sdist bdist_wheel".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        sys.exit()

def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()

setup(
    name="streamlit-charts",
    version="0.1.0",
    author="lxuf1",
    author_email="954055752@qq.com",
    description="Render Ant Design Charts in Streamlit",
    long_description=read('readme.md'),
    long_description_content_type="text/plain",
    keywords=["antv", "charts", "Ant Design Charts", "streamlit-component", "streamlit-charts"],
    url="https://github.com/lxfu1/streamlit-charts",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
    cmdclass={"upload": UploadCommand},
)
