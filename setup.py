from setuptools import setup

setup(name                =  'gameoflife'                                  ,
      version             =  '0.1.0'                                       ,
      description         =  "Conway's Game of Life Simulation."           ,
      url                 =  'http://github.com/artemis-beta/gameoflife'   ,
      author              =  'Kristian Zarebski'                           ,
      author_email        =  'krizar312@yahoo.co.uk'                       ,
      license             =  'MIT'                                         ,
      packages            =  ['gameoflife']                                ,
      zip_safe            =  False                                         ,
      install_requires    =  ['termcolor', 'numpy']
     )
