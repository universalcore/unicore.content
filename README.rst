unicore.content
===============

Generate the models from the Avro_ schema::

    $ virtualenv ve
    $ source ve/bin/activate
    (ve)$ pip install elastic-git
    (ve)$ eg-tools load-schema \
        ./unicore/Page.avro.json \
        ./unicore/Category.avro.json \
        ./unicore/Localisation.avro.json \
        --map-field uuid=elasticgit.models.UUIDField \
        --rename-model GitPageModel=Page \
        --rename-model GitCategoryModel=Category \
        > ./unicore/content/models.py
