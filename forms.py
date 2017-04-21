import datetime
import calendar
from wtforms import Form, DateTimeField, StringField, IntegerField, FloatField, validators


class FilterForm(Form):
	# date_range
	daterange = DateTimeField('daterange', format='%Y-%m-%d')
	# start_date = #parse date_range here
	# end_date = #parse date_range here
	# trading_dates = [] #get list of distinct trading_days from the price list based on input date range
	# current_date = #need to start with start_date and iterate through list of trading_days to the end_date

	# last_price
	inputLastPriceLow = FloatField('inputLastPriceLow', [validators.NumberRange(min=0, max=999999)])
	inputLastPriceHigh = FloatField('inputLastPriceHigh', [validators.NumberRange(min=0, max=999999)])

	# current_ratio
	inputCurrentRatioLow = FloatField('inputCurrentRatioLow', [validators.NumberRange(min=0, max=999999)])
	inputCurrentRatioHigh = FloatField('inputCurrentRatioHigh', [validators.NumberRange(min=0, max=999999)])

	# price_to_earnings
	inputPeLow = FloatField('inputPeLow', [validators.NumberRange(min=0, max=999999)])
	inputPeHigh = FloatField('inputPeHigh', [validators.NumberRange(min=0, max=999999)])

	# earnings_per_share
	inputEpsLow = FloatField('inputEpsLow', [validators.NumberRange(min=0, max=999999)])
	inputEpsHigh = FloatField('inputEpsHigh', [validators.NumberRange(min=0, max=999999)])

	# return_on_equity
	inputRoeLow = FloatField('inputRoeLow', [validators.NumberRange(min=0, max=999999)])
	inputRoeHigh = FloatField('inputRoeHigh', [validators.NumberRange(min=0, max=999999)])

	# return_on_investment_capital
	inputRoicLow = FloatField('inputRoicLow', [validators.NumberRange(min=0, max=999999)])
	inputRoicHigh = FloatField('inputRoicHigh', [validators.NumberRange(min=0, max=999999)])

	# dividend_yield
	inputDivYieldLow = FloatField('inputDivYieldLow', [validators.NumberRange(min=0, max=999999)])
	inputDivYieldHigh = FloatField('inputDivYieldHigh', [validators.NumberRange(min=0, max=999999)])

	# debt_to_equity
	inputDebtEquityLow = FloatField('inputDebtEquityLow', [validators.NumberRange(min=0, max=999999)])
	inputDebtEquityHigh = FloatField('inputDebtEquityHigh', [validators.NumberRange(min=0, max=999999)])

	# volume_change
	inputVolumeChangeBuy = FloatField('inputVolumeChangeBuy', [validators.NumberRange(min=-100, max=999999)])
	inputVolumeChangeSell = FloatField('inputVolumeChangeSell', [validators.NumberRange(min=-100, max=999999)])

	# price_change
	inputPriceChangeBuy = FloatField('inputPriceChangeBuy', [validators.NumberRange(min=-100, max=999999)])
	inputPriceChangeSell = FloatField('inputPriceChangeSell', [validators.NumberRange(min=-100, max=999999)])

	# rsi
	inputRsiBuy = FloatField('inputRsiBuy', [validators.NumberRange(min=0, max=100)])
	inputRsiSell = FloatField('inputRsiSell', [validators.NumberRange(min=0, max=100)])

	# trailing_stop_loss
	inputStoplossSell = FloatField('inputStoplossSell', [validators.NumberRange(min=0, max=100)])






