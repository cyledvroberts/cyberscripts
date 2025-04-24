Objectives:

    Often a cybersecurity engineer needs to geo-locate IP addresses from log files. In this lab, you will write a program to parse a log file which includes records related to failed login attempts and geo locate each unique IP address.
    The company MAXMIND sells a database which can be used to geo locate IP addresses by country, city, postal code, and approximate latitude/longitude. Since IP addresses are not by definition tied to geo-location MAXMIND sells a subscription to these databases and keeps them up to date.
    Use the Python geo location library ‘pygeoip’ to look up the country associated with failed login attempts from IP addresses in a log file.
        The GeoIP.dat files was downloaded from here: https://dev.maxmind.com/geoip/legacy/geolite 

    Links to an external site. (use ‘gunzip GeoIP.dat.gz’ to decompress)
    Use the Canvas file in case there have been changes.

    Documentation available at http://pygeoip.readthedocs.io/en/v0.3.2 

Links to an external site.
You may need to install the library using the Linux command ‘pip install pygeoip’ (run in a terminal with root privilege).
For this lab, use the GeoIP.dat file from course files geolocation directory or download here: GeoIP.dat

        Download GeoIP.dat.

Script Requirements

Write a Python script to parse the logins.txt

Download logins.txt file.  Your script should answer the following questions.

    How many unique IP addresses are in the file?
        I used a Python dictionary to store the count of each unique IP address.  Each IP address was a key and the stored value was the number of times I had seen that IP address.
        Python Dictionary: http://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python
    How many times is each unique IP address present?
    What is the country of origin of each unique IP address?
    How many unique IP addresses are associated with each country?
        I used a Python dictionary again (see above).

Output 

1. Print your output to the console.

2. You do not need to sort the IP addresses. 
How to run your program

Use the following command to run your program.

% python3 geolocate.py

The program should assume the GeoIP.dat and logins.txt are in the same directory has geolocate.py.
