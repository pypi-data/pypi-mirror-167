from marshmallow import (
    Schema,
    fields,
    validate,
)


class ScientificLinkMeetingResourceSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)
    scientific_link_id = fields.Integer(required=True)
    meeting_id = fields.Integer(required=True)
    updated_at = fields.DateTime()
