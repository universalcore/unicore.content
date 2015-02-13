unicore.content
===============

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
