import logging
import os

from ccxt import okex
from notecoin.coins.base.file import DataFileProperty

logger = logging.getLogger()
logger.setLevel(logging.INFO)

path_root = '/home/bingtao/workspace/tmp'


def load():
    file_pro = DataFileProperty(exchange=okex(), freq='daily', data_type='trade', path=path_root, timeframe='detail')
    file_pro .change_freq('daily')
    file_pro.load(total=365)
    file_pro .change_freq('weekly')
    file_pro.load(total=54)
    file_pro .change_freq('monthly')
    file_pro.load(total=12)


load()

# nohup /home/bingtao/opt/anaconda3/bin/python /home/bingtao/workspace/notechats/notecoin/notecoin/coins/base/cron.py >>/notechats/notecoin/logs/notecoin-$(date +%Y-%m-%d).log 2>&1 &
