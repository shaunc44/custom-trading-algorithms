# import feedparser
# from bs4 import BeautifulSoup
# import requests
# from datetime import datetime, date, timedelta
# from django.shortcuts import render
# import json
# import time
from models import run_model
from celery import Celery


celery_app = Celery('algo_tasker', backend='rpc://', broker='amqp://')





@celery_app.task
def algo_task(rundate, enddate, lp_low, lp_high, pe_low, pe_high, dy_low, dy_high, rsi_buy, rsi_sell):

	run = run_model.RunLoop(rundate, enddate, lp_low, lp_high, pe_low, pe_high, dy_low, dy_high, rsi_buy, rsi_sell)
	run.run_loop()

	print ("Loop running")