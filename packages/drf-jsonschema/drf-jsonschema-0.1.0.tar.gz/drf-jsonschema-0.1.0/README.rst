=============================
drf jsonschema
=============================
drf-jsonschema, created by Kiratech from extending `jsonschema <https://github.com/python-jsonschema/jsonschema>`_ package.
This package provides JsonSchemaField and constructs JsonSchema validation error into error tree for Django Rest Framework with custom error message. 

This package will install `jsonschema <https://github.com/python-jsonschema/jsonschema>`_ automatically so manual installation is not necessary.

Quick Start
-----------

1. You can use JsonSchemaFieldValidator in Django's ``models.py`` as such::

    from drf_jsonschema import JsonSchemaFieldValidator
    ...
    ...
    json_data = models.JSONField(validators=[JsonSchemaFieldValidator(schema=your_json_schema)])

2. On ``serializers.py``, modify the serializer field mapping from ``JSONField`` to ``JSONSchemaField`` as the example below::

    class YourSerializer(serializers.ModelSerializer):
        serializer = serializers.ModelSerializer
        serializer_field_mapping = serializer.serializer_field_mapping.copy()
        serializer_field_mapping[models.JSONField] = JSONSchemaField
        ...

3. For more information, visit `jsonschema <https://github.com/python-jsonschema/jsonschema>`_ 
