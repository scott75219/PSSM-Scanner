
PSSM Scanner
Author: Scott Goldweber
Version 0.1.0
7/24/2015
-------------
Purpose: To scan for the occurance of a motif within a set of background set and display the strength of confidence of that motif

Dependencies:
--------------
PHP: https://secure.php.net/
Python 2.7: https://www.python.org/
Bio Python 1.6: http://biopython.org/wiki/Main_Page
Numpy 1.9: http://sourceforge.net/projects/numpy/files/NumPy/
Modern internet broweser
Aoache Webserver

**NOTE: Numpy and Python need a C compiler in order to install on unix machines from binaries (yum install gcc)

--------------
|Installation|
--------------
Install Python 
-----------------------
Download python binaries
tar -zxvf Python-2.7.5.tar.gz
cd Python-2.7
./configure
make
make install
Windows: Download and install .exe file

Install Numpy
----------------------
download numpy-1.7.1.tar.gz
tar -zxvf numpy-1.7.1.tar.gz
cd numpy-1.7.1/
python setup.py build
Windows: Download and install .exe file

Install biopython
--------------------
Download biopython-X.X.tar.gz
tar -zxvf biopython-X.X.tar.gz
cd biopython
python setup.py install
If Python has been downloaded in a standard directory: easy_install -f http://biopython.org/DIST/ biopython
Wndows: download and install .exe file

PHP
______
yum install php
make sure that apache or webserver of choice has write permissions to the uploads directory
e.g: chgrp apache /var/www/html/uploads
check /etc/php.ini to ensure Allow uploads is on and the file size is sufficient fop use
	e.g:Upload_max_filesize  - 1500 M
	Max_input_time  - 1000
	Memory_limit    - 640M
	Max_execution_time -  1800
	Post_max_size - 2000 M

-------
|Input|
-------
PSSM file: Space seperated matrix conveying the likliehood of each nucleotide at every position. If there is no nulceotide position, then the weight will be 0.
Query file: Fasta file with motif to be queried. the query sequence must be same size or smaller then the background lengths, each seqeuence identifier wil begin with ">".
background file: Fasta file all of the same length and must be the same length as the PSSM matrix. Each seqeuence identifier wil begin with ">".
	
--------
|Output|
--------
Sequence logo representation of the PSSM
Graph representing -log p values of scores distributions based on the background sequences
List of Confidence scores
List of max scores for each sequence
 