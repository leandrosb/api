from microbot.restplus import api

category_create_model = api.schema_model("Categories", {
    "properties": {
        "id": {
            "type": "integer",
            "description": "id da categoria"
        },
        "name": {
            "type": "string",
            "description": "name para o portal"
        },
        "status": {
            "type": "string",
            "enum": ["active", "inactive"],
            "description": "Status da categoria: active ou inactive"
        }
    },
    "type": "object",
    "additionalProperties": False,
    "required": ["id", "name", "status"]
})
