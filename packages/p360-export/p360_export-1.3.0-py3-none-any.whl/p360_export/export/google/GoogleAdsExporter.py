from typing import Dict, Any
from pyspark.sql import DataFrame

from p360_export.export.ExporterInterface import ExporterInterface
from p360_export.export.google.GoogleClientGetter import GoogleClientGetter
from p360_export.export.google.UserDataSender import UserDataSender
from p360_export.export.google.UserListGetter import UserListGetter


class GoogleAdsExporter(ExporterInterface):
    def __init__(
        self,
        google_client_getter: GoogleClientGetter,
        user_data_sender: UserDataSender,
        user_list_getter: UserListGetter,
    ):
        self.__google_client_getter = google_client_getter
        self.__user_data_sender = user_data_sender
        self.__user_list_getter = user_list_getter

    @property
    def export_destination(self):
        return "google_ads"

    def export(self, df: DataFrame, config: Dict[str, Any]):
        client = self.__google_client_getter.get(credentials=config["credentials"])

        user_ids = list(df.select("user_id").toPandas()["user_id"])

        user_list_resource_name = self.__user_list_getter.get(client, config)

        self.__user_data_sender.send(client, user_list_resource_name, user_ids)
