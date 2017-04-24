# from dateutil.parser import parse
from wtforms import Form, DateField, FloatField, validators
from wtforms_components import DateRange
import calendar
import datetime


class FilterForm(Form):
	# date_range
	min_date = datetime.datetime.strptime('01/02/2007', '%m/%d/%Y').date()
	max_date = datetime.datetime.strptime('03/28/2017', '%m/%d/%Y').date()

	# start_date
	startdate = DateField('startdate', validators=[DateRange(min=min_date, max=max_date)], format='%m/%d/%Y', default=min_date)

	# end_date
	enddate = DateField('enddate', validators=[DateRange(min=min_date, max=max_date)], format='%m/%d/%Y', default=max_date)

	# last_price
	inputLastPriceLow = FloatField('inputLastPriceLow', [validators.NumberRange(min=0, max=999999)], default=0.0)
	inputLastPriceHigh = FloatField('inputLastPriceHigh', [validators.NumberRange(min=0, max=999999)], default=999999.0)

	# current_ratio
	inputCurrentRatioLow = FloatField('inputCurrentRatioLow', [validators.NumberRange(min=0, max=999999)], default=0)
	inputCurrentRatioHigh = FloatField('inputCurrentRatioHigh', [validators.NumberRange(min=0, max=999999)], default=999999)

	# price_to_earnings
	inputPeLow = FloatField('inputPeLow', [validators.NumberRange(min=-999999, max=999999)], default=-999999)
	inputPeHigh = FloatField('inputPeHigh', [validators.NumberRange(min=0, max=999999)], default=999999)

	# earnings_per_share
	inputEpsLow = FloatField('inputEpsLow', [validators.NumberRange(min=-999999, max=999999)], default=-999999)
	inputEpsHigh = FloatField('inputEpsHigh', [validators.NumberRange(min=0, max=999999)], default=999999)

	# return_on_equity
	inputRoeLow = FloatField('inputRoeLow', [validators.NumberRange(min=-100, max=999999)], default=-100)
	inputRoeHigh = FloatField('inputRoeHigh', [validators.NumberRange(min=0, max=999999)], default=999999)

	# return_on_investment_capital
	inputRoicLow = FloatField('inputRoicLow', [validators.NumberRange(min=-100, max=999999)], default=-100)
	inputRoicHigh = FloatField('inputRoicHigh', [validators.NumberRange(min=0, max=999999)], default=999999)

	# dividend_yield
	inputDivYieldLow = FloatField('inputDivYieldLow', [validators.NumberRange(min=0, max=999999)], default=0)
	inputDivYieldHigh = FloatField('inputDivYieldHigh', [validators.NumberRange(min=0, max=999999)], default=999999)

	# debt_to_equity
	inputDebtEquityLow = FloatField('inputDebtEquityLow', [validators.NumberRange(min=0, max=999999)], default=0)
	inputDebtEquityHigh = FloatField('inputDebtEquityHigh', [validators.NumberRange(min=0, max=999999)], default=999999)

	# AT LEAST ONE OF THESE FIELDS (BUY AND SELL) MUST BE SELECTED
	# volume_change
	inputVolumeChangeBuy = FloatField('inputVolumeChangeBuy', [validators.NumberRange(min=-100, max=999999)], default=False)
	inputVolumeChangeSell = FloatField('inputVolumeChangeSell', [validators.NumberRange(min=-100, max=999999)], default=False)

	# price_change
	inputPriceChangeBuy = FloatField('inputPriceChangeBuy', [validators.NumberRange(min=-100, max=999999)], default=False)
	inputPriceChangeSell = FloatField('inputPriceChangeSell', [validators.NumberRange(min=-100, max=999999)], default=False)

	# rsi
	inputRsiBuy = FloatField('inputRsiBuy', [validators.NumberRange(min=0, max=100)], default=False)
	inputRsiSell = FloatField('inputRsiSell', [validators.NumberRange(min=0, max=100)], default=False)

	# trailing_stop_loss
	inputStoplossSell = FloatField('inputStoplossSell', [validators.NumberRange(min=0, max=100)], default=False)






