unicore.content
===============

.. image:: https://travis-ci.org/universalcore/unicore.content.svg?branch=develop
    :target: https://travis-ci.org/universalcore/unicore.content
    :alt: Continuous Integration

.. image:: https://coveralls.io/repos/universalcore/unicore.content/badge.png?branch=develop
    :target: https://coveralls.io/r/universalcore/unicore.content?branch=develop
    :alt: Code Coverage

Generate the models from the Avro_ schema::

    $ virtualenv ve
    $ source ve/bin/activate
    (ve)$ pip install elastic-git
    (ve)$ eg-tools load-schema \
        ./_schemas/unicore.content.models.Page.avsc \
        ./_schemas/unicore.content.models.Category.avsc \
        ./_schemas/unicore.content.models.Localisation.avsc \
        --map-field uuid=elasticgit.models.UUIDField \
        > ./unicore/content/models.py

.. _Avro: http://avro.apache.org/docs/1.7.7/spec.html
