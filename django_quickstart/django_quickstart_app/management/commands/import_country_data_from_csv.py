import logging
import os

import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand
from django_quickstart_app.models import Country
from pandas import DataFrame


class Command(BaseCommand):
    help = ""
    log = logging.getLogger(__name__)

    def add_arguments(self, parser):
        parser.add_argument(
            "--read_path",
            dest="read_path",
            type=str,
            help="Read path",
            default="",
            required=False,
        )

    # @command_decorator(log, "import_hotels")
    def handle(self, *args, **options):
        self.main(options)

    def main(self, options):
        filename_path = options["read_path"]
        df_country = self.read_data_from_csv(filename_path)
        return df_country

    @staticmethod
    def read_data_from_csv(filename_path: str) -> DataFrame:
        base_dir = settings.BASE_DIR

        print(base_dir)
        # This is overriding the filename_path parameter of this function.
        filename_path = os.path.join(base_dir, "/django_quickstart_app/data/country_data.csv")
        filename_path = "/app/django_quickstart/django_quickstart_app/data/country_data.csv"
        df_country = pd.read_csv(filename_path, sep=",")
        return df_country

    def update_countrys_to_database(df_country: DataFrame):
        for row in df_country.to_dict("records"):
            defaults = {
                "numeric_code": row["numeric_code"],
                "name": row["name"],
                "region": row["region"],
            }
            Country.objects.update_or_create(alpha_code=row["alpha_code"], defaults=defaults)
