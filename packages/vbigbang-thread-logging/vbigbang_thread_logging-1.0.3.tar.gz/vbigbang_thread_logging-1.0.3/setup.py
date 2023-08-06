from setuptools import setup, find_packages

str_version = '1.0.3'
readme_file_path = 'README.md'

setup(name='vbigbang_thread_logging',
      version=str_version,
      description='Commonly used function library by MT',
      url='https://github.com/vbigbang',
      author='vbigbang',
      author_email='i@chenxiaosa.com',
      long_description=open(readme_file_path, encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=[],  # 必要依赖
      python_requires='>=3')
