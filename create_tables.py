#!/usr/bin/env python3
import pymysql.cursors
import csv


conn = pymysql.connect(host='localhost',
	user='scox',
	password='scox',
	db='trading_algo',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor
	)

cursor = conn.cursor()


cursor.execute('''
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS user;
SET foreign_key_checks = 1;
CREATE TABLE user (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
username VARCHAR(128) NOT NULL, 
password VARCHAR(128) NOT NULL
);''')


# cursor.execute('''
# SET foreign_key_checks = 0;
# DROP TABLE IF EXISTS price;
# SET foreign_key_checks = 1;
# CREATE TABLE price (
# id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
# ticker_id INTEGER NOT NULL,
# ticker VARCHAR(128) NOT NULL,
# date VARCHAR(128) NOT NULL,
# adj_close FLOAT NULL,
# adj_volume FLOAT NULL
# );''')


cursor.execute('''
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS price;
SET foreign_key_checks = 1;
CREATE TABLE price (
  ticker_id INTEGER NOT NULL,
  date VARCHAR(128) NOT NULL,
  adj_close FLOAT NULL,
  adj_volume FLOAT NULL
)
PARTITION BY RANGE COLUMNS(date) (
  PARTITION pLESSTHAN1990 VALUES LESS THAN ('1989-12-31'),
  PARTITION pLESSTHAN2000 VALUES LESS THAN ('1999-12-31'),
  PARTITION pLESSTHAN2005 VALUES LESS THAN ('2004-12-31'),
  PARTITION pLESSTHAN2006 VALUES LESS THAN ('2005-12-31'),
  PARTITION pLESSTHAN2007 VALUES LESS THAN ('2006-12-31'),
  PARTITION pLESSTHAN2008 VALUES LESS THAN ('2007-12-31'),
  PARTITION pLESSTHAN2009 VALUES LESS THAN ('2008-12-31'),
  PARTITION pLESSTHAN2010 VALUES LESS THAN ('2009-12-31'),
  PARTITION pLESSTHAN2011 VALUES LESS THAN ('2010-12-31'),
  PARTITION pLESSTHAN2012 VALUES LESS THAN ('2011-12-31'),
  PARTITION pLESSTHAN2013 VALUES LESS THAN ('2012-12-31'),
  PARTITION pLESSTHAN2014 VALUES LESS THAN ('2013-12-31'),
  PARTITION pLESSTHAN2015 VALUES LESS THAN ('2014-12-31'),
  PARTITION pLESSTHAN2016 VALUES LESS THAN ('2015-12-31'),
  PARTITION pLESSTHAN2017 VALUES LESS THAN ('2016-12-31'),
  PARTITION pMAX VALUES LESS THAN (MAXVALUE)
);
''')


cursor.execute('''
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS ticker;
SET foreign_key_checks = 1;
CREATE TABLE ticker (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
symbol VARCHAR(128) NOT NULL
);''')


