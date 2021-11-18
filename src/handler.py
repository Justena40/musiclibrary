from src.core.resources_mgr import ResourcesMgr
from src.domain.music import Music
from src.domain.music_dao import MusicDao

import logging
import json

logger = logging.getLogger()
print("create dynamodb resources")
resources_mgr = ResourcesMgr()

def create_music(event, context):
    print(event)

    body = json.loads(event["body"])
    music = Music(author=body["author"],
                   title=body["title"],
                   genre=body["genre"],
                   date=body["date"])
    dao = MusicDao(
        dynamodb_resource=resources_mgr.dynamodb_resource,
        dynamodb_client=resources_mgr.dynamodb_client,
        table_name=resources_mgr.table_name())

    dao.create(music)
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": music.to_json(),
    }

def find_music(event, context):
    print(event)

    dao = MusicDao(
        dynamodb_resource=resources_mgr.dynamodb_resource,
        dynamodb_client=resources_mgr.dynamodb_client,
        table_name=resources_mgr.table_name(),
    )

    entities = dao.find_by_uuid(event["pathParameters"]["uuid"])

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(entities, default=lambda entity: entity.to_json()),
    }

