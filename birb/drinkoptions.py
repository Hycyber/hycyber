import random

#dump of all possible options for right now. Allow users to add to in the future, eventually expand to api
class DrinkOptions:

    async def _get_bourbon(self):
        bourbon =  ["RUSSELL'S RESERVE 6YR RYE: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/russells-reserve-6yr-rye/p/46841750?s=801&igrules=true",
			"JIM BEAM SINGLE BARREL 108 PROOF: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/jim-beam-single-barrel-108-proof/p/224249750?s=801&igrules=true",
			"VIRGIL KAINE GINGER INFUSED BOURBON: https://www.totalwine.com/spirits/bourbon/virgil-kaine-ginger-infused-bourbon/p/121349750?s=801&igrules=true",
			"BIRD DOG KENTUCKY STRAIGHT BOURBON 84 PROOF: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/bird-dog-kentucky-straight-bourbon-84-proof/p/231881750?s=801&igrules=true",
			"ASW FIDDLER UNISON BOURBON: https://www.totalwine.com/spirits/bourbon/asw-fiddler-unison-bourbon/p/190755750?s=801&igrules=true",
			"HIRSCH HORIZON BOURBON: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/hirsch-horizon-bourbon/p/230979750?s=801&igrules=true",
			"VERY OLD BARTON 90 PF: https://www.totalwine.com/spirits/bourbon/very-old-barton-90-pf/p/169772175?s=801&igrules=true",
			"REDWOOD EMPIRE PIPE DREAM WHISKEY: https://www.totalwine.com/spirits/bourbon/redwood-empire-pipe-dream-whiskey/p/184407750?s=801&igrules=true",
			"PINHOOK FLAGSHIP BOURBON WHISKEY: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/pinhook-flagship-bourbon-whiskey/p/232301750?s=801&igrules=true",
			"JACK DANIELS LEGACY EDITION 2: https://www.totalwine.com/spirits/bourbon/jack-daniels-legacy-edition-2/p/191358750?s=801&igrules=true"]

        return random.choice(bourbon)

    async def _get_brandy(self):
        brandy = ["ABK6 VSOP COGNAC: https://www.totalwine.com/spirits/brandy-cognac/cognac/abk6-vsop-cognac/p/135127750?s=801&igrules=true",
			"1889 ROYAL BRANDY: https://www.totalwine.com/spirits/brandy-cognac/brandy/1889-royal-brandy/p/171047175?s=801&igrules=true",
			"E & J BRANDY: https://www.totalwine.com/spirits/brandy-cognac/brandy/e-j-brandy/p/1007175?s=801&igrules=true",
			"KORBEL BRANDY: https://www.totalwine.com/spirits/brandy-cognac/brandy/korbel-brandy/p/5736175?s=801&igrules=true",
			"FIDELITAS KIRSCHWASSER: https://www.totalwine.com/spirits/brandy-cognac/eau-de-vie/fidelitas-kirschwasser/p/115921750?s=801&igrules=true",
			"CHATEAU DE LAUBADE SIGNATURE ARMAGNAC: https://www.totalwine.com/spirits/brandy-cognac/armagnac/chateau-de-laubade-signature-armagnac/p/117663750?s=801&igrules=true",
			"MAURO SEBASTE MOSCATO GRAPPA: https://github.com/Hycyber/hycyber/edit/main/birb/birb.py",
			"BANKERS CLUB BRANDY: https://www.totalwine.com/spirits/brandy-cognac/brandy/bankers-club-brandy/p/7587175?s=801&igrules=true",
			"CHATEAU DE LACQUY REFERENCE: https://www.totalwine.com/spirits/brandy-cognac/armagnac/chateau-de-lacquy-reference/p/226866750?s=801&igrules=true",
			"D'USSE COGNAC VSOP: https://www.totalwine.com/spirits/brandy-cognac/cognac/dusse-cognac-vsop/p/130477375?s=801&igrules=true"]

        return random.choice(brandy)
