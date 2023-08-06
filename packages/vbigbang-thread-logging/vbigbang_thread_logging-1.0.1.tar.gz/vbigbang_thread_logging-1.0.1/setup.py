from setuptools import setup, find_packages

str_version = '1.0.1'

setup(name='vbigbang_thread_logging',
      version=str_version,
      description='Commonly used function library by MT',
      url='https://github.com/vbigbang',
      author='vbigbang',
      author_email='i@chenxiaosa.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=[],  # 必要依赖
      python_requires='>=3')
