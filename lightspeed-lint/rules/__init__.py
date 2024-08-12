from lightspeed_lint.rules.rule_001_no_hardcoded_ips import NoHardcodedIPs


def load_rules():
    return [
        NoHardcodedIPs()
    ]
