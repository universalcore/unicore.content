# NOTE:
#
#   This is an automatically generated Elasticgit Model definition
#   from an Avro schema. Do not manually edit this file unless you
#   absolutely know what you are doing.
#
# namespace: unicore.content.models
#
# VERSION INFO:
#
#   package:          elastic-git
#   package_version:  1.0.0
#   language_version: 2.7.6
#

from elasticgit import models


class Page(models.Model):

    subtitle = models.TextField("""subtitle""")
    description = models.TextField("""description""")
    language = models.TextField("""language""")
    title = models.TextField("""title""")
    created_at = models.TextField("""created_at""")
    published = models.BooleanField("""published""")
    modified_at = models.TextField("""modified_at""")
    linked_pages = models.ListField("""linked_pages""", fields=(
        models.TextField('string'),
    ))
    slug = models.TextField("""slug""")
    content = models.TextField("""content""")
    source = models.TextField("""source""")
    featured = models.BooleanField("""featured""")
    featured_in_category = models.BooleanField("""featured_in_category""")
    id = models.TextField("""id""")
    position = models.IntegerField("""position""")
    primary_category = models.TextField("""primary_category""")
    image = models.TextField("""image""")
    image_host = models.TextField("""image_host""")
    uuid = models.UUIDField(
        """uuid""", fallbacks=[models.SingleFieldFallback('id'), ])
    author_tags = models.ListField(
        """author_tags""", default=[], fields=(
            models.TextField('string'),
        ))


class Category(models.Model):

    subtitle = models.TextField("""subtitle""")
    language = models.TextField("""language""")
    title = models.TextField("""title""")
    id = models.TextField("""id""")
    source = models.TextField("""source""")
    position = models.IntegerField("""position""")
    featured_in_navbar = models.BooleanField("""featured_in_navbar""")
    slug = models.TextField("""slug""")
    image = models.TextField("""image""")
    image_host = models.TextField("""image_host""")
    uuid = models.UUIDField(
        """uuid""", fallbacks=[models.SingleFieldFallback('id'), ])


class Localisation(models.Model):

    locale = models.TextField("""locale""")
    image = models.TextField("""image""")
    image_host = models.TextField("""image_host""")
    logo_image = models.TextField("""logo_image""")
    logo_image_host = models.TextField("""logo_image_host""")
    logo_text = models.TextField("""logo_text""")
    logo_description = models.TextField("""logo_description""")