cursor.execute('''
SET foreign_key_checks = 0;
DROP TABLE IF EXISTS fundamental;
SET foreign_key_checks = 1;
CREATE TABLE fundamental (
	ticker_id INTEGER NOT NULL,
	date VARCHAR(128) NOT NULL,
	value FLOAT NULL,
	indicator VARCHAR(128) NOT NULL,
	dimension VARCHAR(128) NULL
)
PARTITION BY LIST COLUMNS(indicator) (
	PARTITION pACCOCI VALUES IN('ACCOCI'),
	PARTITION pASSETS VALUES IN('ASSETS'),
	PARTITION pASSETSAVG VALUES IN('ASSETSAVG'),
	PARTITION pASSETSC VALUES IN('ASSETSC'),
	PARTITION pASSETSNC VALUES IN('ASSETSNC'),
	PARTITION pASSETTURNOVER VALUES IN('ASSETTURNOVER'),
	PARTITION pBVPS VALUES IN('BVPS'),
	PARTITION pCALENDARDATE VALUES IN('CALENDARDATE'),
	PARTITION pCAPEX VALUES IN('CAPEX'),
	PARTITION pCASHNEQ VALUES IN('CASHNEQ'),
	PARTITION pCASHNEQUSD VALUES IN('CASHNEQUSD'),
	PARTITION pCONSOLINC VALUES IN('CONSOLINC'),
	PARTITION pCOR VALUES IN('COR'),
	PARTITION pCURRENTRATIO VALUES IN('CURRENTRATIO'),
	PARTITION pDATEKEY VALUES IN('DATEKEY'),
	PARTITION pDE VALUES IN('DE'),
	PARTITION pDEBT VALUES IN('DEBT'),
	PARTITION pDEBTC VALUES IN('DEBTC'),
	PARTITION pDEBTNC VALUES IN('DEBTNC'),
	PARTITION pDEBTUSD VALUES IN('DEBTUSD'),
	PARTITION pDEFERREDREV VALUES IN('DEFERREDREV'),
	PARTITION pDEPAMOR VALUES IN('DEPAMOR'),
	PARTITION pDEPOSITS VALUES IN('DEPOSITS'),
	PARTITION pDILUTIONRATIO VALUES IN('DILUTIONRATIO'),
	PARTITION pDIMENSION VALUES IN('DIMENSION'),
	PARTITION pDIVYIELD VALUES IN('DIVYIELD'),
	PARTITION pDPS VALUES IN('DPS'),
	PARTITION pEBIT VALUES IN('EBIT'),
	PARTITION pEBITDA VALUES IN('EBITDA'),
	PARTITION pEBITDAMARGIN VALUES IN('EBITDAMARGIN'),
	PARTITION pEBITDAUSD VALUES IN('EBITDAUSD'),
	PARTITION pEBITUSD VALUES IN('EBITUSD'),
	PARTITION pEBT VALUES IN('EBT'),
	PARTITION pEPS VALUES IN('EPS'),
	PARTITION pEPSDIL VALUES IN('EPSDIL'),
	PARTITION pEPSDILGROWTH1YR VALUES IN('EPSDILGROWTH1YR'),
	PARTITION pEPSGROWTH1YR VALUES IN('EPSGROWTH1YR'),
	PARTITION pEPSUSD VALUES IN('EPSUSD'),
	PARTITION pEQUITY VALUES IN('EQUITY'),
	PARTITION pEQUITYAVG VALUES IN('EQUITYAVG'),
	PARTITION pEQUITYUSD VALUES IN('EQUITYUSD'),
	PARTITION pEV VALUES IN('EV'),
	PARTITION pEVEBIT VALUES IN('EVEBIT'),
	PARTITION pEVEBITDA VALUES IN('EVEBITDA'),
	PARTITION pEVENT VALUES IN('EVENT'),
	PARTITION pFCF VALUES IN('FCF'),
	PARTITION pFCFPS VALUES IN('FCFPS'),
	PARTITION pFILINGDATE VALUES IN('FILINGDATE'),
	PARTITION pFILINGTYPE VALUES IN('FILINGTYPE'),
	PARTITION pFXUSD VALUES IN('FXUSD'),
	PARTITION pGP VALUES IN('GP'),
	PARTITION pGROSSMARGIN VALUES IN('GROSSMARGIN'),
	PARTITION pINTANGIBLES VALUES IN('INTANGIBLES'),
	PARTITION pINTERESTBURDEN VALUES IN('INTERESTBURDEN'),
	PARTITION pINTEXP VALUES IN('INTEXP'),
	PARTITION pINVCAP VALUES IN('INVCAP'),
	PARTITION pINVCAPAVG VALUES IN('INVCAPAVG'),
	PARTITION pINVENTORY VALUES IN('INVENTORY'),
	PARTITION pINVESTMENTS VALUES IN('INVESTMENTS'),
	PARTITION pINVESTMENTSC VALUES IN('INVESTMENTSC'),
	PARTITION pINVESTMENTSNC VALUES IN('INVESTMENTSNC'),
	PARTITION pLASTUPDATED VALUES IN('LASTUPDATED'),
	PARTITION pLEVERAGERATIO VALUES IN('LEVERAGERATIO'),
	PARTITION pLIABILITIES VALUES IN('LIABILITIES'),
	PARTITION pLIABILITIESC VALUES IN('LIABILITIESC'),
	PARTITION pLIABILITIESNC VALUES IN('LIABILITIESNC'),
	PARTITION pMARKETCAP VALUES IN('MARKETCAP'),
	PARTITION pNCF VALUES IN('NCF'),
	PARTITION pNCFBUS VALUES IN('NCFBUS'),
	PARTITION pNCFCOMMON VALUES IN('NCFCOMMON'),
	PARTITION pNCFDEBT VALUES IN('NCFDEBT'),
	PARTITION pNCFDIV VALUES IN('NCFDIV'),
	PARTITION pNCFF VALUES IN('NCFF'),
	PARTITION pNCFI VALUES IN('NCFI'),
	PARTITION pNCFINV VALUES IN('NCFINV'),
	PARTITION pNCFO VALUES IN('NCFO'),
	PARTITION pNCFOGROWTH1YR VALUES IN('NCFOGROWTH1YR'),
	PARTITION pNCFX VALUES IN('NCFX'),
	PARTITION pNETINC VALUES IN('NETINC'),
	PARTITION pNETINCCMN VALUES IN('NETINCCMN'),
	PARTITION pNETINCCMNUSD VALUES IN('NETINCCMNUSD'),
	PARTITION pNETINCDIS VALUES IN('NETINCDIS'),
	PARTITION pNETINCGROWTH1YR VALUES IN('NETINCGROWTH1YR'),
	PARTITION pNETINCNCI VALUES IN('NETINCNCI'),
	PARTITION pNETMARGIN VALUES IN('NETMARGIN'),
	PARTITION pOPEX VALUES IN('OPEX'),
	PARTITION pOPINC VALUES IN('OPINC'),
	PARTITION pPAYABLES VALUES IN('PAYABLES'),
	PARTITION pPAYOUTRATIO VALUES IN('PAYOUTRATIO'),
	PARTITION pPB VALUES IN('PB'),
	PARTITION pPE VALUES IN('PE'),
	PARTITION pPE1 VALUES IN('PE1'),
	PARTITION pPPNENET VALUES IN('PPNENET'),
	PARTITION pPREFDIVIS VALUES IN('PREFDIVIS'),
	PARTITION pPRICE VALUES IN('PRICE'),
	PARTITION pPS VALUES IN('PS'),
	PARTITION pPS1 VALUES IN('PS1'),
	PARTITION pRECEIVABLES VALUES IN('RECEIVABLES'),
	PARTITION pREPORTPERIOD VALUES IN('REPORTPERIOD'),
	PARTITION pRETEARN VALUES IN('RETEARN'),
	PARTITION pREVENUE VALUES IN('REVENUE'),
	PARTITION pREVENUEGROWTH1YR VALUES IN('REVENUEGROWTH1YR'),
	PARTITION pREVENUEUSD VALUES IN('REVENUEUSD'),
	PARTITION pRND VALUES IN('RND'),
	PARTITION pROA VALUES IN('ROA'),
	PARTITION pROE VALUES IN('ROE'),
	PARTITION pROIC VALUES IN('ROIC'),
	PARTITION pROS VALUES IN('ROS'),
	PARTITION pSBCOMP VALUES IN('SBCOMP'),
	PARTITION pSGNA VALUES IN('SGNA'),
	PARTITION pSHAREFACTOR VALUES IN('SHAREFACTOR'),
	PARTITION pSHARESBAS VALUES IN('SHARESBAS'),
	PARTITION pSHARESWA VALUES IN('SHARESWA'),
	PARTITION pSHARESWADIL VALUES IN('SHARESWADIL'),
	PARTITION pSHARESWAGROWTH1YR VALUES IN('SHARESWAGROWTH1YR'),
	PARTITION pSPS VALUES IN('SPS'),
	PARTITION pTANGIBLES VALUES IN('TANGIBLES'),
	PARTITION pTAXASSETS VALUES IN('TAXASSETS'),
	PARTITION pTAXEFFICIENCY VALUES IN('TAXEFFICIENCY'),
	PARTITION pTAXEXP VALUES IN('TAXEXP'),
	PARTITION pTAXLIABILITIES VALUES IN('TAXLIABILITIES'),
	PARTITION pTBVPS VALUES IN('TBVPS'),
	PARTITION pTICKER VALUES IN('TICKER'),
	PARTITION pWORKINGCAPITAL VALUES IN('WORKINGCAPITAL')
);''')


# cursor.execute('''
# SET foreign_key_checks = 0;
# DROP TABLE IF EXISTS fundamental;
# SET foreign_key_checks = 1;
# CREATE TABLE fundamental (
# 	ticker_id INTEGER NOT NULL,
# 	date VARCHAR(128) NOT NULL,
# 	value FLOAT NULL,
# 	indicator VARCHAR(128) NOT NULL,
# 	dimension VARCHAR(128) NULL
# )
# PARTITION BY HASH(ticker_id)
# PARTITIONS 150;
# ''')
#Not ticker_id !!!!!!!!!!!!!!!!!!



cursor.execute('''
ALTER TABLE price ADD FOREIGN KEY (ticker_id) REFERENCES ticker (id);
ALTER TABLE fundamental ADD FOREIGN KEY (ticker_id) REFERENCES ticker (id);
ALTER TABLE user ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE price ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE ticker ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE fundamental ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')






