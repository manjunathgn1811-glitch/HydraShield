TRAPS = [
    "/admin",
    "/root",
    "/database",
    "/backup"
]

def is_trap(path):

    return path in TRAPS