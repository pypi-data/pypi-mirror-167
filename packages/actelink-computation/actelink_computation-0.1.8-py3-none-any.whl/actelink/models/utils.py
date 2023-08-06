def get_level_params(contexts: dict) -> dict:
    params = {}
    params["demography"]      = contexts["demography"]
    params["regime"]          = contexts["regime"]
    params["levelOfProduct"]  = contexts["levelOfProduct"]
    return params

def get_context_params(context: dict, params: dict, replace_br: bool):
    # dunno why parameters is an array..
    params["parameters"] = context["parameters"][0]
    if replace_br is True and params["parameters"]["bases"][0]["guaranteeValue"]["unit"] == "% BR":
        params["parameters"]["bases"][0]["guaranteeValue"]["unit"] = "% BRSS"
