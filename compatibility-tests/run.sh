#!/bin/sh
#Download Python versions: https://www.python.org/ftp/python/

run_tests () {
	python3 -V >> results.txt 2>&1
	python3 tests.py >> results.txt 2>&1
}

python_purge () {
	sudo apt-get remove python* -y
	sudo apt-get remove --auto-remove python* -y
	sudo apt-get purge python* -y
	sudo apt-get purge --auto-remove python* -y
}

install_libraries() {
	python3 -m pip install aiohttp
	python3 -m pip install ecdsa
	python3 -m pip install grpcio
	python3 -m pip install typing
	python3 -m pip install protobuf
	python3 -m pip install injective-py
}

wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz
wget https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tgz
wget https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tgz
wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
wget https://www.python.org/ftp/python/3.7.10/Python-3.7.10.tgz
wget https://www.python.org/ftp/python/3.7.11/Python-3.7.11.tgz
wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz
wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
wget https://www.python.org/ftp/python/3.8.4/Python-3.8.4.tgz
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz
wget https://www.python.org/ftp/python/3.8.6/Python-3.8.6.tgz
wget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz
wget https://www.python.org/ftp/python/3.8.8/Python-3.8.8.tgz
wget https://www.python.org/ftp/python/3.8.9/Python-3.8.9.tgz
wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz
wget https://www.python.org/ftp/python/3.8.11/Python-3.8.11.tgz
wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz
wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
wget https://www.python.org/ftp/python/3.9.3/Python-3.9.3.tgz
wget https://www.python.org/ftp/python/3.9.4/Python-3.9.4.tgz
wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz
wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz


tar -xvf Python-3.7.0.tgz
tar -xvf Python-3.7.1.tgz
tar -xvf Python-3.7.2.tgz
tar -xvf Python-3.7.3.tgz
tar -xvf Python-3.7.4.tgz
tar -xvf Python-3.7.5.tgz
tar -xvf Python-3.7.6.tgz
tar -xvf Python-3.7.7.tgz
tar -xvf Python-3.7.8.tgz
tar -xvf Python-3.7.9.tgz
tar -xvf Python-3.7.10.tgz
tar -xvf Python-3.7.11.tgz
tar -xvf Python-3.8.0.tgz
tar -xvf Python-3.8.1.tgz
tar -xvf Python-3.8.2.tgz
tar -xvf Python-3.8.3.tgz
tar -xvf Python-3.8.4.tgz
tar -xvf Python-3.8.5.tgz
tar -xvf Python-3.8.6.tgz
tar -xvf Python-3.8.7.tgz
tar -xvf Python-3.8.8.tgz
tar -xvf Python-3.8.9.tgz
tar -xvf Python-3.8.10.tgz
tar -xvf Python-3.8.11.tgz
tar -xvf Python-3.9.0.tgz
tar -xvf Python-3.9.1.tgz
tar -xvf Python-3.9.2.tgz
tar -xvf Python-3.9.3.tgz
tar -xvf Python-3.9.4.tgz
tar -xvf Python-3.9.5.tgz
tar -xvf Python-3.9.6.tgz

python_purge

(cd Python-3.7.0 && ./configure)
(cd Python-3.7.0 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.1 && ./configure)
(cd Python-3.7.1 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.2 && ./configure)
(cd Python-3.7.2 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.3 && ./configure)
(cd Python-3.7.3 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.4 && ./configure)
(cd Python-3.7.4 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.5 && ./configure)
(cd Python-3.7.5 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.6 && ./configure)
(cd Python-3.7.6 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.7 && ./configure)
(cd Python-3.7.7 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.8 && ./configure)
(cd Python-3.7.8 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.9 && ./configure)
(cd Python-3.7.9 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.10 && ./configure)
(cd Python-3.7.10 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.7.11 && ./configure)
(cd Python-3.7.11 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.0 && ./configure)
(cd Python-3.8.0 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.1 && ./configure)
(cd Python-3.8.1 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.2 && ./configure)
(cd Python-3.8.2 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.3 && ./configure)
(cd Python-3.8.3 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.4 && ./configure)
(cd Python-3.8.4 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.5 && ./configure)
(cd Python-3.8.5 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.6 && ./configure)
(cd Python-3.8.6 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.7 && ./configure)
(cd Python-3.8.7 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.8 && ./configure)
(cd Python-3.8.8 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.9 && ./configure)
(cd Python-3.8.9 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.10 && ./configure)
(cd Python-3.8.10 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.8.11 && ./configure)
(cd Python-3.8.11 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.9.0 && ./configure)
(cd Python-3.9.0 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.9.1 && ./configure)
(cd Python-3.9.1 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.9.2 && ./configure)
(cd Python-3.9.2 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.9.3 && ./configure)
(cd Python-3.9.3 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.9.4 && ./configure)
(cd Python-3.9.4 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.9.5 && ./configure)
(cd Python-3.9.5 && sudo make install)
install_libraries
run_tests
python_purge

(cd Python-3.9.6 && ./configure)
(cd Python-3.9.6 && sudo make install)
install_libraries
run_tests
python_purge
break
