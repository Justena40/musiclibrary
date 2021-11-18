import logging

from src.domain.song import Song
from boto3.dynamodb.conditions import Key

logger = logging.getLogger()


class SongDao:
    def __init__(self, dynamodb_resource, dynamodb_client, table_name):
        self.dynamodb_resource = dynamodb_resource
        self.dynamodb_client = dynamodb_client
        self.table = self.dynamodb_resource.Table(table_name)

    def create(self, entity: Song) -> None:
        logger.info("[entity] create")
        self.table.put_item(Item=entity.to_dict())

    def delete(self, uuid) -> None:
        logger.info("[entity] delete")

        self.table.delete_item(Key={"uuid": uuid})

        return None

    def find_by_uuid(self, uuid) -> Song:
        logger.info("[entity] entity")
        result = self.table.query(IndexName="gsi-uuid", KeyConditionExpression=Key('uuid').eq(1))
        print(result)

        return result["Items"] if "Items" in result else None

    def find_by_author_and_title(self, author, title):
        logger.info("[entity] entity")
        result = self.table.get_item(Key={"author": author, "title": title})
        print(result)

        return result

    def find_author_and_date(self, author, date):
        logger.info("[entity] entity")
        result = self.table.query(IndexName="author-date", KeyConditionExpression=Key('author').eq(author) &
                                  Key('date').eq(date))
        print(result)

        return result
