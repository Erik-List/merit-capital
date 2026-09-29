#!/usr/bin/env python3
"""The country vocabulary: every name the inputs use, resolved to ISO 3166-1 alpha-2.

`hq_country` is stored, validated and exported as the two-letter code; rendering
a display name is the frontend's job. `run.py` resolves four inputs through
`canon_country`: a Form D issuer's state or country description (EDGAR renders
foreign countries in capitals and in ISO's older style, "KOREA, REPUBLIC OF",
"KAZAKSTAN"), a Wikidata country label, the unicorn list's country column, and
the judge's own answer.

**The code table is complete** (2026-09-28). It had grown to 107 codes one
rejected batch at a time, and a code it lacked could not be recorded at all:
Xapo (Gibraltar) published as US in two books, Mutual Risk Management (Bermuda)
as US, and Celestia (Liechtenstein) with no country. ISO_NAMES carries all 249
officially assigned codes, current to ISO's 2024-02-29 list as tzdata's
iso3166.tab carries it, plus XK, the user-assigned code the EU and CLDR give
Kosovo, each under its CLDR English name (what the frontend's Intl.DisplayNames
renders).

**A complete table must not turn a loud failure into a silent wrong answer.**
A string the old table resolved resolves exactly as before, the Georgia
collision included: EDGAR's "GEORGIA" is the US state, and the nineteen
Wikidata labels reading "Georgia" were all bad joins on one-word names (Mosaic,
Super, Tempo) that the collision happened to send to US. Only strings the old
table could not resolve changed, each measured on 2026-09-28 against every
Form D ISSUERS description (74 quarters), every Wikidata label in the books'
layer-B caches and the unicorn list:

1. **A filing haven carries no signal** (HAVENS). Its business address is a
   fund vehicle's or a registered office, not where a company operates, so the
   row falls through to the next country source. Mauritius alone is 529
   issuers, nearly all India- and Africa-focused fund vehicles; Nanox files
   from Gibraltar and operates in Israel; FTX Trading filed from Antigua.
2. **A dropdown mis-pick carries no signal** (NO_SIGNAL_CODES). Every issuer
   naming North Korea is in Seoul, the British Indian Ocean Territory filer is
   in Tortola, the US Minor Outlying Islands filers are in Fort Lauderdale and
   New York.
3. **A state that no longer exists carries no signal** (NO_SIGNAL). Wikidata
   gave Czechoslovakia, the Soviet Union, the German Reich, British Hong Kong
   and the People's Republic of Bulgaria for companies founded after them: a
   bad join, never a headquarters.

A code is always accepted as written, havens included, so a judge who places
a company in Gibraltar records GI. A string that is none of the above and names
no country, the unicorn list's "Israel / United States", still comes back
verbatim, so verify flags it instead of the signal being lost.
"""
from __future__ import annotations

import re
import unicodedata

