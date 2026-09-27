"""Focus pass (COLLECTION.md s6 focus): one primary value from the closed twelve, judged
from the firm's CMS description, the row's note and knowledge, with the standing
precedence rules; unidentified rows carry null. Aligned with sibling books where the
same company is shared and their label follows the precedence rules."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402

AI, DATA, DEV, SAAS, SEC, FIN, CRYPTO, IND, CLIM, HEAL, CONS, MEDIA = (
    "AI & Applied AI", "Data Infrastructure", "DevTools & APIs", "SaaS", "Security", "Fintech & Payments",
    "Crypto & Web3", "Industrial & Robotics", "Climate & Energy", "Healthcare & Bio", "Consumer & Marketplaces",
    "Media, Gaming & Advertising")
F = {
 CONS: "airgarage angie-s-list carewell egroups fetch jow shopping-com sonos the-realreal aptoide asana-rebel atlys blinkist brumbrum bumble citydeal darberry del-icio-us ebook experteer fancy farfetch fotolog goop gopuff gr-ns let-s-do-this lightricks made-com munchery-inc myfab nivoda nom-nom numa palmstreet peerflix powerus shipt shutl smartfrog-canary thrive-market vicampo zippia baron-app-inc viavia-corp zumper-inc",
 SAAS: "appfolio bluekai grin mr-ted prescient-ai uxcam when-i-work ag5 air attio automaited bettercloud buk claap codesignal didero-x expertcity flockjay fonoa-x gofreight housecall-pro icertis karma linc merchantry-inc motion owner partnerize plancraft planradar primo procure-ai searchable segment semrush shopmonkey sparetech staffbase stotles taxwire thread trellis notch",
 FIN: "acorns aiprise apiax azimo braavo brite-payments clyde-technologies-inc coya creditas defacto finom first-aml flutterwave fonoa friendsurance heard helcim payflows pismo plumery raisin recurly skalar swile viabill weavr yeahka",
 MEDIA: "k2-network yume-networks axios clique-brands copa90 homa kaufda maker-studios moretv peanut-labs podimo rojo scopely sorare vuze daily-secret-inc fanhattan-inc reelio-inc",
 AI: "adapt ami-labs black-forest-labs deepip didero fundamental kili-technology mistral mithrl recursive voicea vox-ai zive",
 DATA: "nginx data-ai eucalyptus-systems infiniroute lucidlink netbox-labs pronto-networks rendition-networks speakeasy",
 DEV: "dbeaver honeycomb leapwork massive replicated sqldbm tabnine pragli-inc",
 SEC: "bitwarden closinglock cranite exein graylog mine ncircle vizzia",
 HEAL: "airvet allermi bioptimus blossom-health circadia citizen-health claritycare five-lives get-harley heidi-health natural-cycles upheal verse-medical",
 CLIM: "carbonfact gorilla klima monta roadrunner trawa",
 IND: "sonim-technologies hades robco sereact",
 CRYPTO: "deblock",
}
L = []
seen = set()
for focus, slugs in F.items():
    for s in slugs.split():
        if s.endswith("-x"):
            continue
        assert s not in seen, s
        seen.add(s)
        L.append(cls(s, focus=focus, focus_src="model"))
for s in "indigo journey keeper nouri root tandem".split():
    L.append(cls(s, extra={"focus": None, "focus_source": "model"}))
if __name__ == "__main__":
    write("focus-001", L, record="--dry" not in sys.argv)
