import discord
import random


class DrinkOptions:

    #dump of possible options for right now. Allow users to add to in the future, eventually expand to api

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

    async def _get_gin(self)
        gin = ["G&J GREENALL'S GIN: https://www.totalwine.com/spirits/gin/gj-greenalls-gin/p/16371175?s=801&igrules=true",
            "VINCENZI GIN DI FIORI BLOOD ORANGE: https://www.totalwine.com/spirits/gin/vincenzi-gin-di-fiori-blood-orange/p/234547750?s=801&igrules=true",
            "VINCENZI GIN DI FIORI: https://www.totalwine.com/spirits/gin/vincenzi-gin-di-fiori/p/227604750?s=801&igrules=true",
            "TANQUERAY GIN: https://www.totalwine.com/spirits/gin/tanqueray-gin/p/718175?s=801&igrules=true",
            "CITADELLE GIN: https://www.totalwine.com/spirits/gin/citadelle-gin/p/91961175?s=801&igrules=true",
            "BOMBAY SAPPHIRE: https://www.totalwine.com/spirits/gin/bombay-sapphire/p/1658175?s=801&igrules=true",
            "HENDRICKS GIN: https://www.totalwine.com/spirits/gin/hendricks-gin/p/96365175?s=801&igrules=true",
            "BANKERS CLUB GIN: https://www.totalwine.com/spirits/gin/bankers-club-gin/p/7590175?s=801&igrules=true",
            "NEW AMSTERDAM STRAIGHT GIN: https://www.totalwine.com/spirits/gin/new-amsterdam-straight-gin/p/16925175?s=801&igrules=true",
            "3 HOWLS NAVY STRENGTH GIN: https://www.totalwine.com/spirits/gin/3-howls-navy-strength-gin/p/138003750?s=801&igrules=true"]
        return random.choice(gin)

    async def _get_liqueur(self)
        liqueurs = ["BAILEYS IRISH CREAM: https://www.totalwine.com/spirits/liqueurscordialsschnapps/cream/baileys-irish-cream/p/497175?s=801&igrules=true",
            "GRAND IMPERIAL ORANGE LIQUEUR: https://www.totalwine.com/spirits/liqueurscordialsschnapps/citrus-triple-sec/orange/grand-imperial-orange-liqueur/p/2229750?s=801&igrules=true",
            "GRAND MARNIER: https://www.totalwine.com/spirits/liqueurscordialsschnapps/citrus-triple-sec/orange/grand-marnier/p/1735750?s=801&igrules=true",
            "KAVANAGH IRISH CREAM: https://www.totalwine.com/spirits/liqueurscordialsschnapps/cream/kavanagh-irish-cream/p/113938750?s=801&igrules=true",
            "KAHLUA: https://www.totalwine.com/spirits/liqueurscordialsschnapps/coffee/kahlua/p/1804750?s=801&igrules=true",
            "MIDORI MELON: https://www.totalwine.com/spirits/liqueurscordialsschnapps/fruit/melon/midori-melon/p/1814750?s=801&igrules=true",
            "DI AMORE AMARETTO: https://www.totalwine.com/spirits/liqueurscordialsschnapps/nuts-amaretto/di-amore-amaretto/p/485751?s=801&igrules=true",
            "DRILLAUD STRAWBERRY LIQUEUR: https://www.totalwine.com/spirits/liqueurscordialsschnapps/fruit/strawberry/drillaud-strawberry-liqueur/p/110043750?s=801&igrules=true",
            "VITA DIVINE TRIPLE SEC: https://www.totalwine.com/spirits/liqueurscordialsschnapps/citrus-triple-sec/triple-sec/vita-divine-triple-sec/p/133867750?s=801&igrules=true",
            "FENNELLYS IRISH CREAM: https://www.totalwine.com/spirits/liqueurscordialsschnapps/cream/fennellys-irish-cream/p/38360175?s=801&igrules=true"]
        return random.choice(liqueurs)

    async def _get_r2d(self)
        r2d = ["CAZUL 100 MARGARITA POPS - READY TO FREEZE: https://www.totalwine.com/spirits/ready-to-drink/frozen-freezable-cocktails/ice-pops/cazul-100-margarita-pops-ready-to-freeze/p/234549100?s=801&igrules=true",
            "PAINTED DONKEY PINEAPPLE MARGARITA: https://www.totalwine.com/spirits/ready-to-drink/tequila-cocktails/margarita/painted-donkey-pineapple-margarita/p/234138355?s=801&igrules=true",
            "LOS CABOS BLOOD ORANGE MARGARITA: https://www.totalwine.com/spirits/ready-to-drink/tequila-cocktails/margarita/los-cabos-blood-orange-margarita/p/232797175?s=801&igrules=true",
            "LOS CABOS CLASSIC LIME MARGARITA: https://www.totalwine.com/spirits/ready-to-drink/tequila-cocktails/margarita/los-cabos-classic-lime-margarita/p/232798175?s=801&igrules=true",
            "VEIL BLUEBERRY LAVENDER READY TO DRINK: https://www.totalwine.com/spirits/ready-to-drink/vodka-cocktails/veil-blueberry-lavender-ready-to-drink/p/228231175?s=801&igrules=true",
            "1800 ULTIMATE MARGARITA READY TO DRINK: https://www.totalwine.com/spirits/ready-to-drink/tequila-cocktails/margarita/1800-ultimate-margarita-ready-to-drink/p/15402175?s=801&igrules=true",
            "BACARDI RUM PUNCH: https://www.totalwine.com/spirits/ready-to-drink/rum-cocktails/rum-punch-juice/bacardi-rum-punch/p/179214175?s=801&igrules=true",
            "LOS CABOS SPICY MANGO MARGARITA: https://www.totalwine.com/spirits/ready-to-drink/tequila-cocktails/margarita/los-cabos-spicy-mango-margarita/p/233023175?s=801&igrules=true",
            "HANDY & SCHILLER OLD FASHIONED: https://www.totalwine.com/spirits/ready-to-drink/whiskey-cocktails/old-fashioned/handy-schiller-old-fashioned/p/219076750?s=801&igrules=true",
            "THE PERFECT COCKTAIL OLD FASHIONED: https://www.totalwine.com/spirits/ready-to-drink/whiskey-cocktails/old-fashioned/the-perfect-cocktail-old-fashioned/p/219854100?s=801&igrules=true"]
        return random.choice(r2d)

    async def _get_rum(self)
        rum = ["BACARDI SUPERIOR: https://www.totalwine.com/spirits/rum/silver-rum/bacardi-superior/p/3636175?s=801&igrules=true",
            "CAPTAIN MORGAN SPICED RUM: https://www.totalwine.com/spirits/rum/spiced-rum/captain-morgan-spiced-rum/p/2730175?s=801&igrules=true",
            "JONAH'S CURSE BLACK SPICED RUM: https://www.totalwine.com/spirits/rum/spiced-rum/jonahs-curse-black-spiced-rum/p/150301175?s=801&igrules=true",
            "LARGO BAY COCONUT RUM: https://www.totalwine.com/spirits/rum/flavored-rum/coconut/largo-bay-coconut-rum/p/104522175?s=801&igrules=true",
            "RON ZACAPA 23 CENTENARIO RUM: https://www.totalwine.com/spirits/rum/aged-rum/ron-zacapa-23-centenario-rum/p/15593750?s=801&igrules=true",
            "R. L. SEALE'S FINEST 10 YR OLD RUM: https://www.totalwine.com/spirits/rum/aged-rum/r-l-seales-finest-10-yr-old-rum/p/103766750?s=801&igrules=true",
            "MALIBU COCONUT RUM: https://www.totalwine.com/spirits/rum/flavored-rum/coconut/malibu-coconut-rum/p/649175?s=801&igrules=true",
            "SAILOR JERRY SPICED RUM: https://www.totalwine.com/spirits/rum/spiced-rum/sailor-jerry-spiced-rum/p/98562175?s=801&igrules=true",
            "MYERS'S DARK: https://www.totalwine.com/spirits/rum/dark-rum/myerss-dark/p/2835175?s=801&igrules=true",
            "KIRK & SWEENEY RESERVA DOMINICAN RUM: https://www.totalwine.com/spirits/rum/aged-rum/kirk-sweeney-reserva-dominican-rum/p/130558750?s=801&igrules=true"]
        return random.choice(rum)

    async def _get_scotch(self)
        scotch = ["JOHNNIE WALKER RED LABEL: https://www.totalwine.com/spirits/scotch/blended-scotch/johnnie-walker-red-label/p/633175?s=801&igrules=true",
            "GLEN NESS SINGLE MALT SCOTCH WHISKY: https://www.totalwine.com/spirits/scotch/single-malt/glen-ness-single-malt-scotch-whisky/p/2013175?s=801&igrules=true",
            "SHIELDAIG 'THE CLASSIC' BLEND 12YR: https://www.totalwine.com/spirits/scotch/blended-scotch/shieldaig-the-classic-blend-12yr/p/109031175?s=801&igrules=true",
            "GLEN KIRK 8 YR SINGLE MALT SCOTCH WHISKY: https://www.totalwine.com/spirits/scotch/single-malt/glen-kirk-8-yr-single-malt-scotch-whisky/p/109460750?s=801&igrules=true",
            "GLENLIVET FOUNDER'S RESERVE: https://www.totalwine.com/spirits/scotch/single-malt/glenlivet-founders-reserve/p/147281750?s=801&igrules=true",
            "BUCHANAN'S 12 YR: https://www.totalwine.com/spirits/scotch/blended-scotch/buchanans-12-yr/p/17349175?s=801&igrules=true",
            "GRANGESTONE 12 YR SINGLE MALT SCOTCH WHISKY: https://www.totalwine.com/spirits/scotch/single-malt/grangestone-12-yr-single-malt-scotch-whisky/p/115861750?s=801&igrules=true",
            "GLEN LOGIE BLENDED SCOTCH: https://www.totalwine.com/spirits/scotch/glen-logie-blended-scotch/p/159828175?s=801&igrules=true",
            "GRANGESTONE BOURBON CASK FINISH SINGLE MALT SCOTCH WHISKY: https://www.totalwine.com/spirits/scotch/single-malt/grangestone-bourbon-cask-finish-single-malt-scotch-whisky/p/135113175?s=801&igrules=true",
            "GLEN FOHDRY FRENCH OAK CASK: https://www.totalwine.com/spirits/scotch/single-malt/glen-fohdry-french-oak-cask/p/189872750?s=801&igrules=true"]
        return random.choice(scotch)

    async def _get_tequila(self)
        tequila = ["LOS CABOS SILVER TEQUILA: https://www.totalwine.com/spirits/tequila/blancosilver/los-cabos-silver-tequila/p/233715175?s=801&igrules=true",
            "7 LEGUAS BLANCO TEQUILA: https://www.totalwine.com/spirits/tequila/blancosilver/7-leguas-blanco-tequila/p/101628750?s=801&igrules=true",
            "PARTIDA TEQUILA BLANCO: https://www.totalwine.com/spirits/tequila/blancosilver/partida-tequila-blanco/p/3780750?s=801&igrules=true",
            "DULCE VIDA LIME TEQUILA: https://www.totalwine.com/spirits/tequila/flavored-tequila/lime-citrus/dulce-vida-lime-tequila/p/173623750?s=801&igrules=true",
            "LIBRE MELON TEQUILA: https://www.totalwine.com/spirits/tequila/flavored-tequila/libre-melon-tequila/p/189836750?s=801&igrules=true",
            "EL SATIVO BLANCO TEQUILA: https://www.totalwine.com/spirits/tequila/blancosilver/el-sativo-blanco-tequila/p/227252750?s=801&igrules=true",
            "DELEON PREMIUM ANEJO TEQUILA: https://www.totalwine.com/spirits/tequila/anejo/deleon-premium-anejo-tequila/p/147028750?s=801&igrules=true",
            "DULCE VIDA GRAPEFRUIT TEQUILA: https://www.totalwine.com/spirits/tequila/flavored-tequila/lime-citrus/dulce-vida-grapefruit-tequila/p/173622750?s=801&igrules=true",
            "JOSE CUERVO RESERVA DE LA FAMILIA PLATINO: https://www.totalwine.com/spirits/tequila/blancosilver/jose-cuervo-reserva-de-la-familia-platino/p/100572375?s=801&igrules=true",
            "GRAND MAYAN SILVER TEQUILA: https://www.totalwine.com/spirits/tequila/blancosilver/grand-mayan-silver-tequila/p/130630750?s=801&igrules=true"]
        return random.choice(tequila)

    async def _get_vodka(self)
        vodka = ["44 NORTH HUCKLEBERRY VODKA: https://www.totalwine.com/spirits/vodka/flavored-vodka/huckleberry/44-north-huckleberry-vodka/p/15776750?s=801&igrules=true",
            "DIXIE VODKA: https://www.totalwine.com/spirits/vodka/vodka/dixie-vodka/p/139681750?s=801&igrules=true",
            "EFFEN VODKA: https://www.totalwine.com/spirits/vodka/vodka/effen-vodka/p/98310750?s=801&igrules=true",
            "THREE OLIVES VODKA: https://www.totalwine.com/spirits/vodka/vodka/three-olives-vodka/p/94667175?s=801&igrules=true",
            "BELVEDERE SMOGORY FOREST VODKA: https://www.totalwine.com/spirits/vodka/vodka/belvedere-smogory-forest-vodka/p/191349750?s=801&igrules=true",
            "BELVEDERE GINGER ZEST: https://www.totalwine.com/spirits/vodka/flavored-vodka/ginger/belvedere-ginger-zest/p/193110750?s=801&igrules=true",
            "CRATER LAKE VODKA: https://www.totalwine.com/spirits/vodka/vodka/crater-lake-vodka/p/3731750?s=801&igrules=true",
            "NEW AMSTERDAM WATERMELON VODKA: https://www.totalwine.com/spirits/vodka/flavored-vodka/watermelon/new-amsterdam-watermelon-vodka/p/228200750?s=801&igrules=true",
            "CIROC VODKA RED BERRY: https://www.totalwine.com/spirits/vodka/flavored-vodka/mixed-fruit/ciroc-vodka-red-berry/p/109511050?s=801&igrules=true",
            "TWENTY GRAND VODKA PEACH: https://www.totalwine.com/spirits/vodka/flavored-vodka/peach/twenty-grand-vodka-peach/p/159423750?s=801&igrules=true"]
        return random.choice(vodka)

    async def _get_whiskey(self)
        whiskey = ["CROWN ROYAL: https://www.totalwine.com/spirits/canadian-whisky/crown-royal/p/2740175?s=801&igrules=true",
            "JACK DANIELS BLACK: https://www.totalwine.com/spirits/american-whiskey/tennessee-whiskey/jack-daniels-black/p/1782175?s=801&igrules=true",
            "JAMESON IRISH WHISKEY: https://www.totalwine.com/spirits/irish-whiskey/jameson-irish-whiskey/p/2812175?s=801&igrules=true",
            "JIM BEAM PEACH: https://www.totalwine.com/spirits/american-whiskey/whiskey/jim-beam-peach/p/217055175?s=801&igrules=true",
            "BALLOTIN CARAMEL TURTLE WHISKEY: https://www.totalwine.com/spirits/american-whiskey/ballotin-caramel-turtle-whiskey/p/173083750?s=801&igrules=true",
            "FOUR ROSES OBSV CASK SINGLE BARREL SELECT: https://www.totalwine.com/spirits/bourbon/small-batch-bourbon/four-roses-obsv-cask-single-barrel-select/p/145345750?s=801&igrules=true",
            "VIRGIL KAINE GINGER INFUSED BOURBON: https://www.totalwine.com/spirits/bourbon/virgil-kaine-ginger-infused-bourbon/p/121349750?s=801&igrules=true",
            "BIRD DOG CHOCOLATE WHISKEY: https://www.totalwine.com/spirits/american-whiskey/bird-dog-chocolate-whiskey/p/146243750?s=801&igrules=true",
            "REBEL GINGER WHISKEY: https://www.totalwine.com/spirits/american-whiskey/whiskey/rebel-ginger-whiskey/p/173063750?s=801&igrules=true",
            "EMERALD SPRINGS 120: https://www.totalwine.com/spirits/white-whiskeymoonshine/emerald-springs-120/p/232234175?s=801&igrules=true"]
        return random.choice(whiskey)
