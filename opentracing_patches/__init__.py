# Copyright (C) 2018-2019 SignalFx, Inc. All rights reserved.
import traceback
import opentracing

from . import tags


@staticmethod
def _patched_on_error(span, exc_type, exc_val, exc_tb):
    if not span or not exc_val:
        return

    span.set_tag(tags.ERROR, True)
    span.set_tag(tags.ERROR_MESSAGE, str(exc_val))
    span.set_tag(tags.ERROR_OBJECT, exc_val)
    span.set_tag(tags.ERROR_KIND, exc_type)
    span.set_tag(tags.ERROR_STACK, traceback.format_tb(exc_tb))


opentracing.Span._on_error = _patched_on_error
