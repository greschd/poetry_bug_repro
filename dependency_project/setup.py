import os
import setuptools
import subprocess

res = subprocess.check_output(["pre-commit", "--version"],text=True, env=os.environ).strip()
if res != "pre-commit 2.3.0":
    raise RuntimeError(f"Wrong pre-commit '{res}'.")

if __name__ == "__main__":
    setuptools.setup(
        name="dependency_project",
        version="0.1.0",
        author="Dominik Gresch",
        author_email='dominik.gresch@ansys.com',
        long_description_content_type='text/markdown',
        license="MIT",
        python_requires=">=3.9",
        install_requires=["pre-commit==2.3.0"],
        package_dir = {"": "src"},
        packages=setuptools.find_packages("src"),
    )
