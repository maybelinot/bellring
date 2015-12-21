CONFIGURATION
=============
Example of configuration file in ~/.bellring::

   audio:
       destination: Blue Jeans
       file_path: ~/Downloads/23265__digifishmusic__spanner-chime-soft.wav
       source: Monitor of Built-in Audio Analog Stereo
       volume: 70000
       play_time: 5
   mic:
       source: Built-in Audio Analog Stereo
       volume: 30000


INSTALLATION
============
Example install, using VirtualEnv::

   # install/use python virtual environment
   virtualenv ~/virtenv_scratch --no-site-packages

   # activate the virtual environment
   source ~/virtenv_scratch/bin/activate

   # upgrade pip in the new virtenv
   pip install -U pip setuptools

   # install this package in DEVELOPMENT mode
   # python setup.py develop

   # simply install
   # python setup.py install


USAGE
=====

Run bellring to play sound after 5 minutes::

    bellring --wait 5
