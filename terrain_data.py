
BASELINE, FLANK, CENTER = range(1010, 1013)

LIGHT = {BASELINE: {
        'Artillery Move': 'Road',
        'Artillery Reload': 'Road',
        'Cavalry Move': 'Open',
        'Deploy': 'Light Wood',
        'Dress Ranks': 'Open',
        'Heroic Action': "Player's Choice",
        'Infantry Move': 'Road & Village',
        'Infantry Reload': 'Light Hill',
        'Leadership': 'Road',
        'Major Morale': 'Light Water Feature',
        'Maneuver': 'Light Wood',
        'Melee': 'Light Hill',
        'Tactical Advantage': 'Village'
         },
         FLANK: {
        'Artillery Move': 'Road',
        'Artillery Reload': 'Road',
        'Cavalry Move': 'Open',
        'Deploy': 'Light Wood',
        'Dress Ranks': 'Open',
        'Heroic Action': "Player's Choice",
        'Infantry Move': 'Light Water Feature',
        'Infantry Reload': 'Light Water Feature',
        'Leadership': 'Road',
        'Major Morale': 'Light Wood',
        'Maneuver': 'Light Water Feature',
        'Melee': 'Light Hill',
        'Tactical Advantage': 'Village'
         },
         CENTER: {
        'Artillery Move': 'Open',
        'Artillery Reload': 'Light Wood',
        'Cavalry Move': 'Open',
        'Deploy': 'Light Wood',
        'Dress Ranks': 'Open',
        'Heroic Action': "Player's Choice",
        'Infantry Move': 'Light Hill',
        'Infantry Reload': 'Open',
        'Leadership': 'Open',
        'Major Morale': 'Light Wood',
        'Maneuver': 'Impassable',
        'Melee': 'Light Hill',
        'Tactical Advantage': 'Village'
         }

}

MEDIUM = {BASELINE: {
        'Artillery Move': 'Light Hill',
        'Artillery Reload':  'Light Hill',
        'Cavalry Move':  'Light Hill',
        'Deploy':  'Village',
        'Dress Ranks': 'Open',
        'Heroic Action': "Player's Choice",
        'Infantry Move': 'Light Hill & Road',
        'Infantry Reload': 'Light Hill',
        'Leadership': 'Heavy Hill & Road',
        'Major Morale': 'Impassable',
        'Maneuver': 'Road',
        'Melee': 'Light Wood',
        'Tactical Advantage': 'Village'
         },
         FLANK: {
        'Artillery Move': 'Road',
        'Artillery Reload': 'Road',
        'Cavalry Move': 'Open',
        'Deploy': 'Village',
        'Dress Ranks': 'Open',
        'Heroic Action': "Player's Choice",
        'Infantry Move': 'Heavy Hill',
        'Infantry Reload': 'Light Water Feature',
        'Leadership': 'Heavy Water Feature & Road',
        'Major Morale': 'Light Wood & Light Water Feature',
        'Maneuver': 'Road',
        'Melee': 'Light Wood',
        'Tactical Advantage': 'Village'
         },
         CENTER: {
        'Artillery Move': 'Open',
        'Artillery Reload': 'Light Wood',
        'Cavalry Move': 'Open',
        'Deploy': 'Light Wood',
        'Dress Ranks': 'Open',
        'Heroic Action': "Player's Choice",
        'Infantry Move': 'Open',
        'Infantry Reload': 'Open',
        'Leadership': 'Light Wood',
        'Major Morale': 'Heavy Wood',
        'Maneuver': 'Open',
        'Melee': 'Light Wood',
        'Tactical Advantage': 'Village'
         }
}

HEAVY = {BASELINE: {
        'Artillery Move':  'Heavy Hill',
        'Artillery Reload':  'Heavy Hill',
        'Cavalry Move':  'Heavy Hill',
        'Deploy':  'Village',
        'Dress Ranks': 'Open',
        'Heroic Action': "Player's Choice",
        'Infantry Move': ' Heavy Hill & Heavy Wood',
        'Infantry Reload': 'Heavy Hill',
        'Leadership': 'Heavy Water Feature',
        'Major Morale': 'Light Wood',
        'Maneuver': 'Road & Impassable',
        'Melee': 'Heavy Hill',
        'Tactical Advantage': 'Village'
         },
         FLANK: {
        'Artillery Move': 'Heavy Hill & Road',
        'Artillery Reload': 'Heavy Hill & Road',
        'Cavalry Move': 'Light Water Feature',
        'Deploy': 'Heavy Hill & Village',
        'Dress Ranks': 'Open',
        'Heroic Action': "Player's Choice",
        'Infantry Move': 'Impassable',
        'Infantry Reload': 'Heavy Water Feature',
        'Leadership': 'Road',
        'Major Morale': 'Heavy Water Feature',
        'Maneuver': 'Road & Impassable',
        'Melee': 'Heavy Hill',
        'Tactical Advantage': 'Village & Heavy Water Feature'
         },
         CENTER: {
        'Artillery Move': 'Light Wood',
        'Artillery Reload': 'Light Wood',
        'Cavalry Move': 'Open',
        'Deploy': 'Light Hill & Light Wood',
        'Dress Ranks': 'Open',
        'Heroic Action': "Player's Choice",
        'Infantry Move': 'Village',
        'Infantry Reload': 'Light Hill',
        'Leadership': 'Village & Heavy Hill',
        'Major Morale': 'Heavy Wood',
        'Maneuver': 'Impassable',
        'Melee': 'Heavy Hill',
        'Tactical Advantage': 'Village'
         }
}
