from setuptools import setup, find_namespace_packages

setup(name='clean-folder_homework',
      version='1.1.1',
      description='test package',
      author='Max',
      author_email='author@example.com',
      license='MIT',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      packages=find_namespace_packages(),
      entry_points={'console_scripts': [
          'clean-folder=clean_folder.main:main']}
      )
