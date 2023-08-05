import praw

def getinstance(path):
    """
    Script that returns PRAW instance for user.
    
    Parameters
    ----------
    path : str
        Path to config.txt file which contains client_id, client_secret, password, username, user_agent

    Returns
    -------
    instance
        The PRAW Reddit Object as documented in PRAW's documentation
    """
    config_path = path 
    config_file = config_path + "/" + "config.txt"
    config_vars = {}
    with open(config_file, "r") as file:
        for line in file:
            name, value = line.split("=")
            config_vars[name] = eval(value.strip())

    instance = praw.Reddit(
        client_id=config_vars["client_id"],
        client_secret=config_vars["client_secret"],
        password=config_vars["password"],
        username=config_vars["username"],
        user_agent=config_vars["user_agent"],
    )
    
    return instance