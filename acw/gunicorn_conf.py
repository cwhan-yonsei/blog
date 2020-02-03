import multiprocessing

bind = "unix:/home/cwahn/home-server-2/acw/acw_gn.sock"

workers = multiprocessing.cpu_count() * 2

threads = multiprocessing.cpu_count() * 2

timeout = 15

keep_alive = 2

limit_request_line = 4094

reload = True

check_config = True

deamon = True

user = "cwahn"

group = "cwahn"

log_file = "/home/cwahn/home-server-2/acw/gunicorn.log"