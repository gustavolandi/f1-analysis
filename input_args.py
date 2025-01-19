import sys

def input_args():
    args = {}
    for arg in sys.argv[1:]:
        if '=' in arg:
            key, value = arg.split('=', 1)
            args[key] = value

    required_args = ['year', 'weekend', 'session']
    missing_args = [arg for arg in required_args if arg not in args]

    if missing_args:
        print(f"Error: The following parameters are necessary - {', '.join(missing_args)}")
        sys.exit(1)
    
    return args