from spark_pipeline_framework.proxy_generator.translator_proxy_base import (
    TranslatorProxyBase,
)
from os import path


# This file was auto-generated by generate_proxies(). It enables auto-complete in PyCharm. Do not edit manually!
class TranslatorsMyTranslator(TranslatorProxyBase):
    def __init__(self) -> None:
        location: str = path.dirname(path.abspath(__file__))
        super().__init__(location=location, csv_file="provider_types.csv")
