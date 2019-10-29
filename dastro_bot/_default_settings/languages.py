from collections import namedtuple


Messages = namedtuple('Messages', [
    'ship_not_exists',
    'multiple_ships_found',
    'member_not_found',
    'member_ships_modified',
    'member_ships_invalid',
    'member_ship_not_found',
    'ship_price_unknown',
    'ship_from_report_not_found',
    'ship_price_report',
    'new_version',
    'road_map_not_found',
    'something_went_wrong',
    'success',
    'found_nothing',
])

Commands = namedtuple('Commands', [
    'help',
    'fleet',
    'add_ship',
    'remove_ship',
    'clear_member_ships',
    'remove_member',
    'prices',
    'ship',
    'compare',
    'releases',
    'roadmap',
    'trade',
    'trade_prices',
    'mining',
    'trade_report',
    'mining_report',
])

messages_pl = Messages(
    ship_not_exists="%s, taki okręt nie istnieje!",
    multiple_ships_found="Niestety, nie jestem pewien czego dokładnie szukasz druhu. Czy chodziło Ci może o ...\n%s",
    member_not_found="Przykro mi, nie znalazłem takiej osoby.",
    member_ships_modified="Drogi %s, zanotowałem. Oto Twoja aktualna flota:",
    member_ships_invalid="%s, przykro mi lecz takie statki nie istnieją:",
    member_ship_not_found="%s, przykro mi lecz nie posiadasz tego statku.",
    ship_price_unknown="Wybacz Panie Bracie, lecz nie znam ceny okrętu *%s*  **%s**.",
    ship_from_report_not_found="Czołem!\nNie mogłem odnaleźć żadnych wieści o statku *%s*.",
    ship_price_report="Czołem!\n *%s* obecnie kosztuje *%s*",
    new_version="Czołem! Przynoszę Wam wieści:\n%s",
    road_map_not_found="Przykro mi, nic takiego nie znalazłem. Posiadam jednakże wiedzę o poniższych:\n```%s```",
    something_went_wrong="Coś poszło nie tak...",
    success="Udało się!",
    found_nothing="Przykro mi, lecz nic nie znalazłem."
)

commands_pl = Commands(
    help="pomoc",
    fleet="flota",
    add_ship="dodaj",
    remove_ship="usuń",
    clear_member_ships="usuń moje statki",
    remove_member="usuń_członka",
    prices="ceny",
    ship="statek",
    compare="porównaj",
    releases="wersje",
    roadmap="obiecanki",
    trade="handel",
    trade_prices="handel_ceny",
    mining="kopanie",
    trade_report="raport_handlowy",
    mining_report="raport_górniczy",
)

messages_en = Messages(
    ship_not_exists="%s, there's no such ship!",
    multiple_ships_found="Not sure what you mean. Maybe try one of this:\n%s",
    member_not_found="I'm sorry, there's no such member.",
    member_ships_modified="%s Here's your updated fleet:",
    member_ships_invalid="%s, sorry but those ships are not valid:",
    member_ship_not_found="%s, sorry but you don't have such ship.",
    ship_price_unknown="I'm sorry but I don't knowh price of *%s*  **%s**.",
    ship_from_report_not_found="Sorry, didn't find anything on ship *%s*.",
    ship_price_report="The price of *%s* is updated to *%s*",
    new_version="Howdy! I found some news:\n%s",
    road_map_not_found="Sorry, didn't find anything like that. You may try something like:\n```%s```",
    something_went_wrong="Something went wrong...",
    success="Done!",
    found_nothing="I'm sorry. I found nothing."
)

commands_en = Commands(
    help="help",
    fleet="fleet",
    add_ship="add_ship",
    remove_ship="remove_ship",
    clear_member_ships="clear my ships",
    remove_member="remove_member",
    prices="prices",
    ship="ship",
    compare="compare",
    releases="releases",
    roadmap="roadmap",
    trade="trade",
    trade_prices="trade_prices",
    mining="mining",
    trade_report="trade_report",
    mining_report="mining_report",
)

messages_fr = Messages(
    ship_not_exists="%s, il n'y a pas de vaisseaux!",
    multiple_ships_found="Je ne suis pas sûre de votre réponse, essayer ceci :\n%s",
    member_not_found="Je suis désolé, je n'ai trouvé aucun membre.",
    member_ships_modified="%s Voici votre flotte mise à jour :",
    member_ships_invalid="%s, désolé ce vaisseau n'est pas valide:",
    member_ship_not_found="%s, désolé mais vous n'avez pas ce vaisseau.",
    ship_price_unknown="Désolé je ne connais pas le tarif de *%s*  **%s**.",
    ship_from_report_not_found="Désolé je ne trouve rien sur *%s*.",
    ship_price_report="Le prix de *%s* a été mis à jour à *%s*",
    new_version="Salut! J'ai trouvé des nouvelles:\n%s",
    road_map_not_found="Désolé, je n'ai rien trouvé de tel. Vous pouvez essayer quelque chose comme:\n```%s```",
    something_went_wrong="Quelque chose a mal tourné...",
    success="Terminé !",
    found_nothing="Désolé je n'ai rien trouvé..."
)

commands_fr = Commands(
    help="aide",
    fleet="flotte",
    add_ship="ajout_vaisseau",
    remove_ship="retirer_vaisseau",
    clear_member_ships="effacer ma liste de vaisseaux",
    remove_member="retirer_membre",
    prices="prix",
    ship="vaisseaux",
    compare="comparer",
    releases="releases",
    roadmap="roadmap",
    trade="commerce",
    trade_prices="prix_du_commerce",
    mining="minage",
    trade_report="rapport_de_commerce",
    mining_report="rapport_de_minage",
)