ISO_NAMES = {
    "AD": "Andorra", "AE": "United Arab Emirates", "AF": "Afghanistan",
    "AG": "Antigua & Barbuda", "AI": "Anguilla", "AL": "Albania", "AM": "Armenia",
    "AO": "Angola", "AQ": "Antarctica", "AR": "Argentina", "AS": "American Samoa",
    "AT": "Austria", "AU": "Australia", "AW": "Aruba", "AX": "Åland Islands",
    "AZ": "Azerbaijan", "BA": "Bosnia & Herzegovina", "BB": "Barbados",
    "BD": "Bangladesh", "BE": "Belgium", "BF": "Burkina Faso", "BG": "Bulgaria",
    "BH": "Bahrain", "BI": "Burundi", "BJ": "Benin", "BL": "St. Barthélemy",
    "BM": "Bermuda", "BN": "Brunei", "BO": "Bolivia", "BQ": "Caribbean Netherlands",
    "BR": "Brazil", "BS": "Bahamas", "BT": "Bhutan", "BV": "Bouvet Island",
    "BW": "Botswana", "BY": "Belarus", "BZ": "Belize", "CA": "Canada",
    "CC": "Cocos (Keeling) Islands", "CD": "Congo - Kinshasa",
    "CF": "Central African Republic", "CG": "Congo - Brazzaville", "CH": "Switzerland",
    "CI": "Côte d’Ivoire", "CK": "Cook Islands", "CL": "Chile", "CM": "Cameroon",
    "CN": "China", "CO": "Colombia", "CR": "Costa Rica", "CU": "Cuba",
    "CV": "Cape Verde", "CW": "Curaçao", "CX": "Christmas Island", "CY": "Cyprus",
    "CZ": "Czechia", "DE": "Germany", "DJ": "Djibouti", "DK": "Denmark",
    "DM": "Dominica", "DO": "Dominican Republic", "DZ": "Algeria", "EC": "Ecuador",
    "EE": "Estonia", "EG": "Egypt", "EH": "Western Sahara", "ER": "Eritrea",
    "ES": "Spain", "ET": "Ethiopia", "FI": "Finland", "FJ": "Fiji",
    "FK": "Falkland Islands", "FM": "Micronesia", "FO": "Faroe Islands", "FR": "France",
    "GA": "Gabon", "GB": "United Kingdom", "GD": "Grenada", "GE": "Georgia",
    "GF": "French Guiana", "GG": "Guernsey", "GH": "Ghana", "GI": "Gibraltar",
    "GL": "Greenland", "GM": "Gambia", "GN": "Guinea", "GP": "Guadeloupe",
    "GQ": "Equatorial Guinea", "GR": "Greece",
    "GS": "South Georgia & South Sandwich Islands", "GT": "Guatemala", "GU": "Guam",
    "GW": "Guinea-Bissau", "GY": "Guyana", "HK": "Hong Kong SAR China",
    "HM": "Heard & McDonald Islands", "HN": "Honduras", "HR": "Croatia", "HT": "Haiti",
    "HU": "Hungary", "ID": "Indonesia", "IE": "Ireland", "IL": "Israel",
    "IM": "Isle of Man", "IN": "India", "IO": "British Indian Ocean Territory",
    "IQ": "Iraq", "IR": "Iran", "IS": "Iceland", "IT": "Italy", "JE": "Jersey",
    "JM": "Jamaica", "JO": "Jordan", "JP": "Japan", "KE": "Kenya", "KG": "Kyrgyzstan",
    "KH": "Cambodia", "KI": "Kiribati", "KM": "Comoros", "KN": "St. Kitts & Nevis",
    "KP": "North Korea", "KR": "South Korea", "KW": "Kuwait", "KY": "Cayman Islands",
    "KZ": "Kazakhstan", "LA": "Laos", "LB": "Lebanon", "LC": "St. Lucia",
    "LI": "Liechtenstein", "LK": "Sri Lanka", "LR": "Liberia", "LS": "Lesotho",
    "LT": "Lithuania", "LU": "Luxembourg", "LV": "Latvia", "LY": "Libya",
    "MA": "Morocco", "MC": "Monaco", "MD": "Moldova", "ME": "Montenegro",
    "MF": "St. Martin", "MG": "Madagascar", "MH": "Marshall Islands",
    "MK": "North Macedonia", "ML": "Mali", "MM": "Myanmar (Burma)", "MN": "Mongolia",
    "MO": "Macao SAR China", "MP": "Northern Mariana Islands", "MQ": "Martinique",
    "MR": "Mauritania", "MS": "Montserrat", "MT": "Malta", "MU": "Mauritius",
    "MV": "Maldives", "MW": "Malawi", "MX": "Mexico", "MY": "Malaysia",
    "MZ": "Mozambique", "NA": "Namibia", "NC": "New Caledonia", "NE": "Niger",
    "NF": "Norfolk Island", "NG": "Nigeria", "NI": "Nicaragua", "NL": "Netherlands",
    "NO": "Norway", "NP": "Nepal", "NR": "Nauru", "NU": "Niue", "NZ": "New Zealand",
    "OM": "Oman", "PA": "Panama", "PE": "Peru", "PF": "French Polynesia",
    "PG": "Papua New Guinea", "PH": "Philippines", "PK": "Pakistan", "PL": "Poland",
    "PM": "St. Pierre & Miquelon", "PN": "Pitcairn Islands", "PR": "Puerto Rico",
    "PS": "Palestinian Territories", "PT": "Portugal", "PW": "Palau", "PY": "Paraguay",
    "QA": "Qatar", "RE": "Réunion", "RO": "Romania", "RS": "Serbia", "RU": "Russia",
    "RW": "Rwanda", "SA": "Saudi Arabia", "SB": "Solomon Islands", "SC": "Seychelles",
    "SD": "Sudan", "SE": "Sweden", "SG": "Singapore", "SH": "St. Helena",
    "SI": "Slovenia", "SJ": "Svalbard & Jan Mayen", "SK": "Slovakia",
    "SL": "Sierra Leone", "SM": "San Marino", "SN": "Senegal", "SO": "Somalia",
    "SR": "Suriname", "SS": "South Sudan", "ST": "São Tomé & Príncipe",
    "SV": "El Salvador", "SX": "Sint Maarten", "SY": "Syria", "SZ": "Eswatini",
    "TC": "Turks & Caicos Islands", "TD": "Chad", "TF": "French Southern Territories",
    "TG": "Togo", "TH": "Thailand", "TJ": "Tajikistan", "TK": "Tokelau",
    "TL": "Timor-Leste", "TM": "Turkmenistan", "TN": "Tunisia", "TO": "Tonga",
    "TR": "Türkiye", "TT": "Trinidad & Tobago", "TV": "Tuvalu", "TW": "Taiwan",
    "TZ": "Tanzania", "UA": "Ukraine", "UG": "Uganda", "UM": "U.S. Outlying Islands",
    "US": "United States", "UY": "Uruguay", "UZ": "Uzbekistan", "VA": "Vatican City",
    "VC": "St. Vincent & Grenadines", "VE": "Venezuela", "VG": "British Virgin Islands",
    "VI": "U.S. Virgin Islands", "VN": "Vietnam", "VU": "Vanuatu",
    "WF": "Wallis & Futuna", "WS": "Samoa", "XK": "Kosovo", "YE": "Yemen",
    "YT": "Mayotte", "ZA": "South Africa", "ZM": "Zambia", "ZW": "Zimbabwe",
}

