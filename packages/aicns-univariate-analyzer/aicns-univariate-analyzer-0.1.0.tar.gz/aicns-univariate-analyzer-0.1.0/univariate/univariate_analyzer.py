"""
    Univariate Time Series Analyzer module
"""

from pyspark.sql import DataFrame
from typing import Optional, List
from univariate.hook import Hook
from univariate.analyzer import (
    AnalysisReport,
    Analyzer,
    RegularityAnalyzer,
    DescriptiveStatAnalyzer,
)
import logging

logger = logging.getLogger()


class UnivariateAnalyzer:
    """
    Univariate Time Series Analyzer
    """

    def __init__(
        self,
        ts: DataFrame,
        val_col: str = "value",
        time_col: str = "time",
        hooks=Optional[List[Hook]],
    ):
        """

        :param ts: Spark dataframe that has one datatime column, and has one timeseries value(float or number) column
        :param val_col: string column name containing timeseries values
        :param time_col: string column name containing pyspark.sql.DatetimeType
        :param hooks: list of hooks that want to be notified analysis reports
        """
        logger.debug(
            f"Setup Analyzer start, ts: {ts}, val_col: {val_col}, time_col: {time_col}, hooks: {hooks or '[]'}"
        )
        self.ts: DataFrame = ts
        self.hooks: List[Hook] = hooks or []  # todo : default post analysis hook
        self.analysis_queue: List[Analyzer] = list()
        self.time_col_name: str = time_col
        self.data_col_name: str = val_col
        try:
            self.__validate_ts(val_col, time_col)
        except Exception as e:  # todo: Custom exception or specific
            logger.error(
                "Error in validation ts, ts must be pyspark sql dataframe that has one DatatimeType column, "
                "and has one timeseries value(float or number) column"
            )
            raise e
        else:
            regularity_analyzer: Analyzer = RegularityAnalyzer()
            self.regularity_report: AnalysisReport = regularity_analyzer.analyze(
                ts=self.ts, time_col_name=time_col
            )
            self.__notify_report(self.regularity_report)
            self.__enqueue_analysis_job()
        logger.debug("Setup Analyzer finish")

    def __validate_ts(self, val_col: str, time_col: str) -> bool:
        pass

    def __notify_report(self, report: AnalysisReport):
        map(lambda hook: hook.do_post_analysis(report), self.hooks)
        logger.debug("Notify all hook")
        logger.debug("Notify hook finish")

    def __enqueue_analysis_job(self):
        """

        :return:
        """
        logger.debug("enqueue analysis job start")
        if self.regularity_report.parameters["regularity"] == "regular":
            logger.debug("regularity: regular")
            self.analysis_queue.append(DescriptiveStatAnalyzer())
            pass
        elif self.regularity_report.parameters["regularity"] == "irregular":
            logger.debug("regularity: irregular")
            pass
        logger.debug("enqueue analysis job finish")

    def analyze(self):
        """

        :return:
        """
        logger.debug("analyze called")

        reports = list(
            map(
                lambda job: job.analyze(
                    ts=self.ts,
                    time_col_name=self.time_col_name,
                    data_col_name=self.data_col_name,
                ),
                self.analysis_queue,
            )
        )  # todo : Explore parallezing with spark sub(child) context & python asyncio?
        map(
            lambda report: map(lambda hook: hook.do_post_analysis(report), self.hooks),
            reports,
        )
        """
        reports = []
        for job in self.analysis_queue:
            report = job.analyze(ts=self.ts, time_col_name=self.time_col_name, data_col_name=self.data_col_name)
            reports.append(report)
        """  # todo : clean dummy code
        logger.debug("analyze return")
        return reports
