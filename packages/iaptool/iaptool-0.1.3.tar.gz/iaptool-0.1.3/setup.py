#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/7 15:24
# @Author  : jeremy
# @File    : setup.py




from distutils.core import setup
from setuptools import find_packages

setup(name='iaptool',  # 包名
      version='0.1.3',  # 版本号
      description='sinomcu chip hex download tool',
      long_description='sinomcu chip hex download tool For Embedded development.',
      author='文涛',
      author_email='33672008@qq.com',
      url='https://gitee.com/stduino',
      license='GPL3.0',#'pyqtwebengine>=5.15',
      install_requires=['pyside6==6.3.0','pyserial==3.5','diskcache==5.4.0','crcmod==1.7'],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities'
      ],
      keywords='chip hex download tool',
      packages=find_packages('core'),  # 必填，就是包的代码主目录
      package_dir={'': 'core'},  # 必填
      include_package_data=True,
      )
