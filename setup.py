from distutils.core import setup
setup(
  name = 'cardpack',       
  packages = ['cardpack'],  
  version = '1.0',      
  license='MIT',       
  description = 'Create command line card games at the drop of a hat',   
  author = 'Pieter Meijer',                   
  author_email = 'info@petoeten.com',       
  url = 'https://github.com/mejongetje/cardpack',  
  download_url = 'https://github.com/mejongetje/cardpack/archive/v_01.tar.gz',    
  keywords = ['Card Game', 'Card Deck', ''],    
  install_requires=[           
          'random',
      ],
  classifiers=[
    'Development Status :: 35 - Production/Stable',     
    'Intended Audience :: Beginner Programmers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',    
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ],
)