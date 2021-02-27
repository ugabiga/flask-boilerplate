def doc_build(
    tags: str, name: str, ref: str, has_many=False, success_meta=None, use_security=True
):
    success_data = {name: {"type": "object", "$ref": "#/definitions/{}".format(ref)}}

    if has_many:
        success_data[name]["type"] = "array"

    if success_meta is None:
        success_meta = {}

    doc = {
        "tags": {tags: {}},
        "responses": {
            "200": {
                "description": "Success",
                "schema": {
                    "type": "object",
                    "properties": {
                        "data": {"type": "object", "properties": success_data},
                        "meta": {"type": "object", "properties": success_meta},
                    },
                },
            }
        },
    }

    if use_security:
        doc["security"] = {"Token Bearer": {}}

    return doc
