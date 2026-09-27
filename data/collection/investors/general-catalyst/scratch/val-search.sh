#!/bin/zsh
# Valuation headline search for the A/B pass (nw rows); output to scratch/val-search.out
G=data/collection/investors/general-catalyst
while IFS='|' read -r slug name; do
  echo "== $slug | $name"
  python3 $G/scratch/news.py "\"$name\" valuation" --name "$name" --decode 3 2>&1 | tail -6
done <<'LIST'
awardco|Awardco
color|Color Health
eikon|Eikon Therapeutics
multiverse|Multiverse
superhuman-platform|Grammarly
teamworks|Teamworks
airslate|airSlate
amperity|Amperity
arrivent|ArriVent
athletic-greens|AG1
beast-industries|Beast Industries
cambridge-mobile-telematics|Cambridge Mobile Telematics
content-square|Contentsquare
continuum-analytics|Anaconda
dandy|Dandy
datavant|Datavant
devoted|Devoted Health
fireflies-ai|Fireflies.ai
general-intuition|General Intuition
greenlight-financial-technology|Greenlight
hi-bob|HiBob
hive|Hive AI
iceye|ICEYE
judi-health|Judi Health
kraken-technologies-global-group|Kraken Technologies
lila-sciences|Lila Sciences
material-bank|Material Bank
maze|Maze
minio|MinIO
parabilis-medicines|Parabilis Medicines
perk|Perk
point-wild-holdings|Point Wild
polymarket|Polymarket
spring-health|Spring Health
sword|Sword Health
upside|Upside
wonder|Wonder
zapier|Zapier
LIST
