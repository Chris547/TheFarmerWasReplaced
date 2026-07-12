import config

# TODO: use a dictionary to allow source-based level overrides
level = 4

quick_print("log.level", level)

# DEBUG = 5
# INFO  = 4
# WARN  = 3
# ERROR = 2
# FATAL = 1
# NONE  = 0


def debug(source, message):
	if level >= 5:
		quick_print("DEBUG:", source, message)

	
def info(source, message):
	if level >= 4:
		quick_print("INFO:", source, message)

	
def warn(source, message):
	if level >= 3:
		quick_print("WARN:", source, message)


def error(source, message):
	if level >= 2:
		quick_print("ERROR:", source, message)


def fatal(source, message):
	if level >= 1:
		quick_print("FATAL:", source, message)


# tests
#debug("source", "debug")
#info("source", ("info", 2, 3, 4))
#warn("source", "warning")
#error("source", "error")
#fatal("source", "fatal")
