# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:56:21 2022

@author: wujian
"""

import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

from distutils.core import setup
setup(
  name = 'risk_model_maidou',         # How you named your package folder (MyLib)
  # packages = ['risk_model_maidou'],   # Chose the same as "name"
  version = '0.0.11',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = '自动评分卡建模工具-Automatic scorecard modeling tool',   # Give a short description about your library
  author = 'maidoudoujiushiwo',                   # Type in your name
  author_email = 'fengyuguohou2010@hotmail.com',      # Type in your E-Mail
  url = 'https://github.com/maidoudoujiushiwo/risk_model',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/maidoudoujiushiwo/risk_model.git',    # I explain this later on
  keywords = ['Automatic', 'scorecard', 'woe'],   # Keywords that define your package best
  # install_requires=[            # I get to this in a second
  #         '0.0.2',       # 可以加上版本号，如validators=1.5.1   
  #         'risk_model_maidou',
      # ],

  packages=setuptools.find_packages(),
    
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',   
    'Programming Language :: Python :: 3.5', 
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ],
)


