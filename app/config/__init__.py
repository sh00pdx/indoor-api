from decouple import config

DATABASE = {
    "host": config("DB_HOST", "localhost"),
    "port": int(config("DB_PORT", default=3306)),
    "name": config("DB_NAME", default="indoor"),
    "user": config("DB_USER", "root"),
    "pass": config("DB_PASS", None),
}

ENV = config("ENVIRONMENT", default="qa")

TOKEN = "2!551t4D8?eJjamsapxLRwcf7ImambmqRDEAPB4gS0Bp8UaryoQik2J5YJPwwTNbtxiZHOizWWFvwbdBkOGLzKqs/sPFXPSuuKCLLNVpdz7Vbo/Y/?n=lmPqKDrXMCH/VcauGW3DiGrbIZ6h0EnjjDlxlooaVqfb/cMRPA1zscM8Xb2p3Oc6q95v5eD36NccZEt2eXJh62BnilRCzIUibgm8?g/SyJ/VWbsFf0=SyRVHjkoHN7UsCtLo7ew/wtCu"
