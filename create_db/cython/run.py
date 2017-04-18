import add_avg_gain
import resource

resource.setrlimit(
	resource.RLIMIT_CORE,
	(resource.RLIM_INFINITY, resource.RLIM_INFINITY))