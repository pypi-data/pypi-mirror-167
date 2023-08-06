from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(name='division_multiplication',
      version='0.3',
      author='Love Kadiya',
      description='Division and Multiplication by three updated',
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['division_multiplication'],
      author_email='love.kadiya@acquaintsoft.com',
      zip_safe=False)
