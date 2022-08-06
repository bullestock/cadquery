import cadquery as cq
from cq_warehouse.fastener import HexNut, SocketHeadCapScrew, SetScrew
MM = 1
IN = 25.4 * MM

s = SocketHeadCapScrew(size="M8-1.25", length=15, fastener_type="iso4762")#"iso4017")
show_object(s)
