def print_error(err, msg):
    """
        Prints out colored error info
    """
    # get error type for debug purposes
    etype = type(err).__name__

    # format error message
    err_msg = '\033[91m{} {}:\n{}\033[0m'.format(msg, etype, err)

    # log to stdout
    print(err_msg)
