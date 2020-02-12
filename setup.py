from distutils.core import setup

setup(
  name = 'bestbuy',         # How you named your package folder (MyLib)
  packages = ['bestbuy'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='GNU GPLv3',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Use BestBuy APIs in Python',   # Give a short description about your library
  long_description_content_type='text/markdown',
  long_description='Full documentation available on GitHub at https://github.com/nwithan8/BestBuy',
  author = 'Nate Harris',                   # Type in your name
  author_email = 'n8gr8gbln@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/nwithan8/BestBuy',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/nwithan8/BestBuy/archive/v1.0.tar.gz',    # I explain this later on
  keywords = ['BestBuy', 'Best Buy', 'shopping', 'API', 'developer', 'products', 'technology', 'electronics'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)