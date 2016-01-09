#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 04 22:01:16 2016

@author: David
"""

# Dictionary module

def badNames():    # return dictionary
    return {'AA':'rough, cindery lava',
            'AAA':'American Automobile Association',
            'AAH':'',
            'AAL':'',
            'AAS':'',
            'AB':'abdominal muscle',
            'ABA':'',
            'ABC':'American Broadcasting Commission',
            'ABO':'',
            'ABS':'',
            'ABY':'',
            'ACE':'',
            'ACT':'',
            'AD':'advertisement',
            'ADD':'',
            'ADO':'',
            'ADS':'',
            'ADZ':'',
            'AE':'one',
            'AFF':'',
            'AFK':'away from keyboard',
            'AFT':'',
            'AG':'pert. to agriculture',
            'AGA':'',
            'AGE':'',
            'AGO':'',
            'AGS':'',
            'AH':'to exclaim in amazement',
            'AHA':'',
            'AHI':'',
            'AHS':'',
            'AI':'three-toed sloth',
            'AID':'',
            'AIL':'',
            'AIM':'',
            'AIN':'',
            'AIR':'',
            'AIS':'',
            'AIT':'',
            'AKA':'also known as',
            'AL':'East Indian tree',
            'ALA':'',
            'ALB':'',
            'ALE':'',
            'ALL':'',
            'ALP':'',
            'ALS':'',
            'ALT':'',
            'AM':'to exist',
            'AMA':'',
            'AMI':'',
            'AMP':'',
            'AMU':'',
            'AN':'indefinite article',
            'ANA':'',
            'AND':'',
            'ANE':'',
            'ANI':'',
            'ANT':'',
            'ANY':'',
            'APE':'',
            'APO':'',
            'APP':'',
            'APT':'',
            'AR':'letter \'r\'',
            'ARB':'',
            'ARC':'',
            'ARE':'',
            'ARF':'',
            'ARK':'',
            'ARM':'',
            'ARS':'',
            'ART':'',
            'AS':'to the same degree',
            'ASH':'',
            'ASK':'',
            'ASL':'age, sex, location',
            'ASP':'',
            'ASS':'',
            'AT':'in the location of',
            'ATE':'',
            'ATM':'automated teller machine',
            'ATT':'',
            'AUK':'',
            'AVA':'',
            'AVE':'',
            'AVO':'',
            'AW':'intj. expressing disbelief',
            'AWA':'',
            'AWE':'',
            'AWL':'',
            'AWN':'',
            'AX':'to cut with an ax',
            'AXE':'',
            'AY':'aye',
            'AYE':'',
            'AYS':'',
            'AZO':'',
            'BA':'eternal soul in Egyptian mythology',
            'BAA':'',
            'BAC':'blood alcohol content',
            'BAD':'',
            'BAG':'',
            'BAH':'',
            'BAL':'',
            'BAM':'',
            'BAN':'',
            'BAP':'',
            'BAR':'',
            'BAS':'',
            'BAT':'',
            'BAY':'',
            'BBC':'British Broadcasting Commission',
            'BC':'because',
            'BE':'to exist',
            'BED':'',
            'BEE':'',
            'BEG':'',
            'BEL':'',
            'BEN':'',
            'BES':'',
            'BET':'',
            'BEY':'',
            'BF':'boyfriend',
            'BI':'bisexual',
            'BIB':'',
            'BID':'',
            'BIG':'',
            'BIN':'',
            'BIO':'',
            'BIS':'',
            'BIT':'',
            'BIZ':'',
            'BM':'',
            'BO':'pal',
            'BOA':'',
            'BOB':'',
            'BOD':'',
            'BOG':'',
            'BOO':'',
            'BOP':'',
            'BOS':'',
            'BOT':'',
            'BOW':'',
            'BOX':'',
            'BOY':'',
            'BRA':'',
            'BRO':'',
            'BRR':'',
            'BS':'bull shit',
            'BTW':'by the way',
            'BUB':'',
            'BUD':'',
            'BUG':'',
            'BUM':'',
            'BUN':'',
            'BUR':'',
            'BUS':'',
            'BUT':'',
            'BUY':'',
            'BY':'side issue',
            'BYE':'',
            'BYS':'',
            'CAA':'Civil Aviation Authority',
            'CAB':'',
            'CAD':'',
            'CAM':'',
            'CAN':'',
            'CAP':'',
            'CAR':'',
            'CAT':'',
            'CAW':'',
            'CAY':'',
            'CBS':'Columbia Broadcasting System',
            'CDC':'Centers for Disease Control',
            'CEE':'',
            'CEL':'',
            'CEP':'',
            'CHI':'',
            'CIA':'Central Intelligence Agency',
            'CIG':'',
            'CIS':'',
            'COB':'',
            'COD':'',
            'COG':'',
            'COL':'',
            'CON':'',
            'COO':'',
            'COP':'',
            'COR':'',
            'COS':'',
            'COT':'',
            'COW':'',
            'COX':'',
            'COY':'',
            'COZ':'',
            'CRU':'',
            'CRY':'',
            'CU':'see you',
            'CUB':'',
            'CUD':'',
            'CUE':'',
            'CUM':'',
            'CUP':'',
            'CUR':'',
            'CUT':'',
            'CWM':'',
            'CYA':'see ya',
            'DAB':'',
            'DAD':'',
            'DAG':'',
            'DAH':'',
            'DAK':'',
            'DAL':'',
            'DAM':'',
            'DAN':'',
            'DAP':'',
            'DAW':'',
            'DAY':'',
            'DE':'of, from',
            'DEA':'Drug Enforcement Agency',
            'DEB':'',
            'DED':'',
            'DEE':'',
            'DEF':'',
            'DEL':'',
            'DEN':'',
            'DEV':'',
            'DEW':'',
            'DEX':'',
            'DEY':'',
            'DHS':'Department of Homeland Security',
            'DIB':'',
            'DIC':'',
            'DID':'',
            'DIE':'',
            'DIF':'',
            'DIG':'',
            'DIK':'',
            'DIM':'',
            'DIN':'',
            'DIP':'',
            'DIS':'',
            'DIT':'',
            'DIX':'',
            'DIY':'do it yourself',
            'DL':'download',
            'DO':'to execute/first tone of musical scale',
            'DOC':'',
            'DOD':'Department of Defense',
            'DOE':'',
            'DOE':'Department of Energy',
            'DOG':'',
            'DOL':'',
            'DOM':'',
            'DON':'',
            'DOR':'',
            'DOS':'',
            'DOT':'',
            'DOT':'Department of Transportation',
            'DOW':'',
            'DRY':'',
            'DUB':'',
            'DUD':'',
            'DUE':'',
            'DUG':'',
            'DUH':'',
            'DUI':'',
            'DUN':'',
            'DUO':'',
            'DUP':'',
            'DYE':'',
            'DYK':'',
            'EAR':'',
            'EAT':'',
            'EAU':'',
            'EBB':'',
            'ECU':'',
            'ED':'',
            'ED':'education',
            'EDH':'',
            'EDS':'',
            'EEK':'',
            'EEL':'',
            'EF':'letter \'f\'',
            'EFF':'',
            'EFS':'',
            'EFT':'',
            'EGG':'',
            'EGO':'',
            'EH':'intj. used to indicate lack of understanding',
            'EKE':'',
            'EL':'letter \'l\'',
            'ELD':'',
            'ELF':'',
            'ELK':'',
            'ELL':'',
            'ELM':'',
            'ELS':'',
            'EM':'printer\'s measurement',
            'EME':'',
            'EMS':'',
            'EMU':'',
            'EN':'printer\'s measurement',
            'END':'',
            'ENG':'',
            'ENS':'',
            'EOF':'end of file',
            'EON':'',
            'EPA':'Environmental Protection Agency',
            'ER':'intj. expressing hesitation',
            'ERA':'',
            'ERE':'',
            'ERG':'',
            'ERN':'',
            'ERR':'',
            'ERS':'',
            'ES':'letter \'s\'',
            'ESS':'',
            'ET':'[eat-conj] (to consume)',
            'ETA':'',
            'ETH':'',
            'EVE':'',
            'EWE':'',
            'EX':'letter \'x\'',
            'EYE':'',
            'FA':'fourth tone of diatonic musical scale',
            'FAA':'Federal Aviation Administration',
            'FAB':'',
            'FAD':'',
            'FAG':'',
            'FAN':'',
            'FAQ':'Frequenctly Asked Questions',
            'FAQ':'frequently asked questions',
            'FAR':'',
            'FAS':'',
            'FAT':'',
            'FAX':'',
            'FAY':'',
            'FBI':'Federal Bureau of Investigation',
            'FDA':'Food and Drug Administration',
            'FE':'Hebrew letter (feh, pe)',
            'FED':'',
            'FEE':'',
            'FEH':'',
            'FEM':'',
            'FEN':'',
            'FER':'',
            'FES':'',
            'FET':'',
            'FEU':'',
            'FEW':'',
            'FEY':'',
            'FEZ':'',
            'FHA':'Federal Housing Administration',
            'FIB':'',
            'FID':'',
            'FIE':'',
            'FIG':'',
            'FIL':'',
            'FIN':'',
            'FIR':'',
            'FIT':'',
            'FIX':'',
            'FIZ':'',
            'FLE':'',
            'FLU':'',
            'FLY':'',
            'FOB':'fresh off the boat',
            'FOE':'',
            'FOG':'',
            'FOH':'',
            'FON':'',
            'FOP':'',
            'FOR':'',
            'FOU':'',
            'FOX':'',
            'FOY':'',
            'FRO':'',
            'FRY':'',
            'FU':'',
            'FUB':'',
            'FUC':'',
            'FUD':'',
            'FUG':'',
            'FUK':'',
            'FUN':'',
            'FUR':'',
            'FUX':'',
            'FYI':'for your information',
            'GAB':'',
            'GAD':'',
            'GAE':'',
            'GAG':'',
            'GAL':'',
            'GAM':'',
            'GAN':'',
            'GAO':'General Accounting Office',
            'GAP':'',
            'GAR':'',
            'GAS':'',
            'GAT':'',
            'GAY':'',
            'GED':'',
            'GEE':'',
            'GEL':'',
            'GEM':'',
            'GEN':'',
            'GET':'',
            'GEY':'',
            'GF':'girlfriend',
            'GHI':'',
            'GIB':'',
            'GID':'',
            'GIE':'',
            'GIF':'Graphics Interchange Format',
            'GIG':'',
            'GIN':'',
            'GIP':'',
            'GIT':'',
            'GL':'good luck',
            'GNU':'',
            'GNU':'GNU\'s not Unix!',
            'GO':'to leave/Japanese board game',
            'GOA':'',
            'GOB':'',
            'GOD':'',
            'GOO':'',
            'GOR':'',
            'GOS':'',
            'GOT':'',
            'GOX':'',
            'GOY':'',
            'GPU':'Graphics Processing Unit',
            'GSA':'General Services Agency',
            'GUL':'',
            'GUM':'',
            'GUN':'',
            'GUT':'',
            'GUV':'',
            'GUY':'',
            'GYM':'',
            'GYP':'',
            'HA':'sound expressing triumph',
            'HAD':'',
            'HAE':'',
            'HAG':'',
            'HAH':'',
            'HAJ':'',
            'HAM':'',
            'HAO':'',
            'HAP':'',
            'HAS':'',
            'HAT':'',
            'HAW':'',
            'HAY':'',
            'HE':'male person',
            'HEH':'',
            'HEM':'',
            'HEN':'',
            'HEP':'',
            'HER':'',
            'HES':'',
            'HET':'',
            'HEW':'',
            'HEX':'',
            'HEY':'',
            'HHS':'Health and Human Services',
            'HI':'intj. used as a greeting',
            'HIC':'',
            'HID':'',
            'HIE':'',
            'HIM':'',
            'HIN':'',
            'HIP':'',
            'HIS':'',
            'HIT':'',
            'HIV':'',
            'HM':'intj. expressing thought (hmm)',
            'HMM':'',
            'HO':'intj. used to attract attention to something',
            'HO':'short for whore',
            'HOB':'',
            'HOD':'',
            'HOE':'',
            'HOG':'',
            'HON':'',
            'HOP':'',
            'HOS':'',
            'HOT':'',
            'HOW':'',
            'HOY':'',
            'HUB':'',
            'HUD':'Housing and Urban Development',
            'HUE':'',
            'HUG':'',
            'HUH':'',
            'HUM':'',
            'HUN':'',
            'HUP':'',
            'HUT':'',
            'HYP':'',
            'IC':'I see',
            'ICE':'',
            'ICH':'',
            'ICK':'',
            'ICY':'',
            'ID':'part of psyche related to instinctual impulses',
            'IDK':'I don\'t know',
            'IDS':'',
            'IF':'possible condition',
            'IFF':'',
            'IFS':'',
            'IGG':'',
            'ILK':'',
            'ILL':'',
            'IMP':'',
            'IN':'influence',
            'INK':'',
            'INN':'',
            'INS':'',
            'ION':'',
            'IOU':'I owe you',
            'IRA':'Individual Retirement Account',
            'IRE':'',
            'IRK':'',
            'IRL':'in real life',
            'IRS':'Internal Revenue Service',
            'IS':'to exist',
            'ISM':'',
            'IT':'person playing tag/indefinite pronoun',
            'ITS':'',
            'IVY':'',
            'JAB':'',
            'JAG':'',
            'JAM':'',
            'JAR':'',
            'JAW':'',
            'JAY':'',
            'JEE':'',
            'JET':'',
            'JEU':'',
            'JEW':'',
            'JIB':'',
            'JIG':'',
            'JIN':'',
            'JK':'just kidding',
            'JO':'sweetheart',
            'JOB':'',
            'JOE':'',
            'JOG':'',
            'JOT':'',
            'JOW':'',
            'JOY':'',
            'JUG':'',
            'JUN':'',
            'JUS':'',
            'JUT':'',
            'KA':'Egyptian spiritual self',
            'KAB':'',
            'KAE':'',
            'KAF':'',
            'KAS':'',
            'KAT':'',
            'KAY':'',
            'KEA':'',
            'KEF':'',
            'KEG':'',
            'KEN':'',
            'KEP':'',
            'KEX':'',
            'KEY':'',
            'KGB':'Komitet Gosudarstvennoi Bezopaznosti (Russian CIA)',
            'KHI':'',
            'KI':'vital life-sustaining energy force (qi)',
            'KID':'',
            'KIF':'',
            'KIK':'',
            'KIN':'',
            'KIP':'',
            'KIR':'',
            'KIS':'',
            'KIT':'',
            'KKK':'',
            'KOA':'',
            'KOB':'',
            'KOI':'',
            'KOP':'',
            'KOR':'',
            'KOS':'',
            'KUE':'',
            'KY':'',
            'KYE':'',
            'LA':'sixth tone of diatonic musical scale',
            'LAB':'life\'s a bitch',
            'LAC':'',
            'LAD':'',
            'LAG':'',
            'LAM':'',
            'LAP':'',
            'LAR':'',
            'LAS':'',
            'LAT':'',
            'LAV':'',
            'LAW':'',
            'LAX':'',
            'LAY':'',
            'LCD':'liquid crystal display',
            'LEA':'',
            'LED':'',
            'LEE':'',
            'LEG':'',
            'LEI':'',
            'LEK':'',
            'LES':'',
            'LET':'',
            'LEU':'',
            'LEV':'',
            'LEX':'',
            'LEY':'',
            'LEZ':'',
            'LI':'Chinese unit of distance',
            'LIB':'',
            'LID':'',
            'LIE':'',
            'LIN':'',
            'LIP':'',
            'LIS':'',
            'LIT':'',
            'LIX':'',
            'LO':'intj. used to attract attention',
            'LOB':'',
            'LOG':'',
            'LOL':'laughing out loud',
            'LOO':'',
            'LOP':'',
            'LOT':'',
            'LOW':'',
            'LOX':'',
            'LSD':'',
            'LUG':'',
            'LUM':'',
            'LUV':'',
            'LUX':'',
            'LY':'love ya',
            'LYE':'',
            'MA':'mother',
            'MAC':'',
            'MAD':'',
            'MAE':'',
            'MAG':'',
            'MAN':'',
            'MAP':'',
            'MAR':'',
            'MAS':'',
            'MAT':'',
            'MAW':'',
            'MAX':'',
            'MAY':'',
            'ME':'pronoun referring to myself',
            'MED':'',
            'MEG':'',
            'MEL':'',
            'MEM':'',
            'MEN':'',
            'MET':'',
            'MEW':'',
            'MHO':'',
            'MI':'third tone of diatonic musical scale',
            'MIB':'',
            'MIC':'',
            'MID':'',
            'MIG':'',
            'MIL':'',
            'MIM':'',
            'MIR':'',
            'MIS':'',
            'MIX':'',
            'MM':'intj. expressing satisfaction',
            'MO':'moment',
            'MOA':'',
            'MOB':'',
            'MOC':'',
            'MOD':'',
            'MOG':'',
            'MOL':'',
            'MOM':'',
            'MON':'',
            'MOO':'',
            'MOP':'',
            'MOR':'',
            'MOS':'',
            'MOT':'',
            'MOW':'',
            'MU':'Greek letter',
            'MUD':'',
            'MUG':'',
            'MUM':'',
            'MUN':'',
            'MUS':'',
            'MUT':'',
            'MY':'possessive prounoun',
            'MYC':'',
            'NA':'no',
            'NAB':'',
            'NAE':'',
            'NAG':'',
            'NAH':'',
            'NAM':'',
            'NAN':'',
            'NAP':'',
            'NAW':'',
            'NAY':'',
            'NE':'born with the name of (nee)',
            'NEB':'',
            'NEE':'',
            'NEG':'',
            'NET':'',
            'NEW':'',
            'NFI':'no f***ing idea',
            'NIB':'',
            'NIH':'National Institutes of Health',
            'NIL':'',
            'NIM':'',
            'NIP':'',
            'NIT':'',
            'NIX':'',
            'NM':'never mind',
            'NO':'',
            'NO':'negative reply',
            'NOB':'',
            'NOD':'',
            'NOG':'',
            'NOH':'',
            'NOM':'',
            'NOO':'',
            'NOR':'',
            'NOS':'',
            'NOT':'',
            'NOW':'',
            'NP':'no problem',
            'NRO':'National Reconnaissance Office',
            'NS':'no shit',
            'NSA':'National Security Agency',
            'NTH':'',
            'NU':'Greek letter',
            'NUB':'',
            'NUN':'',
            'NUS':'',
            'NUT':'',
            'NVM':'nevermind',
            'OAF':'',
            'OAK':'',
            'OAR':'',
            'OAT':'',
            'OBA':'',
            'OBE':'',
            'OBI':'',
            'OCA':'',
            'OD':'hypothetical force of natural power',
            'ODA':'',
            'ODD':'',
            'ODE':'',
            'ODS':'',
            'OE':'Faroean wind',
            'OEM':'Original Equipment Manufacturer',
            'OES':'',
            'OF':'coming from',
            'OFF':'',
            'OFT':'',
            'OH':'to exclaim \'oh\'',
            'OHM':'',
            'OHO':'',
            'OHS':'',
            'OI':'intj. expressing dismay (oy)',
            'OIL':'',
            'OK':'okay',
            'OKA':'',
            'OKE':'',
            'OLD':'',
            'OLE':'',
            'OM':'mantra used in meditation',
            'OMB':'Office of Management and Budget',
            'OMG':'oh my god',
            'OMS':'',
            'ON':'side of wicket where cricket batsman stands',
            'ONE':'',
            'ONO':'',
            'ONS':'',
            'OOH':'',
            'OOT':'',
            'OP':'style of abstract art',
            'OPE':'',
            'OPS':'',
            'OPT':'',
            'OR':'heraldic color gold',
            'ORA':'',
            'ORB':'',
            'ORC':'',
            'ORE':'',
            'ORS':'',
            'ORT':'',
            'OS':'orifice/bone/ridge of sand (esker)',
            'OSE':'',
            'OUD':'',
            'OUR':'',
            'OUT':'',
            'OVA':'',
            'OW':'intj. expressing sudden pain',
            'OWE':'',
            'OWL':'',
            'OWN':'',
            'OX':'hoofed mammal/clumsy person',
            'OXO':'',
            'OXY':'',
            'OY':'intj. expressing dismay',
            'PA':'father',
            'PAC':'',
            'PAD':'',
            'PAH':'',
            'PAL':'',
            'PAM':'',
            'PAN':'',
            'PAP':'',
            'PAR':'',
            'PAS':'',
            'PAT':'',
            'PAW':'',
            'PAX':'',
            'PAY':'',
            'PBS':'Public Broadcasting System',
            'PDA':'public display of affection',
            'PE':'Hebrew letter',
            'PEA':'',
            'PEC':'',
            'PED':'',
            'PEE':'',
            'PEG':'',
            'PEH':'',
            'PEN':'',
            'PEP':'',
            'PER':'',
            'PES':'',
            'PET':'',
            'PEW':'',
            'PHI':'',
            'PHT':'',
            'PI':'Greek letter/to jumble',
            'PIA':'',
            'PIC':'',
            'PIE':'',
            'PIG':'',
            'PIN':'',
            'PIN':'Personal Identification Number',
            'PIP':'',
            'PIS':'',
            'PIT':'',
            'PIU':'',
            'PIX':'',
            'PLY':'',
            'PLZ':'please',
            'POD':'',
            'POH':'',
            'POI':'',
            'POL':'',
            'POM':'',
            'POO':'',
            'POP':'',
            'POT':'',
            'POW':'',
            'POX':'',
            'PPL':'people',
            'PRO':'',
            'PRY':'',
            'PS':'post script',
            'PSI':'',
            'PST':'',
            'PUB':'',
            'PUD':'',
            'PUG':'',
            'PUL':'',
            'PUN':'',
            'PUP':'',
            'PUR':'',
            'PUS':'',
            'PUT':'',
            'PYA':'',
            'PYE':'',
            'PYX':'',
            'QAT':'',
            'QI':'vital life-sustaining energy force',
            'QIS':'',
            'QT':'cutie',
            'QUA':'',
            'RAD':'',
            'RAG':'',
            'RAH':'',
            'RAI':'',
            'RAJ':'',
            'RAM':'',
            'RAN':'',
            'RAP':'',
            'RAS':'',
            'RAT':'',
            'RAW':'',
            'RAX':'',
            'RAY':'',
            'RE':'second tone of diatonic musical scale',
            'REB':'',
            'REC':'',
            'RED':'',
            'REE':'',
            'REF':'',
            'REG':'',
            'REI':'',
            'REM':'',
            'REP':'',
            'RES':'',
            'RET':'',
            'REV':'',
            'REX':'',
            'RHO':'',
            'RIA':'',
            'RIB':'',
            'RID':'',
            'RIF':'',
            'RIG':'',
            'RIM':'',
            'RIN':'',
            'RIP':'',
            'ROB':'',
            'ROC':'',
            'ROD':'',
            'ROE':'',
            'ROM':'',
            'ROT':'',
            'ROW':'',
            'RUB':'',
            'RUE':'',
            'RUG':'',
            'RUM':'',
            'RUN':'',
            'RUT':'',
            'RYA':'',
            'RYE':'',
            'SAB':'',
            'SAC':'',
            'SAD':'',
            'SAE':'',
            'SAG':'',
            'SAL':'',
            'SAP':'',
            'SAT':'',
            'SAT':'Scholastic Achievement Test',
            'SAU':'',
            'SAW':'',
            'SAX':'',
            'SAY':'',
            'SEA':'',
            'SEC':'',
            'SEC':'Securities and Exchange Commission',
            'SEE':'',
            'SEG':'',
            'SEI':'',
            'SEL':'',
            'SEN':'',
            'SER':'',
            'SET':'',
            'SEW':'',
            'SEX':'',
            'SH':'intj. used to urge silence',
            'SHA':'',
            'SHE':'',
            'SHH':'',
            'SHY':'',
            'SI':'seventh tone of diatonic musical scale (ti)',
            'SIB':'',
            'SIC':'',
            'SIK':'',
            'SIM':'',
            'SIN':'',
            'SIP':'',
            'SIR':'',
            'SIS':'',
            'SIT':'',
            'SIX':'',
            'SKA':'',
            'SKI':'',
            'SKY':'',
            'SLY':'',
            'SO':'fifth tone of diatonic musical scale',
            'SO':'significant other',
            'SOB':'',
            'SOD':'',
            'SOL':'',
            'SOM':'',
            'SON':'',
            'SOP':'',
            'SOS':'',
            'SOT':'',
            'SOU':'',
            'SOW':'',
            'SOX':'',
            'SOY':'',
            'SPA':'',
            'SPY':'',
            'SQL':'Structured Query Language',
            'SRI':'',
            'SRY':'sorry',
            'SSA':'Social Security Administration',
            'STD':'',
            'STY':'',
            'SUB':'',
            'SUE':'',
            'SUK':'',
            'SUM':'',
            'SUN':'',
            'SUP':'',
            'SUQ':'',
            'SUX':'',
            'SYN':'',
            'TA':'thanks',
            'TAB':'',
            'TAD':'',
            'TAE':'',
            'TAG':'',
            'TAJ':'',
            'TAM':'',
            'TAN':'',
            'TAO':'',
            'TAP':'',
            'TAR':'',
            'TAS':'',
            'TAT':'',
            'TAU':'',
            'TAV':'',
            'TAW':'',
            'TAX':'',
            'TEA':'',
            'TED':'',
            'TEE':'',
            'TEG':'',
            'TEL':'',
            'TEN':'',
            'TET':'',
            'TEW':'',
            'THE':'',
            'THO':'',
            'THX':'thanks',
            'THY':'',
            'TI':'seventh tone of diatonic musical scale',
            'TIC':'',
            'TIE':'',
            'TIL':'',
            'TIN':'',
            'TIP':'',
            'TIS':'',
            'TIT':'',
            'TMI':'too much information',
            'TO':'toward',
            'TOD':'',
            'TOE':'',
            'TOG':'',
            'TOM':'',
            'TON':'',
            'TOO':'',
            'TOP':'',
            'TOR':'',
            'TOT':'',
            'TOW':'',
            'TOY':'',
            'TP':'',
            'TRY':'',
            'TSA':'Transportation Security Agency',
            'TSK':'',
            'TUB':'',
            'TUG':'',
            'TUI':'',
            'TUN':'',
            'TUP':'',
            'TUT':'',
            'TUX':'',
            'TWA':'',
            'TWO':'',
            'TYE':'',
            'UDO':'',
            'UGH':'',
            'UH':'intj. expressing hesitation',
            'UKE':'',
            'ULU':'',
            'UM':'intj. expressing hesitation',
            'UMM':'',
            'UMP':'',
            'UN':'one',
            'UNS':'',
            'UP':'to raise',
            'UPO':'',
            'UPS':'',
            'URB':'',
            'URD':'',
            'URN':'',
            'URP':'',
            'US':'objective pronoun for \'we\'',
            'USA':'United States of America',
            'USE':'',
            'UT':'musical tone in French solmization system',
            'UTA':'',
            'UTE':'',
            'UTS':'',
            'VAC':'',
            'VAN':'',
            'VAR':'',
            'VAS':'',
            'VAT':'',
            'VAU':'',
            'VAV':'',
            'VAW':'',
            'VEE':'',
            'VEG':'',
            'VET':'',
            'VEX':'',
            'VIA':'',
            'VID':'',
            'VIE':'',
            'VIG':'',
            'VIM':'',
            'VIS':'',
            'VOE':'',
            'VOW':'',
            'VOX':'',
            'VUG':'',
            'VUM':'',
            'WAB':'',
            'WAD':'',
            'WAE':'',
            'WAG':'',
            'WAN':'',
            'WAP':'',
            'WAR':'',
            'WAS':'',
            'WAT':'',
            'WAW':'',
            'WAX':'',
            'WAY':'',
            'WE':'plural pronoun',
            'WEB':'',
            'WED':'',
            'WEE':'',
            'WEN':'',
            'WET':'',
            'WHA':'',
            'WHO':'',
            'WHO':'World Health Organization',
            'WHY':'',
            'WIG':'',
            'WIN':'',
            'WIS':'',
            'WIT':'',
            'WIZ':'',
            'WO':'woe',
            'WOE':'',
            'WOG':'',
            'WOK':'',
            'WON':'',
            'WOO':'',
            'WOP':'',
            'WOS':'',
            'WOT':'',
            'WOW':'',
            'WRY':'',
            'WTF':'what the F***?',
            'WUD':'',
            'WWW':'World Wide Web',
            'WYE':'',
            'WYN':'',
            'XI':'Greek letter',
            'XIS':'',
            'XU':'Vietnamese monetary unit',
            'YA':'you',
            'YAG':'',
            'YAH':'',
            'YAK':'',
            'YAM':'',
            'YAP':'',
            'YAR':'',
            'YAW':'',
            'YAY':'',
            'YE':'you',
            'YEA':'',
            'YEH':'',
            'YEN':'',
            'YEP':'',
            'YES':'',
            'YET':'',
            'YEW':'',
            'YID':'',
            'YIN':'',
            'YIP':'',
            'YO':'intj. used to call attention',
            'YOB':'',
            'YOD':'',
            'YOK':'',
            'YOM':'',
            'YON':'',
            'YOU':'',
            'YOW':'',
            'YUK':'',
            'YUM':'',
            'YUP':'',
            'ZA':'pizza',
            'ZAG':'',
            'ZAP':'',
            'ZAS':'',
            'ZAX':'',
            'ZED':'',
            'ZEE':'',
            'ZEK':'',
            'ZEP':'',
            'ZIG':'',
            'ZIN':'',
            'ZIP':'',
            'ZIT':'',
            'ZOA':'',
            'ZOO':'',
            'ZUZ':'',
            'ZZZ':'',}
