"""Exercise 5.5 — EAFP vs LBYL (script, no test).

Read cfg["db"]["port"] from a nested dict three ways:
1. LBYL: `in` checks at each level
2. EAFP: try/except KeyError
3. .get chains with defaults

Run each against: a complete cfg, cfg missing "db", cfg missing "port".
In comments: which reads best? Which can silently hide a real bug (typo in
a key)? Which would you use in TaskForge and why?

Skills practiced:
- EAFP vs LBYL styles
- KeyError handling and .get chains
"""

def port_lbyl(cfg, default=None):
    """Read the database port by checking before each lookup."""
    if "db" in cfg and "port" in cfg["db"]:
        return cfg["db"]["port"]
    return default


def port_eafp(cfg, default=None):
    """Read the database port and handle an expected missing key."""
    try:
        return cfg["db"]["port"]
    except KeyError:
        return default


def port_get(cfg, default=None):
    """Read the database port using chained dictionary getters."""
    return cfg.get("db", {}).get("port", default)


# EAFP is the clearest version when db.port is expected to exist: it shows the
# successful operation directly and catches only the anticipated KeyError.
# LBYL works but becomes noisy as nesting grows. The .get version is concise
# for genuinely optional configuration, but a typo such as "prot" silently
# returns the default and can hide a bug. In TaskForge I would use EAFP for
# required settings and translate KeyError into a meaningful configuration
# error; I would reserve .get for settings with documented defaults.


if __name__ == "__main__":
    configs = {
        "complete": {"db": {"port": 5432}},
        "missing db": {},
        "missing port": {"db": {}},
    }

    for name, cfg in configs.items():
        print(name)
        print("  LBYL:", port_lbyl(cfg))
        print("  EAFP:", port_eafp(cfg))
        print("  get: ", port_get(cfg))
