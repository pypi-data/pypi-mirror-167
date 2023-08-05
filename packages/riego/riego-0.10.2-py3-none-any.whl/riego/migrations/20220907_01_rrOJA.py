"""

"""

from yoyo import step

__depends__ = {'20210214_01_WyOHg'}

steps = [
    step('''ALTER TABLE "boxes" ADD COLUMN "rssi"       INTEGER'''),
    step('''ALTER TABLE "boxes" ADD COLUMN "link_count" INTEGER'''),
    step('''ALTER TABLE "boxes" ADD COLUMN "down_time"  TEXT''')
]
