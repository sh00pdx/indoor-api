from app.services.auth import AuthServiceSingleton

check_token_deps = {
    "services": {
        "AuthService": AuthServiceSingleton
    }
}