ISO_CODES = frozenset(ISO_NAMES)

# Other names the inputs use for a code, matched after country_key folds case,
# accents, punctuation, "&", "St." and "the": EDGAR's ISO-style descriptions,
# tzdata's and older spellings, and the long forms Wikidata and YC's directory
# carry. CLDR's own names (ISO_NAMES) need no entry here.
ALIASES = {
    "United States of America": "US", "USA": "US", "U.S.": "US", "U.S.A.": "US",
    "UK": "GB", "Great Britain": "GB", "Britain": "GB", "Britain (UK)": "GB",
    "England": "GB", "Scotland": "GB", "Wales": "GB", "Northern Ireland": "GB",
    "Kingdom of the Netherlands": "NL", "Holland": "NL",
    "People's Republic of China": "CN", "Mainland China": "CN",
    "Hong Kong": "HK", "Macau": "MO", "Macao": "MO",
    "Taiwan, Province of China": "TW",
    "Korea, Republic of": "KR", "Republic of Korea": "KR", "Korea (South)": "KR",
    "Korea, Democratic People's Republic of": "KP", "Korea (North)": "KP",
    "Russian Federation": "RU", "Viet Nam": "VN", "Republic of Ireland": "IE",
    "Czech Republic": "CZ", "Slovak Republic": "SK", "Turkey": "TR",
    "UAE": "AE", "Ivory Coast": "CI", "Myanmar": "MM", "Burma": "MM",
    "Democratic Republic of the Congo": "CD", "Congo, The Democratic Republic of the": "CD",
    "DR Congo": "CD", "Congo": "CG", "Republic of the Congo": "CG",
    "Palestine": "PS", "State of Palestine": "PS", "Palestinian Territory, Occupied": "PS",
    "Iran, Islamic Republic of": "IR", "Syrian Arab Republic": "SY",
    "Lao People's Democratic Republic": "LA", "Libyan Arab Jamahiriya": "LY",
    "Moldova, Republic of": "MD", "Bolivia, Plurinational State of": "BO",
    "Venezuela, Bolivarian Republic of": "VE", "Tanzania, United Republic of": "TZ",
    "Micronesia, Federated States of": "FM", "Macedonia": "MK",
    "Macedonia, the Former Yugoslav Republic of": "MK", "Holy See": "VA",
    "Holy See (Vatican City State)": "VA", "Brunei Darussalam": "BN", "Cabo Verde": "CV",
    "East Timor": "TL", "Swaziland": "SZ", "Kazakstan": "KZ", "Kyrgyz Republic": "KG",
    "Surinam": "SR", "Bonaire, Sint Eustatius and Saba": "BQ",
    "Virgin Islands, British": "VG", "Virgin Islands, U.S.": "VI",
    "United States Minor Outlying Islands": "UM",
    # ISO's current long forms, which EDGAR may adopt
    "United Kingdom of Great Britain and Northern Ireland": "GB",
    "Netherlands (Kingdom of the)": "NL", "Palestine, State of": "PS",
    "Saint Martin (French part)": "MF", "Sint Maarten (Dutch part)": "SX",
    "Heard Island and McDonald Islands": "HM", "Pitcairn": "PN",
    "Falkland Islands (Malvinas)": "FK",
}

