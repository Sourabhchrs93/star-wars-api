#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful_swagger import swagger


@swagger.model
class LocalSave:
    """Login fields."""

    resource_fields = {
        'name': 'fields.String',
        'url': 'fields.String'
    }
