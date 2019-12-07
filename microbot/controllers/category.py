from microbot.restplus import api

category_create_model = api.schema_model("Categories", {
    "properties": {
        "name": {
            "type": "string",
            "description": "Nome da categoria"
        }
    },
    "type": "object",
    "additionalProperties": False,
    "required": ["name"]
})
