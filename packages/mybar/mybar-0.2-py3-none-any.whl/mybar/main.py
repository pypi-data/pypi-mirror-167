from .base import *
from .field_funcs import *

CONFIG_FILE = 'bar.json' #'~/bar.json'
CSI = '\033['  # Unix terminal escape code (control sequence introducer)
CLEAR_LINE = '\x1b[2K'  # VT100 escape code to clear line
HIDE_CURSOR = '?25l'
UNHIDE_CURSOR = '?25h'
COUNT = [0]



def run():
    fhostname = Field(name='hostname', func=get_hostname, run_once=True, term_icon='')
    fuptime = Field(name='uptime', func=get_uptime, kwargs={'fmt': '%-jd:%-Hh:%-Mm'}, term_icon='Up:')
    fcpupct = Field(name='cpu_usage', func=get_cpu_usage, interval=2, threaded=True, term_icon='CPU:')
    fcputemp = Field(name='cpu_temp', func=get_cpu_temp, interval=2, threaded=True, term_icon='')
    fmem = Field(name='mem_usage', func=get_mem_usage, interval=2, term_icon='Mem:')
    fdisk = Field(name='disk_usage', func=get_disk_usage, interval=2, term_icon='/:')
    # fbatt = Field(name='battery', func=get_battery_info, interval=1, overrides_refresh=False, term_icon='Bat:')
    fbatt = Field(name='battery', func=get_battery_info, interval=1, overrides_refresh=True, term_icon='Bat:')
    fnet = Field(name='net_stats', func=get_net_stats, interval=4, term_icon='', threaded=False)

    fdate = Field(
        # fmt="<3 {icon}{}!",
        name='datetime',
        func=get_datetime,
        interval=1/8,
        overrides_refresh=True,
        term_icon='?'
    )
    fcounter = Field(name='counter', func=counter, interval=1, args=[COUNT])

    # fdate = Field(name='datetime', func=get_datetime, interval=1, overrides_refresh=False, term_icon='')
    # fdate = Field(func=get_datetime, interval=0.5, overrides_refresh=False)
    # fdate = Field(func=get_datetime, interval=1)
    # mocpline = Field(name='mocpline', func=

    global fields
    fields = (
        Field(
            name='isatty',
            func=(lambda args=None, kwargs=None: str(bar.in_a_tty)),
            # icon='TTY:',
            run_once=True,
            # interval=0
        ),
        # fhostname,
        # fuptime,
        fcpupct,
        fcputemp,
        fmem,
        fdisk,
        fbatt,
        fnet,
        fdate,
        # fcounter,
    )

    # fields = [Field(name='test', interval=1/16, func=(lambda args=None, kwargs=None: "WORKING"), overrides_refresh=True, term_icon='&', gui_icon='@')]

    global bar
    # bar = Bar(fields=fields)
    # bar = Bar(fields=fields, sep=None, fmt=None)  # Raise IncompatibleParams

    # fmt = "Up{uptime} | CPU: {cpu_usage}, {cpu_temp}|Disk: {disk_usage} Date:{datetime}..."
    # fmt = None
    # bar = Bar(fmt=fmt)

    # bar = Bar(fields=[fdate, fcount, fhostname, fuptime])

    # bar = Bar(fields='uptime cpu_usage cpu_temp mem_usage datetime datetime datetime disk_usage battery net_stats datetime'.split())


    global CFG
    # CFG = Config('bar.conf')
    # CFG = Config('bar.json')
    CFG = Config(CONFIG_FILE)
    bar = CFG.get_bar()

##    if not os.path.exists(file):
##        CFG.write_config(file, defaults)

    bar.run()


if __name__ == '__main__':
    main()


