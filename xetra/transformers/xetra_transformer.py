""" Xetra ETL Component"""
import logging 
from typing import NamedTuple

from xetra.common.s3 import S3BucketConnector

class XetraSourceConfig(NamedTuple):
    """
    Class for source configuration data

    sec_first_extract_date: Determines the date for extracting the source
    src_columns : Source Column Names
    src_col_date: column name for date in source
    src_col_isin: column name for isin in source
    src_col_time: column name for time in source
    src_col_start_price: column name for starting price in source
    src_col_min_price: column name for minimum price in source
    src_col_max_price: column name for maximum price in source
    src_col_traded_vol: column name for traded volume in source
    """

    src_first_extract_date:str
    src_columns: list
    src_col_date: str
    src_col_isin: str
    src_col_time: str
    src_col_start_price:str
    src_col_min_price:str
    src_col_max_price:str
    src_col_traded_vol:str


class XetraTargetConfig(NamedTuple):
    """
    Class for target configuration data

    trg_col_isin: column name for isin in target
    trg_col_date: column name for date in target
    trg_col_op_price: columne name for opening price in target
    trg_col_clos_price: column name for closing price in target
    trg_col_min_price: column name for minimum price in target
    trg_col_max_price:
    trg_col_dail_trad_vol
    trg_cold_ch_prev_clos
    trg_key
    trg_key_date_format
    trg_format:

    """
    trg_col_isin:str
    trg_col_date:str
    trg_col_op_price:str
    trg_col_clos_price:str
    trg_col_min_price:str
    trg_col_max_price:str
    trg_col_dail_trad_vol:str
    trg_cold_ch_prev_clos:str
    trg_key:str
    trg_key_date_format:str
    trg_format:str


class XetraETL():
    """
    Reads the Xetra data, transforms and writes the transformed to target
    """

    def __init__(self , s3_bucket_src:S3BucketConnector, 
                        s3_bucket_trg:S3BucketConnector, meta_key:str, 
                        src_args:XetraSourceConfig, trg_args:XetraTargetConfig):
        """
        Constructor for XetraTransformer

        :param s3_bucket_src: connection to source s3 bucket
        :param s3_bucket_trg: connection to target s3 bucket
        :param meta_keys: used as self.meta_key -> key of meta file
        :param src_args: NamedTouple class with source configuration data
        :param trg_args: NamedTouple class with target configuration data

        """
        self._logger_ = logging.getLogger(__name__)
        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_trg = s3_bucket_trg
        self.meta_key = meta_key
        self.src_args = src_args
        self.trg_args = trg_args
        self.extract_date = 
        self.extract_date_list = 
        self.meta_update_list = 
    def extract(self):
        pass

    def transform_report1(self):
        pass

    def load(self):
        pass

    def etl_report1(self):
        pass
    











