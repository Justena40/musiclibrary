import logging

from src.domain.music import Music

logger = logging.getLogger()


class MusicDao:
    def __init__(self, dynamodb_resource, dynamodb_client, table_name):
        self.dynamodb_resource = dynamodb_resource
        self.dynamodb_client = dynamodb_client
        self.table = self.dynamodb_resource.Table(table_name)

    def create(self, entity: Music) -> None:
        logger.info("[entity] create")
        self.table.put_item(Item=entity.to_dict())

    def delete(self, uuid) -> None:
        logger.info("[entity] delete")

        self.table.delete_item(Key={"uuid": uuid})

        return None

    def find_by_uuid(self, uuid) -> Music:
        logger.info("[entity] entity")
        result = self.table.get_item(Key={"uuid": uuid})

        print(result)

        return result["Item"] if "Item" in result else None
