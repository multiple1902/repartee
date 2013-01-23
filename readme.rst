====================================================
Repartee: a DPI storage back-end and query front-end
====================================================

:Author:    Weisi Dai <multiple1902@gmail.com>
:License:   MIT License

Repartee is a storage back-end and query front-end which should be put behind a deep packet inspection filter and in front of managers that want to analyse flows. Repartee implements a strategy called *ping-pong* which doubles the performance of the storage phase in DPI. 

Repartee is sucessor to the PHP-based ``kopdpi`` project, which is presented in Cheng Zhang's thesis. 

Technical Specs
===============

* Repartee is implemented using Django 1.4, and runs on Python 2.7.
* Repartee uses `PostgreSQL <http://www.postgresql.org/>`_ for storage.
* Repartee uses HTML5 and `Processing.js <http://processingjs.org/>`_ for query UI and data visualization.
* Repartee is released under MIT License. See the ``LICENSE`` file for details.

Related Project
===============

* `KOP-DPI-System <https://github.com/antsgroup/KOP-DPI-System>`_ (ANTS Group, Xi'an Jiaotong University)
    This filters raw traffic (pcap) and produces output regarding meta info of flows, such as OS name, app name, app behavior as well as src / dst IP / ports.

Paper
=====

#. Cheng Zhang. (2012). Design and Implementation of storage and query system of mobile Internet usage behavior (Bachelor's thesis).

