from pathlib import Path
from typing import Dict, Any, Optional, Union

# noinspection PyProtectedMember
from pyspark import keyword_only
from pyspark.ml.param import Param
from pyspark.sql.dataframe import DataFrame
from spark_pipeline_framework.logger.yarn_logger import get_logger
from spark_pipeline_framework.progress_logger.progress_logger import ProgressLogger
from spark_pipeline_framework.transformers.framework_parquet_exporter.v1.framework_parquet_exporter import (
    FrameworkParquetExporter,
)
from spark_pipeline_framework.transformers.framework_parquet_loader.v1.framework_parquet_loader import (
    FrameworkParquetLoader,
)
from spark_pipeline_framework.transformers.framework_transformer.v1.framework_transformer import (
    FrameworkTransformer,
)


class FrameworkCheckpoint(FrameworkTransformer):
    """
    Saves given view to parquet and reloads it
    """

    # noinspection PyUnusedLocal
    @keyword_only
    def __init__(
        self,
        file_path: Union[str, Path],
        view: Optional[str] = None,
        name: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        progress_logger: Optional[ProgressLogger] = None,
    ):
        """
        Saves given view to parquet and reload it.
        This is to cut off the Spark lineage by saving to temporary location thus making Spark faster in some cases
        https://jaceklaskowski.gitbooks.io/mastering-spark-sql/content/spark-sql-checkpointing.html
        Normally Spark will run from the beginning of the pipeline to the end but in complex pipelines this can cause
        slowness and "out of memory" errors.
        By doing a checkpoint, we can improve this.  However, the downside of checkpointing is that you can slow the
        pipeline since you're writing out a temporary result to the disk.  So this should be used ONLY when the
        pipelines are slow or running out of memory.


        :param view: view to save to parquet
        :param file_path: where to save
        :param name: a name for the transformer step
        :param parameters: parameters
        :param progress_logger: the logger to use for logging
        """
        super().__init__(
            name=name, parameters=parameters, progress_logger=progress_logger
        )

        self.logger = get_logger(__name__)

        assert isinstance(file_path, Path) or isinstance(file_path, str)
        assert file_path

        assert view

        # add a param
        self.view: Param[str] = Param(self, "view", "")
        self._setDefault(view=view)

        self.file_path: Param[Union[str, Path]] = Param(self, "file_path", "")
        self._setDefault(file_path=None)

        kwargs = self._input_kwargs
        self.setParams(**kwargs)

    def _transform(self, df: DataFrame) -> DataFrame:
        view: str = self.getView()
        file_path: Union[str, Path] = self.getFilePath()

        save_transformer = FrameworkParquetExporter(
            view=view,
            name=f"{self.getName()}-save",
            file_path=file_path,
            parameters=self.getParameters(),
            progress_logger=self.getProgressLogger(),
        )
        df = save_transformer.transform(df)

        load_transformer = FrameworkParquetLoader(
            view=view,
            file_path=file_path,
            name=f"{self.getName()}-load",
            parameters=self.getParameters(),
            progress_logger=self.getProgressLogger(),
        )
        df = load_transformer.transform(df)
        return df

    # noinspection PyPep8Naming,PyMissingOrEmptyDocstring
    def getView(self) -> str:
        return self.getOrDefault(self.view)

    # noinspection PyPep8Naming,PyMissingOrEmptyDocstring
    def getFilePath(self) -> Union[str, Path]:
        return self.getOrDefault(self.file_path)