# US states (EDGAR's ISSUERS descriptions, in capitals) collapse to US.
US_STATES = {
    "ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO",
    "CONNECTICUT", "DELAWARE", "DISTRICT OF COLUMBIA", "FLORIDA", "GEORGIA",
    "HAWAII", "IDAHO", "ILLINOIS", "INDIANA", "IOWA", "KANSAS", "KENTUCKY",
    "LOUISIANA", "MAINE", "MARYLAND", "MASSACHUSETTS", "MICHIGAN", "MINNESOTA",
    "MISSISSIPPI", "MISSOURI", "MONTANA", "NEBRASKA", "NEVADA", "NEW HAMPSHIRE",
    "NEW JERSEY", "NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA",
    "OHIO", "OKLAHOMA", "OREGON", "PENNSYLVANIA", "PUERTO RICO", "RHODE ISLAND",
    "SOUTH CAROLINA", "SOUTH DAKOTA", "TENNESSEE", "TEXAS", "UTAH", "VERMONT",
    "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING",
}
# Business addresses in filing havens say nothing about where a company
# operates; fall through to the next country source instead. The first seven
# are the original list; the rest joined 2026-09-28 (rule 1 above).
HAVENS = {"KY", "VG", "BM", "BS", "MH", "JE", "GG",
          "MU", "BB", "BZ", "IM", "KN", "LC", "VC", "WS", "AG", "AI", "TC", "CK",
          "GI", "MC", "VI"}
# No company is headquartered here; every filing naming them was a mis-pick.
NO_SIGNAL_CODES = {"KP", "IO", "UM"}
# Names that carry no country: former states (rule 3) and EDGAR's placeholder.
NO_SIGNAL = {"Unknown", "Czechoslovakia", "Soviet Union", "USSR", "German Reich",
             "East Germany", "German Democratic Republic", "Yugoslavia",
             "Serbia and Montenegro", "British Hong Kong", "People's Republic of Bulgaria",
             "Netherlands Antilles"}


def country_key(name: str) -> str:
    """One spelling per country: case, accents, apostrophes, punctuation, "&",
    "St." and "the" folded, so EDGAR's "SAINT KITTS AND NEVIS", CLDR's
    "St. Kitts & Nevis" and "The Bahamas" meet their table entries."""
    s = re.sub(r"['’`]", " ", name)
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\bst\b\.?", "saint", s.replace("&", " and "))
    s = re.sub(r"\bthe\b", " ", s)
    return " ".join(re.findall(r"[a-z0-9]+", s))


BY_NAME = {country_key(n): c for c, n in ISO_NAMES.items()}
BY_NAME.update({country_key(n): c for n, c in ALIASES.items()})
NO_SIGNAL_KEYS = {country_key(n) for n in NO_SIGNAL}


def canon_country(raw: str | None) -> str | None:
    """Normalize an ISSUERS state description, Wikidata label, or free-form
    country to an ISO 3166-1 alpha-2 code; US states collapse to US; a haven, a
    mis-picked dropdown entry, a former state or a Wikidata blank node returns
    None (no signal). An unrecognized name comes back verbatim so verify can
    flag it rather than losing the signal."""
    if not raw:
        return None
    raw = raw.strip()
    if len(raw) == 2 and raw.upper() in ISO_CODES:
        return raw.upper()
    if raw.upper() in US_STATES:
        return "US"
    if "CANADA" in raw.upper():
        return "CA"
    key = country_key(raw)
    if key in NO_SIGNAL_KEYS or raw.startswith("http"):
        return None
    code = BY_NAME.get(key)
    if code is None:
        return raw
    return None if code in HAVENS or code in NO_SIGNAL_CODES else code
