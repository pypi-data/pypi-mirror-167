import traceback

from fastapi.responses import Response
from hautils.logger import logger
import json
from mongoengine import Document, QuerySet
from pydantic import BaseModel

def mongo_to_dict(content):
    if not issubclass(type(content), Document) and not issubclass(type(content), dict) and not issubclass(type(content), BaseModel):
        logger.warn("unsupported object type %s " % (type(content)))
        raise Exception
    if issubclass(type(content), Document):
        response_object = json.loads(content.to_json())
        response_object["id"] = str(content.id)
        response_object.pop("_id")
    elif issubclass(type(content), BaseModel):
        response_object = content.dict()
    else:
        logger.debug("format type %s" % (type(content)))
        response_object = content

    return response_object


def json_response(content, status=200, pop_fields=list()):
    try:
        if issubclass(type(content), QuerySet) or issubclass(type(content), list):
            response = []
            for doc in content:
                response.append(doc_cleanup(doc, pop_fields))
        else:
            response = doc_cleanup(content, pop_fields)
        logger.debug("json dumping type %s" % (type(response)))
        response = json.dumps(response)
        logger.info("json encode %s" % (response,))
        return Response(content=response, status_code=status, media_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.debug(traceback.format_exception(type(e), e, e.__traceback__))

    return Response(content=content, status_code=403, media_type="application/json")


def doc_cleanup(doc, pop_fields):
    response = mongo_to_dict(doc)
    for field in pop_fields:
        try:
            response.pop(field)
        except Exception as e:
            logger.error("field %s not in dictionary" % (field,))
    return response


def mongo_to_log(content):
    try:
        return json.dumps(mongo_to_dict(content))
    except Exception as e:
        return ""


def exception_log(e):
    logger.error(e)
    logger.debug(traceback.format_exception(type(e), e, e.__traceback__))
