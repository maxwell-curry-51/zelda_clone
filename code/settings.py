# game setup
from tkinter import Grid


# SETTINGS
# GLOBALS
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64

#SPRITESHEET MAPPINGS
#  CODES - 2 char codes (owner of sprite, direction)
#  MAPPING
#   PLAYER
#    pr - player right
#    pu - player up
#    pd - player down
#   ENEMY
#    er - enemy right
#    eu - enemy up
#    ed - enemy down
SAMPLE_1 = [
['er','er','ed','ed','eu','  ','  ','  ','  ','  ',],
['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',],
['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',],
['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',],
['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',],
['  ','pr','pr','pd','pd','pd','pu','pu','pu','  ',],
['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',],
['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ',],
]
SAMPLE_2 = [
['pd','pd','pd','pu','pu','pu','ed','ed','ed','eu','eu','eu',],
]
SAMPLE_3 = [
['pr','pr','pr','pr','er','er','er'],
]

# MAP GRIDS
#  CODES
#   INVISIBLE BARRIERS
#    4 QUADRANT
#     x - all 4 quadrant barrier
#    3 QUADRANT
#     4 - all except bottom right quarter
#     5 - all except bottom left quarter
#     6 - all except top right quarter
#     7 - all except top left quarter
#    2 QUADRANT
#     t - top half
#     b - bottom half
#     l - left half
#     r - right half
#    1 QUADRANT
#     0 - top left quarter
#     1 - top right quarter
#     2 - bottom left quarter
#     3 - bottom right quarter
#   BREAKABLE BARRIERS
#   PORTALS
#     d - portal location
#   PLAYER
#     p - player spawn point
#   ENEMIES
#     e - basic path driven enemy
#     h - homing enemy
#   ITEMS
#    

# MAPS
EP_0_MAP = [
['x','x','d',' ','x','x','x','x','x','x','d',' ','x','x','x','x','x','x','d',' ','x','x'],
['x','4','p',' ','5','x','x','x','x','4','p',' ','5','x','x','x','x','4','p',' ','5','x'],
['x','l',' ',' ','r','x','x','x','x','l','*','*','r','x','x','x','x','l',' ',' ','r','x'],
['x','l',' ',' ','r','x','x','x','x','l','*','*','r','x','x','x','x','l',' ',' ','r','x'],
['x','l',' ',' ','r','x','x','x','x','l','e',' ','r','x','x','x','x','l',' ',' ','r','x'],
['x','l',' ',' ','1','t','x','x','t','0',' ',' ','1','t','x','x','t','0',' ',' ','r','x'],
['x','l',' ',' ',' ',' ','x','x','+',' ',' ',' ',' ',' ','x','x',' ',' ',' ',' ','r','x'],
['x','l',' ',' ',' ',' ','t','t',' ',' ',' ','e',' ',' ','t','t',' ',' ',' ',' ','r','x'],
['x','l',' ',' ',' ','e',' ',' ',' ','s',' ',' ',' ',' ',' ','e',' ',' ',' ',' ','r','x'],
['x','6','b','b','b','b',' ',' ',' ',' ',' ',' ',' ','+',' ',' ','b','b','b','b','7','x'],
['x','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x'],
['x','x','x','x','x','x','b','b','b','b',' ',' ','b','b','b','b','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','p',' ','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]
EP_1_MAP = [
['x','x','x','x','x','x','x','x','x','x','d',' ','x','x','x','x','x','x','x','x','x','x'],
['x','x',' ','x','x','x','x','x','x','t','p',' ','t','x','x','x','x','x',' ','x','x','x'],
['x','x',' ',' ','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x',' ',' ','x','x'],
['x','x',' ',' ','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x',' ',' ','x','x'],
['x','x',' ',' ','x','x','x','x','x','k',' ',' ',' ','x','x','x','x','x',' ',' ','x','x'],
['x','x',' ',' ','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x',' ',' ','x','x'],
['x','x',' ',' ','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x',' ',' ','x','x'],
['x','x',' ',' ','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x',' ',' ','x','x'],
['x','x','x','x','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x'],
['x','x',' ',' ','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x',' ',' ','x','x'],
['x','x',' ',' ','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x',' ',' ','x','x'],
['x','x','p',' ','x','x','x','x','x','b','p',' ','b','x','x','x','x','x','p',' ','x','x'],
['x','x','d',' ','x','x','x','x','x','x','d',' ','x','x','x','x','x','x','d',' ','x','x'],
]
EP_EP_BOSS = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','4','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','5','x'],
['x','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','x'],
['x','6','b','b','b','2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','3','b','b','b','7','x'],
['x','x','x','x','x','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','x','x','x','x','x'],
['x','x','x','x','x','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','x','x','x','x','x'],
['x','x','x','x','x','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','x','x','x','x','x'],
['x','x','x','x','x','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','x','x','x','x','x'],
['x','x','x','x','x','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','x','x','x','x','x'],
['x','x','x','x','x','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','x','x','x','x','x'],
['x','x','x','x','x','l',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','r','x','x','x','x','x'],
['x','x','x','x','x','6','b','b','b','b','p',' ','b','b','b','b','7','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','d',' ','x','x','x','x','x','x','x','x','x','x'],
]

# PORTAL MAPPINGS
#  Destination Map
#  Destination Map Spawn Number
#  Destination Spawn Centering code
EP_0_PORTALS = [('EP_1_MAP',1,'m'),('EP_1_MAP',2,'m'),('EP_1_MAP',3,'m')]
EP_1_PORTALS = [('EP_BOSS',0,'m'),('EP_0_MAP',0,'m'),('EP_0_MAP',1,'m'),('EP_0_MAP',2,'m')]
EP_BOSS_PORTALS = [('EP_1_MAP',0,'m')]

# SETTINGS OBJECT
#  Current Map Name
SETTING_INDEXES = ['EP_0_MAP', 'EP_1_MAP', 'EP_BOSS']
#  Image Grid
#  Image Portal Mapping
#  Image File
#  Tile Size
#  Image Size
#  Image Shift
SETTINGS = [
    (EP_0_MAP, EP_0_PORTALS,'../graphics/dungeon/EP_0.png',64,(2700, 2500),(-684,-780)),
    (EP_1_MAP, EP_1_PORTALS,'../graphics/dungeon/EP_1.png',64,(2700, 2500),(-703,-780)),
    (EP_EP_BOSS, EP_BOSS_PORTALS,'../graphics/dungeon/EP_boss_room.png',64,(2700, 2500),(-684,-775))]

# OLD ASSETS
WORLD_MAP = [
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','p',' ',' ',' ',' ',' ','h',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ','e',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ','x'],
['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ','D',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]
SUB_WORLD_MAP = [
['x','x','x','x','x'],
['x',' ',' ',' ','x'],
['x',' ','p',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ',' ',' ','x'],
['x',' ','D',' ','x'],
['x',' ',' ',' ','x'],
['x','x','x','x','x'],
]
EP_0_MAP_copy = [
['x','x','x','x','x','x','d',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','d',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','d',' ','x','x','x','x'],
['x','x','x','x','x','x',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ','x','x','x','x'],
['x','x','x','x','x','x','p',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','p',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','p',' ','x','x','x','x'],
['x','x','x','x','x','x',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ','x','x','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ','p',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',' ',' ',' ',' ','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]