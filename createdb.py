CREATE TABLE "users" (
	"user_id"  SERIAL ,
	"stock_id" INTEGER ,
	"username" VARCHAR ,
	"password" VARCHAR ,
	PRIMARY KEY ("user_id")
);

CREATE TABLE "stocks" (
	"stock_id"  SERIAL ,
	"ticker" CHAR(10) ,
	"company" VARCHAR(20) ,
	"last_price" DECIMAL ,
	"roi" DECIMAL ,
	"roe" DECIMAL ,
	"eps" DECIMAL ,
	"div_yield" DECIMAL ,
	"debt_to_equity" DECIMAL ,
	"current_ratio" DECIMAL ,
	"p/e" DECIMAL ,
	"open_price" DECIMAL ,
	"close_price" INTEGER ,
	"beta" DECIMAL ,
	"52_wk_price_chg" DECIMAL ,
	"volume" INTEGER ,
	"price_change" DECIMAL ,
	"50_day_sma" DECIMAL ,
	"200_day_sma" INTEGER ,
	"rsi" DECIMAL ,
	"macd" INTEGER ,
	"divergence" INTEGER ,
	PRIMARY KEY ("stock_id")
);

ALTER TABLE "users" ADD FOREIGN KEY ("stock_id") REFERENCES "stocks" ("stock_id");