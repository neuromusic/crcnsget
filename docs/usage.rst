=====
Usage
=====

crcnsget is a command-line utility to enable downloading datasets from crcnr.org

First, make sure you are have an account at at crcns.org. If you do not, you can request one https://crcns.org/request-account/fg_base_view_p3.

.. code-block:: console

    $ crcnsget --username <username> --dataset <path to dataset>

crcnsget will then prompt for your password.

For example,

.. code-block:: console

    $ crcnsget --username crcnsget --dataset alm-1/datafiles/data_structure_files/data_structure_ANM218457.tar.gz

Will download the from the `data_structure_ANM218457.tar.gz` file from the `alm-1` dataset.